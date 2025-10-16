// ---- Nano (ATmega328P): 4x HC-SR04 + BNO055 -> UART D2/D3 (CSV + Laps) ----
// CSV format: l90, l45, r45, r90, laps
// Requirements: HC-SR04 + BNO055 (without Adafruit libraries)

#include <Wire.h>
#include <SoftwareSerial.h>
#include <NewPing.h>

// ------------------- ULTRASONIC CONFIGURATION -------------------
// Maximum distance in cm for ultrasonic readings
#define MAX_DISTANCE 200

// Ultrasonic sensor pin configuration: trigger, echo, max distance
NewPing r90(12, 11, MAX_DISTANCE);
NewPing r45(10, 9, MAX_DISTANCE);
NewPing l45(8, 7, MAX_DISTANCE);
NewPing l90(6, 5, MAX_DISTANCE);

// ------------------- LAP DETECTION CONFIGURATION -------------------
#define LAPS_METHOD 3 // Method 3 combines rotation and angular gate detection

// Defines how many ticks correspond to one full rotation (360° * 16)
const long LAP_TICKS16 = 360L * 16;
// Minimum time (ms) between laps to avoid false detections
const unsigned long LAP_MIN_MS = 3000;

const int GATE_HALF_WIDTH = 15;
const int GATE_HYST = 5;
int c = 0;

// ------------------- UART COMMUNICATION --------------------------
// Software serial communication: TX = D3 (to master EV3)
SoftwareSerial link(2, 3);  

// ------------------- BNO055 MINIMAL IMPLEMENTATION ----------------
// Minimal I2C communication to read heading directly from BNO055 sensor
namespace BNO {
static uint8_t ADDR = 0x28;
const uint8_t REG_CHIP_ID = 0x00;
const uint8_t REG_EUL_HEADING_LSB = 0x1A;
const uint8_t REG_OPR_MODE = 0x3D;
const uint8_t REG_SYS_TRIG = 0x3F;
const uint8_t REG_PAGE_ID = 0x07;
const uint8_t REG_PWR_MODE = 0x3E;
const uint8_t REG_UNIT_SEL = 0x3B;
const uint8_t OPR_CONFIG = 0x00;
const uint8_t OPR_NDOF = 0x0C;
const uint8_t PWR_NORMAL = 0x00;

// --- Low-level I2C write ---
inline void write8(uint8_t reg, uint8_t val) {
  Wire.beginTransmission(ADDR);
  Wire.write(reg);
  Wire.write(val);
  Wire.endTransmission();
}

// --- Low-level I2C read (multiple bytes) ---
inline void readLen(uint8_t reg, uint8_t *buf, uint8_t len) {
  Wire.beginTransmission(ADDR);
  Wire.write(reg);
  Wire.endTransmission();
  Wire.requestFrom((int)ADDR, (int)len);
  for (uint8_t i = 0; i < len && Wire.available(); i++) buf[i] = Wire.read();
}

// --- Read a single byte from a register ---
inline uint8_t read8(uint8_t reg) {
  uint8_t v = 0;
  readLen(reg, &v, 1);
  return v;
}

// --- Detect valid BNO055 I2C address (0x28 or 0x29) ---
bool probeAny() {
  delay(700);
  uint8_t posibles[2] = { 0x28, 0x29 };
  for (uint8_t i = 0; i < 2; i++) {
    ADDR = posibles[i];
    for (uint8_t j = 0; j < 10; j++) {
      delay(20);
      if (read8(REG_CHIP_ID) == 0xA0) return true;
    }
  }
  return false;
}

// --- Initialize BNO055 without using external libraries ---
bool begin() {
  if (!probeAny()) return false;
  write8(REG_OPR_MODE, OPR_CONFIG);
  delay(25);
  write8(REG_SYS_TRIG, 0x20);
  delay(700);
  if (!probeAny()) return false;
  write8(REG_PAGE_ID, 0x00);
  delay(5);
  write8(REG_PWR_MODE, PWR_NORMAL);
  delay(10);
  write8(REG_UNIT_SEL, 0x00);
  delay(10);
  write8(REG_OPR_MODE, OPR_NDOF);
  delay(50);

  // Wait until valid heading data is available
  uint32_t t0 = millis();
  while (millis() - t0 < 300) {
    uint8_t b[2];
    readLen(REG_EUL_HEADING_LSB, b, 2);
    if (b[0] || b[1]) break;
    delay(10);
  }
  return true;
}

// --- Read 16-bit heading value (yaw angle) ---
inline int16_t readHeading16() {
  uint8_t b[2];
  readLen(REG_EUL_HEADING_LSB, b, 2);
  return (int16_t)((uint16_t)b[0] | ((uint16_t)b[1] << 8));
}
}  // namespace BNO

// ------------------- ANGLE UTILITIES -----------------
static inline int16_t yawDelta16(int16_t cur, int16_t prev) {
  int16_t d = cur - prev;
  while (d > 2880) d -= 5760;
  while (d < -2880) d += 5760;
  return d;
}
static inline int angDiffDeg(int a, int b) {
  int d = a - b;
  while (d > 180) d -= 360;
  while (d < -180) d += 360;
  return d;
}

// ------------------- STATE VARIABLES --------------------
int16_t yaw_prev16 = 0;
bool yaw_has_prev = false;
long yaw_accum16 = 0;
long yaw_sinceLap16 = 0;
int lap_count = 0;
unsigned long lastLapMs = 0;
int gate0_deg = 0;
bool gate_armed = false;
bool yaw_pending = false;
bool gate_pending = false;
bool bno_ok = false;

// ------------------- LAP CALCULATION FUNCTIONS -------------------
inline bool timeOk() {
  return (millis() - lastLapMs) > LAP_MIN_MS;
}
inline void countedNow() {
  lastLapMs = millis();
}

// --- Detect lap based on accumulated yaw angle ---
void tryCountLapAccumYaw() {
#if (LAPS_METHOD == 1) || (LAPS_METHOD == 3)
  if (labs(yaw_sinceLap16) >= LAP_TICKS16) {
#if (LAPS_METHOD == 1)
    if (timeOk()) {
      lap_count++;
      countedNow();
    }
    yaw_sinceLap16 %= LAP_TICKS16;
#else
    yaw_pending = true;
    yaw_sinceLap16 %= LAP_TICKS16;
#endif
  }
#endif
}

// --- Detect lap based on gate crossing (angle threshold) ---
void tryCountLapGate(int deg_now) {
#if (LAPS_METHOD == 2) || (LAPS_METHOD == 3)
  int dgate = angDiffDeg(deg_now, gate0_deg);
  if (!gate_armed && abs(dgate) > (GATE_HALF_WIDTH + GATE_HYST)) gate_armed = true;
  if (gate_armed && abs(dgate) <= GATE_HALF_WIDTH) {
#if (LAPS_METHOD == 2)
    if (timeOk()) {
      lap_count++;
      countedNow();
    }
    gate_armed = false;
#else
    gate_pending = true;
    gate_armed = false;
#endif
  }
#endif
}

// --- Combine both lap detection methods ---
void resolveLapMethod3() {
#if (LAPS_METHOD == 3)
  if (yaw_pending && gate_pending && timeOk()) {
    lap_count++;
    countedNow();
    yaw_pending = false;
    gate_pending = false;
  }
#endif
}

// ------------------- ULTRASONIC FILTER -------------------
// Median + average filter to remove outliers from sensor readings
#define READS_PER_SENSOR 5
unsigned int filteredPing(NewPing &sensor) {
  int vals[READS_PER_SENSOR];
  int valid = 0;

  // Perform multiple readings
  for (int i = 0; i < READS_PER_SENSOR; i++) {
    unsigned int uS = sensor.ping();
    if (uS > 0) vals[valid++] = uS / US_ROUNDTRIP_CM;
    delay(10);
  }
  if (valid == 0) return 0;

  // Sort values (simple insertion sort)
  for (int i = 1; i < valid; i++) {
    int key = vals[i];
    int j = i - 1;
    while (j >= 0 && vals[j] > key) {
      vals[j + 1] = vals[j];
      j--;
    }
    vals[j + 1] = key;
  }

  // Median-based filter: remove outliers beyond ±15 cm
  int median = vals[valid / 2];
  int sum = 0, count = 0;
  for (int i = 0; i < valid; i++) {
    if (abs(vals[i] - median) < 15) {
      sum += vals[i];
      count++;
    }
  }
  return (count > 0) ? (sum / count) : median;
}

// ------------------- SERIAL DATA -------------------
String line = "";

// ------------------- SETUP -------------------
void setup() {
  Serial.begin(9600);
  link.begin(115200);
  Wire.begin();

  // Initialize BNO055
  bno_ok = BNO::begin();
  if (!bno_ok) link.println(F("ERR_BNO"));
  
  // Save initial heading as gate reference
  if (bno_ok) {
    int16_t h16 = BNO::readHeading16();
    gate0_deg = (int)((h16 + 8) / 16);
  }

  // Print CSV header
  link.println(F("l90,l45,r45,r90,lap_count"));
}

// ------------------- MAIN LOOP -------------------
void loop() {

  // --- Check for serial command to reset laps ---
  if (link.available()) {
    c = link.read();
  } else {
    c = 0;
  }
  if (c == 10) {  // If newline received, reset counters
    lap_count = 0;
    yaw_accum16 = 0;
    yaw_sinceLap16 = 0;
    yaw_has_prev = false;
    gate_armed = false;
    yaw_pending = false;
    gate_pending = false;
  }

  Serial.println(lap_count);

  // --- Filtered ultrasonic readings ---
  int l90b = filteredPing(l90);
  int l45b = filteredPing(l45);
  int r45b = filteredPing(r45);
  int r90b = filteredPing(r90);

  // --- Heading and lap calculation from BNO055 ---
  int pos_deg = 0, deg_now = 0;
  if (bno_ok) {
    int16_t yaw_now16 = BNO::readHeading16();
    deg_now = (int)((yaw_now16 + 8) / 16);
    if (!yaw_has_prev) {
      yaw_prev16 = yaw_now16;
      yaw_has_prev = true;
    } else {
      int16_t d16 = yawDelta16(yaw_now16, yaw_prev16);
      yaw_accum16 += (long)d16;
      yaw_sinceLap16 += (long)d16;
      yaw_prev16 = yaw_now16;
      tryCountLapAccumYaw();
      tryCountLapGate(deg_now);
      resolveLapMethod3();
    }
    pos_deg = (int)(yaw_accum16 / 16L);
  }

  // --- Send CSV line over UART ---
  link.print(l90b);
  link.print(',');
  link.print(l45b);
  link.print(',');
  link.print(r45b);
  link.print(',');
  link.print(r90b);
  link.print(',');
  link.println(lap_count);

  delay(40);
}

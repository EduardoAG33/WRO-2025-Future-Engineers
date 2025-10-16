#include <Wire.h>
#define SLAVE_ADDRESS 0x04
#include <SoftwareSerial.h>
#include <Adafruit_NeoPixel.h>
#include <NewPing.h>

Adafruit_NeoPixel matriz(16, 9, NEO_GRB + NEO_KHZ800);
NewPing frontU(11, 10, 200);

int POT_LUZ = 10;
bool linkSent = false;  // global flag for first-time data sending

// Sensors
int front;  // Local front HC-SR04
int l45;
int r45;
int l90;
int r90;
int laps;
float As6;
float As7;
float rearanalog;
float rearanalog2;

// Mapped data
int frontbyte;
int l45byte;
int r45byte;
int l90byte;
int r90byte;
int A6byte;
int A7byte;

int mind_n_DATO_1;
int8_t tx_byte = 0;

SoftwareSerial sensorLink(2, 5);  // RX=D2, TX=D5
String line = "";

void setup() {
  sensorLink.begin(115200);  // Communication with Nano sensors

  Wire.begin(SLAVE_ADDRESS);  // Initialize I2C as slave
  Wire.onRequest(sendData);
  Wire.onReceive(onreceiveEvent);

  matriz.begin();
  matriz.show();
  int rgb = map(POT_LUZ, 0, 100, 0, 255);
  matriz.fill(matriz.Color(rgb, rgb, rgb), 0, 16);
  matriz.show();
}

void loop() {
  // Local front sensor
  front = frontU.ping_cm();
  As6 = analogRead(A6);
  rearanalog = (As6 * 500) / 1023;
  As7 = analogRead(A7);
  rearanalog2 = (As7 * 500) / 1023;

  // Read CSV line from Nano
  while (sensorLink.available()) {
    char c = sensorLink.read();
    if (c == '\n') {
      processLine(line);
      line = "";
    } else if (c != '\r') {
      line += c;
    }
  }

  // Map data to ranges (-100,100) or (-127,127)
  frontbyte = map(front, 0, 200, -100, 100);
  l45byte = map(l45, 0, 200, -100, 100);
  r45byte = map(r45, 0, 200, -100, 100);
  l90byte = map(l90, 0, 200, -100, 100);
  r90byte = map(r90, 0, 200, -100, 100);
  A6byte = map(rearanalog, 0, 500, -127, 127);
  A7byte = map(rearanalog2, 0, 500, -127, 127);
}

void sendData() {
  switch (mind_n_DATO_1) {
    case 1: tx_byte = l90byte; break;
    case 2: tx_byte = l45byte; break;
    case 3: tx_byte = frontbyte; break;
    case 4: tx_byte = r45byte; break;
    case 5: tx_byte = r90byte; break;
    case 6:
      if (!linkSent) {         // only if it hasn't been sent before
        sensorLink.write(10);  // send the data
        linkSent = true;       // mark as sent
      }
      tx_byte = 0;
      break;
    case 7: tx_byte = laps; break;
    case 8: tx_byte = A6byte; break;
    case 9: tx_byte = A7byte; break;
    default:
      tx_byte = 0;
      break;
  }

  // Reset flag if leaving case 6
  if (mind_n_DATO_1 != 6) linkSent = false;

  Wire.write((uint8_t)tx_byte);
}

void onreceiveEvent() {
  while (Wire.available()) {
    mind_n_DATO_1 = (Wire.read());
  }
}

void processLine(String l) {
  // CSV with 5 values: l90, l45, r45, r90, laps
  int values[5];
  int idx = 0;
  char *token;
  char buf[50];
  l.toCharArray(buf, sizeof(buf));

  token = strtok(buf, ",");
  while (token != NULL && idx < 5) {
    values[idx++] = atoi(token);
    token = strtok(NULL, ",");
  }

  if (idx == 5) {
    l90 = values[0];
    l45 = values[1];
    r45 = values[2];
    r90 = values[3];
    laps = values[4];
  }
}

# WRO-2025-Future-Engineers

Official repository of Team Los Grises Superiores for the Future Engineers – World Robot Olympiad 2025.  
<img width="1000" height="500" alt="image" src="https://github.com/user-attachments/assets/b3e384a1-e19b-4c7f-addf-655aeb32bc3a" />

---

## Team photo
<div align="center">
  <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/8c940a8b-cdcd-43a6-ab31-e2c4029053f1" />
</div>

---

### Eric Daniel Guerrero Uresti
<div align="center">
  <img src="https://github.com/user-attachments/assets/9e1509ca-ad50-48b9-ab44-2787fcce8e0e" alt="Eric Guerrero photo" width="200" height="200">
</div>
**Role:** Programming & Mechanics  

I started participating in robotics tournaments from 2016 to 2019, achieving **two second places** in the Mexican Robotics Tournament (TMR). Due to the **Covid-19 pandemic**, I couldn’t compete again until 2024, when I returned as a **coach** in TMR and WRO, earning a spot at the international competition. I am currently in my final year of **Mechatronics Engineering**.

---

### Paulina Ibarra Martínez
<div align="center">
  <img src="https://github.com/user-attachments/assets/86413c8a-610a-4270-a92d-cb3ed135d41b" alt="Paulina Martinez photo" width="200" height="200">
</div>
**Role:** Programming & Electronics  

I have been part of the **Robotics Club** at *Escuela Normal Superior “Profr. Moisés Sáenz Garza”* for three years, participating in **two Mexican Robotics Tournaments**, achieving **5th place** in the most recent one. Starting in 2024, I became a **junior coach**, achieving **third place** in WRO 2024 and **first place nationally** in the Mexican Robotics Tournament 2025.

---

## Contents
* [Project Overview](#project-overview)
* [Vehicle Photos](#vehicle-photos)
* [Components and Hardware](#components-and-hardware)
* [Mobility Management](#mobility-management)
  * [Chassis](#chassis)
  * [Steering System](#steering-system)
  * [Movement and Traction System](#movement-and-traction-system)
  * [Differential](#differential)
* [Power and Sense Management](#power-and-sense-management)
  * [Power Management](#power-management)
  * [Sense Management](#sense-management)
* [Obstacle Management](#obstacle-management)
  * [Vision System](#vision-system)
* [Calibration](#calibration)
* [ROI Evolution](#roi-evolution)
* [Detection and Avoidance Strategies](#detection-and-avoidance-strategies)
* [Manual Direction PDF](#manual-direction-pdf)
* [Differential Manual PDF](#differential-manual-pdf)
* [Hardware Developer Kit PDF](#hardware-developer-kit-pdf)
* [WRO 2025 Competition Info](#wro-2025-competition-info)

---

## Project Overview

### Abstract

We present the **development and implementation of an autonomous vehicle** designed for the **World Robot Olympiad 2025 – Future Engineers** category.  
The competition challenges participants to design, construct, and program a self-driving car capable of completing specific tasks under variable environmental and rule-based conditions.

The **Future Engineers** category consists of **two main challenges**:

1. **Open Challenge**  
   - The vehicle must autonomously complete **three laps** on a predefined track.  
   - The **starting position** and **driving direction** (clockwise or counterclockwise) are **randomly assigned** before each run.

2. **Obstacle Challenge**  
   - Similar to the Open Challenge, but the vehicle must **detect and react to colored pillars** acting as traffic signals:  
     - **Red pillars → Turn right**  
     - **Green pillars → Turn left**

**Documentation:**  
Documentation is a critical component of the challenge, as it reflects the team’s **engineering process**. Teams are required to maintain a **public repository** including code, CAD files, logs, and other technical documentation.

For full rules and official specifications:  
🔗 [WRO 2025 Future Engineers – General Rules (PDF)](https://wro-association.org/wp-content/uploads/WRO-2025-Future-Engineers-Self-Driving-Cars-General-Rules.pdf)

---

## Vehicle Photos

---

## Components and Hardware

| Component | Description | Image | Purchase Link |
|-----------|------------|-------|---------------|
| **45544 LEGO MINDSTORMS Education EV3 Core Set** | Forms the foundational structure and chassis. | <img width="100" height="100" alt="image" src="https://github.com/user-attachments/assets/a725c977-b28b-4b5d-b95c-506c84cd6706" /> | [Buy here](https://bricks-store.com/esp/item/585/66/45544-set-base-lego-mindstorms-education-ev3) |
| **OpenMV Cam H7 Plus** | Smart camera for navigation and obstacle detection. | <img width="100" height="100" alt="image" src="https://github.com/user-attachments/assets/2f1dc12c-a2f9-4e47-b665-d9b37091a8ce" />| [Buy here](https://openmv.io/products/openmv-cam-h7-plus) |
| **HC-SR04 Ultrasonic Sensor** | Distance measurement sensor | <img width="100" height="1000" alt="image" src="https://github.com/user-attachments/assets/f55c9c1f-b8f7-4d51-9b24-01f51de329b8" />| [Buy here](https://uelectronics.com/producto/sensor-ultrasonico-hc-sr04/) |
| **Arduino Nano** | ATmega328-based microcontroller for control tasks. | <img width="100" height="100" alt="image" src="https://github.com/user-attachments/assets/22e8f59c-909d-4ff2-b637-dc03e15f4de6" /> | [Buy here](https://www.steren.com.mx/placa-de-desarrollo-nano.html) |
| **4x4 RGB LED Matrix** |Compact display module consisting of 16 individual LEDs arranged in a 4-row by 4-column grid | <img width="100" height="100" alt="image" src="https://github.com/user-attachments/assets/1dfe866c-7431-4e3f-93b5-e756a8c59637" />| [Buy here](https://mvelectronica.com/producto/matriz-de-led-rgb-4x4-ws2812-16bits-a-5v-led-5050) |
| **LTC1871 DC-DC Step-up Boost Converter** | Increases low input voltage to a stable higher output. | <img width="100" height="100" alt="image" src="https://github.com/user-attachments/assets/5ebb04f5-a49e-4a5f-b0ff-865bd1fc2c5e" /> | [Buy here](https://mvelectronica.com/producto/elevador-de-voltaje-ltc1871-dc-dc-step-up-boost-entrada-3-35v-salida-3-5-35v-6a#2) |

---

## Mobility Management

### Chassis
The main chassis consists of LEGO pieces selected for their accessibility and for enabling a compact and efficient design. Initially, the prototype was designed using Studio 2.0 software to ensure proper part selection and structural balance.  
For the second level, an acrylic base (acrylate polymer) was used to support the ultrasonic sensors. The shape of this base was customized as part of the design by applying heat to specific areas to mold it into the desired form.  
This level integrates five ultrasonic sensors, strategically distributed to enhance environmental detection and obstacle avoidance.

<div align="center">
<img width="800" height="800" alt="Ultrasonic and PCB Base" src="https://github.com/user-attachments/assets/48febdb7-b3fb-46fc-b429-0648d3b4971d" />
</div>

The elaboration process:

Using a heat gun, each side of the acrylic base designated for the sensors was carefully heated. Once the material reached the appropriate temperature, it was bent using a mold to achieve the 90° angle required for the optimal positioning and field of view of the sensors.

<div align="center">
  <img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/53dec651-0a3b-47fa-895d-e4c19290b290" />     
  <img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/6d716c07-a7b4-4b70-b3c2-c8264ffc2f77" />
</div>

## The final result is mounted on the robot  
<div align="center">
<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/7e76597a-44b9-4264-923c-65cb95d99f65" />
</div>

This base is attached to the chassis using four screws in the middle to give it stability, and on top of this locate the PCB is located where the ultrasonic sensors are connected.

The measurements for the sensor support can be found in the datasheet.



<div align="center">
<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/034fa407-525b-413a-86d8-a455544e789a" />
</div>

## DATASHEET:

https://github.com/EduardoAG33/WRO-2025-Future-Engineers/blob/main/Others/HC-SR04_Datasheet_with_Dimensions%20(1).pdf


And for the upper level of the robot, we have the support for the camera and the Neo pixel light:  

<div align="center">
<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/e680e149-5586-4c7b-b0e2-6f53eb4f0bf5" />

The support is positioned at a 70° inclination to ensure the vehicle remains within the maximum allowed height. This angle was carefully chosen to optimize the camera’s field of view, as detailed in the Power and Sense Management section.



**Chassis render**
<div align="center">
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/5a8c0801-5dba-4137-ac2b-e9e2eaf370f1" />

**Assembly manual:**
[chassis assambly instruction.pdf](https://github.com/user-attachments/files/22890187/chassis.assambly.instruction.pdf)

**material that makes up the structure of the chassis:**
<div align="center">
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/6be42468-d342-4a3f-bf52-336521bc3e64" />

<div align="center">
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/3d160bbb-81db-4c22-88aa-1f6bce73b8f8" />

<div align="center">
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/d0c6ef1d-8a5d-4c55-8a12-6d94522b6061" />

In the Mexican National Tournament, we only used one differential, and the robot dimensions were both wider and taller. For the updated version, we decided to implement two differentials, as this configuration provides significantly better control when moving forward. Additionally, reducing the robot’s overall dimensions helps prevent collisions with obstacles and makes it easier to maneuver around them.



### Steering System
The EV3’s middle motor converts rotational motion into steering movement through a gear train mechanism. The wheels are linked by a connecting rod, allowing them to move freely. With the assistance of the front differential, this setup transmits motion through the drivetrain to the rear motors, enabling smooth and controlled movement.

The steering rotation is limited to 45 degrees due to the chassis design; however, this range is sufficient for proper turning and obstacle avoidance. If needed, the rotation angle can be further reduced through the block programming.
Functionality

Pinion (circular gear): The circular gear located at the center of the structure. When it rotates, it moves the rack from side to side.

Rack (toothed bar): A long bar with teeth that meshes with the pinion. As the pinion turns, the rack slides horizontally.

Wheel connection: The ends of the rack are linked to the wheels through steering arms. When the rack moves, it pushes or pulls these arms, causing the wheels to turn.

<div align="center">
  <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/6fa1eabc-dd34-4a60-99e5-533a9b5d4c33" />

</div>

  **Steering system render**

<div align="center">
  <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/7d3d6e34-4af9-4f2e-b322-6381a5fed5f1" />

</div>

**material that makes up the structure of the steering:**
<div align="center">
 <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/5f12ed7e-0da7-49d1-aecc-cf8525e78320" />
  
**Assembly manual**
</div>
[Sterring system manual.pdf](https://github.com/user-attachments/files/22892572/Sterring.system.manual.pdf)



---

### Movement and Traction System
Two medium motors with differential system transmit energy to wheels. Transmission: 20-tooth → 12-tooth gears → 28-tooth → 20-tooth driving wheels. Position accuracy ±1°, torque 0.08 Nm, speed 240 RPM.
According to the competition rules, the engines cannot be mounted directly on the wheels. Therefore, we chose to implement a transmission system connected to the differential, allowing the engine’s motion to be transferred to the tires, causing them to rotate.
We decided to use two motors because they offer greater speed, power, and stability to the vehicle’s base compared to using only one. This configuration allows for a more balanced distribution of torque, improving traction and control during movement. After testing different options, we chose the medium LEGO motor because it provides an optimal balance between size, weight, and energy efficiency, making it ideal for our chassis design. Additionally, its compact structure facilitates integration into the transmission system while maintaining low power consumption and reliable performance.

**material that makes up the structure of the traction system:**

<div align="center">
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/5b2d5fdf-bf02-4cb2-97f9-ac3fb9f56719" />

</div>

**Traction system render**

<div align="center">
 <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/de4066aa-9ef0-4369-a0e5-4047937f75a1" />

</div>

**Traction system manual**
[traction system manual.pdf](https://github.com/user-attachments/files/22892680/traction.system.manual.pdf)


---

### Differential
Distributes torque to wheels, enabling smooth cornering. Input via pinion and crown gears. Outer wheel rotates faster in turns, inner wheel slower, straight motion equal.

<div align="center">
  <img width="500" height="400" alt="Differential example" src="https://github.com/user-attachments/assets/841f8551-b8cd-43e2-a964-24c97eb4f7ce" />
  <p><em>Image 4.1: Differential example</em></p>
</div>

---

## Power and Sense Management
The Power and Sensor Management system of the vehicle is engineered to optimize energy distribution and ensure reliable operation of all electronic components. It carefully regulates the power supply to motors and sensors, maintaining stability and efficiency under varying load conditions. This system enables precise control over sensor readings and motor performance, supporting accurate navigation, obstacle detection, and overall vehicle functionality.
   
   **Battery for EV3:**
   
<div align="center">
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/baf83fc5-b1e4-444e-b0d3-33d77a03abcb" />

   **Specifications:**
   
   | Specification       | Details |
|--------------------|--------|
| **Battery Type**       | Rechargeable Lithium-Ion (Li-Ion)  |
| **Nominal Voltage**     | 7.4 V (Li-Ion) |
| **Capacity**            | 2000 mAh (Li-Ion) |
| **Typical Usage Time**  | Approximately 1–2 hours with intensive use of motors and sensors |
| **Charging Time**       | 1.5 – 2 hours (Li-Ion) |
| **Weight**              | 160 g (Li-Ion) |
| **Connector**           | Integrated in EV3 Brick |
| **Note**                | Using the official rechargeable Li-Ion battery is recommended for optimal performance and to avoid voltage variation from AA batteries |

This battery is the recommended power source for the LEGO EV3. There are two options: the official rechargeable battery or six AA batteries. Using the official battery is preferable, as it provides a stable and consistent voltage, ensuring reliable operation of motors and sensors under varying loads. Additionally, it offers longer runtime, making it ideal for extended use and competitive.

**Battery 18650**

<div align="center">
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/343775dc-0e65-4a3e-8732-99fa9c5848e2" />

**Specifications:**

| Specification           | Description                                    |
|-------------------------|------------------------------------------------|
| **Type**                | Li-ion Rechargeable                            |
| **Model**               | 18650                                          |
| **Nominal Voltage**     | 3.7 V                                          |
| **Full Charge Voltage** | 4.2 V                                          |
| **Capacity**            | 2600–3500 mAh (typical)                        |
| **Discharge Current**   | 5–10 A (continuous), up to 20 A (peak)         |
| **Charging Current**    | 0.5–1 C                                        |
| **Dimensions**          | 18 mm diameter × 65 mm length                  |
| **Weight**              | ~45 g                                          |
| **Cycle Life**          | 300–500 cycles (typical)                       |
| **Protection Circuit**  | Optional (PCB for overcharge/discharge/cutoff)|

The 18650 is Li-ion battery is a high-capacity rechargeable cell widely used in electronics and robotics due to its stable voltage output, high energy density, and long cycle life.
can safely deliver continuous currents of 5–10 A and occasional peak currents up to 20 A,When paired with a protection circuit, it safeguards against overcharging, over-discharging, and short circuits, increasing safety and durability.
In this setup, we use 18650 batteries to power the Arduino Nano for controlling the ultrasonic sensors. Two 18650 cells are connected to a DC-DC step-up module to increase the voltage, which is then supplied to the Arduino, ensuring stable operation and consistent sensor readings.

**Microcontroller(Arduino nano)**

<div align="center">
<img width="800" height="800" alt="image" src="https://github.com/user-attachments/assets/0d45ec5e-d666-4185-be01-94dc062a9f37" />

**Specifications:**

| Specification            | Description |
|---------------------------|-------------|
| **Microcontroller**       | ATmega328P |
| **Operating Voltage**     | 5 V |
| **Input Voltage (recommended)** | 7–12 V |
| **Input Voltage (limit)** | 6–20 V |
| **Digital I/O Pins**      | 14 (6 PWM outputs) |
| **Analog Input Pins**     | 8 |
| **DC Current per I/O Pin** | 40 mA |
| **Flash Memory**          | 32 KB (2 KB used by bootloader) |
| **SRAM**                  | 2 KB |
| **EEPROM**                | 1 KB |
| **Clock Speed**           | 16 MHz |
| **USB Connection**        | Mini USB |
| **Dimensions**            | 45 mm x 18 mm |
| **Weight**                | ~7 g |


The Arduino Nano is a compact,microcontroller board based on the ATmega328P. Despite its small size, it offers full functionality with 14 digital I/O pins, 8 analog inputs, and a 16 MHz clock speed.
It operates at 5V and can be powered through a Mini USB connection, a regulated 5V pin, or an external 7–12V input, we used this embedded system for programming the ultrasonic sensor and after pass the information to ev3,We chose this microcontroller because it provides sufficient performance for our project requirements, and its compact size fits perfectly within the available space of our design.


**Medium motor EV3**

<div align="center">
<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/c0c91a6f-02e9-4b4f-8271-1a25b965384c" />

**Specifications**

| Specification              | Description |
|-----------------------------|-------------|
| **Model**                   | EV3 Medium Motor (45503) |
| **Type**                    | Servo Motor with integrated rotation sensor |
| **Operating Voltage**       | 9 V DC |
| **Nominal Power**           | 2.5 W |
| **No-load Speed**           | ~260 rpm |
| **Stall Torque**            | ~8 N·cm (0.08 N·m) |
| **Stall Current**           | ~0.7 A |
| **Tacho Sensor Resolution** | 1° (360 counts per rotation) |
| **Weight**                  | 75 g |
| **Cable Length**            | 25 cm |
| **Connector Type**          | EV3 Plug |
| **Control Features**        | Speed, position, and direction control |

It operates at 9V DC and is designed to provide a balance between speed and torque, making it suitable for medium-load
We connect these motors directly to the EV3, and control them directly with the programming block for these motors, which in our robot consumes the following:


EV3 Brick controls all motors. Powered by 10V 2050 mAh battery.  
- **Movement motors (2):** 150–250 mA  
- **Steering motor (1):** 120–250 mA

  
In terms of power consumption, the motor typically draws around 250–300 mA under normal load, but this can increase up to 1.2 A when operating under heavy load or stall conditions. Its power output reaches approximately 2.5 W, depending on the applied voltage and load.

**measures and details**

| **Feature** | **Value** |
|--------------|-----------|
| **Total length (with axle)** | 7.1 cm |
| **Body length** | 5.5 cm |
| **Width** | 3.8 cm |
| **Height** | 4.7 cm |
| **Axle diameter (LEGO cross axle)** | 4.8 mm |
| **Weight** | ≈ 75 g |
| **Connector type** | EV3 RJ12 (6-pin) |
| **Rotation sensor resolution** | 1° per step |
| **Rotation direction** | Bidirectional |
| **Position feedback** | Integrated rotation sensor |

<div align="center">
  <img width="326" height="96" alt="Medium Motor Voltage" src="https://github.com/user-attachments/assets/ea92cc7c-aa1b-4ce5-b05f-c80b4cd0d48a" />
  <p><em>Image 5.3: Medium Motor Voltage</em></p>
</div>

We found the information about the motor here:
[Hardware Developer Kit PDF](https://github.com/user-attachments/files/22328277/hardware_developer_kit.pdf)

## OpenMv H7 plus

<div align="center">
<img width="800" height="800" alt="image" src="https://github.com/user-attachments/assets/70af811b-02ed-4663-bd44-6418958fd6bd" />

## Specifications

| Feature              | Details                                                                 |
|----------------------|-------------------------------------------------------------------------|
| Processor            | ARM® Cortex®-M7, 32-bit, 480 MHz with Double Precision FPU             |
| RAM                  | 512 KB SRAM                                                              |
| Flash Memory         | 2 MB Flash                                                               |
| Image Sensor         | OV5640 (5 MP) or MT9M114 (1/3") with M12 lens mount                     |
| Resolution           | Up to 2592×1944 (OV5640) or 640×480 (MT9M114)                           |
| Frame Rate           | Up to 80 FPS (MT9M114), 75 FPS (OV5640)                                 |
| Image Formats        | Grayscale, RGB565, JPEG, BAYER, YUV422                                  |
| Connectivity         | Full-speed USB (12 Mbps), microSD card socket (up to 64 GB), SPI, I2C, CAN, UART |
| GPIO Pins            | 10 I/O pins (3.3V logic, 5V tolerant), supports PWM and interrupts      |
| Power Supply         | 5V via USB or VIN pin, 3.3V regulated output                             |
| Onboard LEDs         | RGB LED and two high-power 850nm IR LEDs                                  |
| Programming Language | MicroPython via OpenMV IDE                                               |
| Operating Voltage    | 5V DC                                                                    |
| Dimensions           | 40 mm × 40 mm × 15 mm                                                    |
| Weight               | Approximately 25 g                                                       |

The OpenMV H7 Pro is a low-power machine vision camera designed for embedded systems. It operates at 5V, drawing a typical current of 250–300 mA during normal operation, and up to 480 mA when all peripherals are active.
Key considerations for energy management:

**IR LEDs:** High current draw when enabled; use sparingly to extend battery life.

**MicroSD Logging:** Writing images or logs increases power usage slightly.

**Processing Load:** More complex algorithms (e.g., object recognition, color tracking) increase CPU activity and power draw.

**GPIO Outputs:** PWM and other peripherals also consume extra current.
  
Powered at 3.3V, max 480 mA, connected via custom PCB to EV3.

The camera is mounted at a 70° angle on the highest point of the vehicle. This position was selected to maximize the field of view, allowing the vehicle to better detect obstacles and monitor the track, covering a larger area and facilitating the identification of the designated parking zone. Initially, the camera was positioned at the front of the vehicle, above the steering system. However, it faced visibility issues, as the field of view was limited, which led to errors when avoiding the pillars. 

## 4x4 RGB LED Matrix

<div align="center">
<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/66861e06-8f1b-4c2e-b706-a11882cf633b" />


**Specifications**

| Specification               | Details                                                                 |
|------------------------------|------------------------------------------------------------------------|
| **Dimensions**               | 30 x 30 mm                                                              |
| **LED Configuration**        | 4 x 4 (16 RGB LEDs)                                                     |
| **LED Pitch**                | 3 mm                                                                    |
| **Operating Voltage**        | 5V DC                                                                    |
| **Current Consumption**      | 60–80 mA per LED at full brightness                                     |
| **Data Interface**           | Single-wire digital input (Data In)                                     |
| **Signal Protocol**          | WS2812B or compatible                                                   |
| **Power Input**              | VCC and GND                                                             |
| **LED Type**                 | Integrated RGB LEDs with built-in control                               |
| **Color Depth**              | 16.7 million colors (24-bit)                                            |
| **Control Method**           | PWM (Pulse Width Modulation)                                            |
| **Addressability**           | Individually addressable LEDs                                           |
| **Cascading Capability**     | Yes, via Data Out → Data In                                             |
| **Compatible Platforms**     | Arduino, ESP32, Raspberry Pi                                           |
| **Libraries**                | Adafruit NeoPixel, FastLED                                             |
| **Applications**             | DIY projects, wearable tech, prototyping                                 |

The 4x4 RGB LED matrix contains 16 individually addressable LEDs. Each LED operates at 5V DC and can draw approximately 60 mA at full brightness when displaying white (all three colors at maximum).

Typical current per LED: 60 mA (max)

Total current for 16 LEDs at full brightness: 16 × 60 mA = 960 mA

**P = V × I = 5V × 0.96A ≈ 4.8 Watts**

We use Neopixel LED to support the camera, as they help improve the distinction of colors in obstacles and the parking lot. The Neopixels are controlled using the NeoPixel library in Arduino, which then sends data to the EV3. This setup allows the EV3 to adjust the intensity of the Neopixels dynamically, enhancing the robot’s color detection and visual accuracy.

A 4x4 WS2812B matrix usually has 3 main pins:

VCC (Power)

Supplies 5V DC to the LEDs.

Connect to the 5V pin on Arduino or an external 5V power source.

GND (Ground)

Common ground for power and data.

Connect to Arduino GND and the negative terminal of the power supply.

DIN (Data In)

Receives the digital control signal from the Arduino.

Connect to a digital pin on Arduino (e.g., D6).

DOUT (Data Out) – optional for chaining

Allows connection to the Data In of another matrix for cascading multiple matrices.



---
## Obstacle managament
## Detection and Avoidance Strategies

**Metric:** X coordinate at blob base  

| Problem | Solution |
|---------|---------|
| Light variations | Fixed auto-gain, auto-white balance, exposure |
| Lost far pillars in curves | Extended dynamic ROIs, blob base compensation |
| Oversized blobs | X coordinate as main metric |
| Redundant OpenMV scripts | Unified via LPF2 protocol |
| Non-reactive line follower | Corridor width as proportional KP |
| Missed pillars → collision risk | Dedicated Black ROI |

### Line Tracking
Dynamic ROIs provide position error → proportional KP in EV3.

### Corridor Width Regulation
Proportional correction from lower ROIs.

### Obstacle Avoidance
Red → right, Green → left based on X coordinate vs target.

### Data Communication (OpenMV → EV3)
LPF2 protocol: unified data slots.

| Sensor / Source | Metric | Usage |
|-----------------|--------|-------|
| Low ROI | Line error | Main trajectory |
| Middle ROI | Corridor width, colors | Proportional regulation & obstacle anticipation |
| High ROI | Far obstacle position | Curve support |
| Black ROI | Dark area detection | Collision alert |
| Color blobs | X coordinate | Defines avoidance side |
| EV3 Motors | Speed, distance | Smooth control |
| EV3 Logic | KP | Dynamic correction |

---

## Calibration
Fixed camera parameters (auto-gain, auto-white balance, exposure). LAB thresholds adjusted for white, red, green, blue, orange.

---

## ROI Evolution
| Stage | Description |
|-------|------------|
| Initial | Central dynamic ROI anchored to white floor |
| Improvement | Trapezoidal ROIs for path and pillars |
| September | Three horizontal ROIs (low, middle, high) |
| Current | Four adaptive ROIs (Low, Middle, High, Black) covering full scene |

---

## References
- [WRO 2025 Future Engineers – General Rules PDF](https://wro-association.org/wp-content/uploads/WRO-2025-Future-Engineers-Self-Driving-Cars-General-Rules.pdf)
- [Manual Direction PDF](https://github.com/user-attachments/files/22270572/manual.direction.pdf)
- [Differential Manual PDF](https://github.com/user-attachments/files/22326888/Diferencial.manual.pdf)
- [Hardware Developer Kit PDF](https://github.com/user-attachments/files/22328277/hardware_developer_kit.pdf)

---

*End of README.md for Team Los Grises Superiores – WRO 2025 Future Engineers*

# 🤖 WRO-2025-Future-Engineers

Official repository of Team Los Grises Superiores for the **Future Engineers – World Robot Olympiad 2025**.  
<div align="center">
<img width="1000" height="500" alt="team-image" src="https://github.com/user-attachments/assets/b3e384a1-e19b-4c7f-addf-655aeb32bc3a" />
</div>

---

## 📸 Team photo
<div align="center">
  <img width="500" height="500" alt="team-photo" src="https://github.com/user-attachments/assets/8c940a8b-cdcd-43a6-ab31-e2c4029053f1" />
</div>

---

## 👥 Team Members

### Eduardo Alvarado Gonzalez
<div align="center">
<img width="200" height="200" alt="Eduardo Gonzalez" src="https://github.com/user-attachments/assets/20ccfb81-0bc1-4147-aa43-fefe649a55c0" />
</div>

**Role:** Coach and founder

An engineer and professor founded the **Los Grises Superiores** in 2014, since then with outstanding national and international participations.

---

### Eric Daniel Guerrero Uresti
**Age:** 22
<div align="center">
  <img width="200" height="200" alt="Eric Guerrero photo" src="https://github.com/user-attachments/assets/9e1509ca-ad50-48b9-ab44-2787fcce8e0e" />
</div>

**Role:** Programming & Mechanics

I started participating in robotics tournaments from 2016 to 2019, achieving **two second places** in the Mexican Robotics Tournament (TMR). Due to the **Covid-19 pandemic**, I couldn’t compete again until 2024, when I returned as a **coach** in TMR and WRO, earning a spot at the international competition. I am currently in my final year of **Mechatronics Engineering**.

---

### Paulina Ibarra Martínez
**Age:** 20
<div align="center">
  <img width="200" height="200" alt="Paulina Martinez photo" src="https://github.com/user-attachments/assets/86413c8a-610a-4270-a92d-cb3ed135d41b" />
</div>

**Role:** Programming & Electronics

I have been part of the **Robotics Club** at *Escuela Normal Superior “Profr. Moisés Sáenz Garza”* for three years, participating in **two Mexican Robotics Tournaments**, achieving **5th place** in the most recent one. Starting in 2024, I became a **junior coach**, achieving **third place** in WRO 2024 and **first place nationally** in the Mexican Robotics Tournament 2025.

---

## 📚 Contents
- [Project Overview](#project-overview)
- [Vehicle Photos](#vehicle-photos)
- [Components and Hardware](#components-and-hardware)
- [Mobility Management](#mobility-management)
  - [Chassis](#chassis)
  - [Steering System](#steering-system)
  - [Movement and Traction System](#movement-and-traction-system)
  - [Differential](#about-differential)
- [Power and Sense Management](#power-and-sense-management)
  - [Power Management](#power-management)
  - [Sense Management](#sense-management)
- [Obstacle Management](#obstacle-management)
  - [Vision System](#vision-system)
- [Calibration](#calibration)
- [ROI Evolution](#roi-evolution)
- [Detection and Avoidance Strategies](#detection-and-avoidance-strategies)
- [Manual Direction PDF](#manual-direction-pdf)
- [Differential Manual PDF](#differential-manual-pdf)
- [Hardware Developer Kit PDF](#hardware-developer-kit-pdf)
- [WRO 2025 Competition Info](#wro-2025-competition-info)

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

<div align="center">

| Front | Back |
|:--:|:--:|
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/7454f980-7fc9-454d-bd65-ce0c79626236" /> | <img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/df42b51e-19c5-4a8b-8104-9d87c46ed63f" /> |



| Bottom | Top |
|:--:|:--:|
| <img width="500" height="500" alt="Top" src="https://github.com/user-attachments/assets/6325fc24-d175-4126-9392-f010eebdde21" /> | <img width="500" height="500" alt="Bottom" src="https://github.com/user-attachments/assets/26f38601-a131-497d-996f-47b13516da12" /> |

| Left | Right |
|:--:|:--:|
| <img width="500" height="500" alt="Left" src="https://github.com/user-attachments/assets/e4613658-9c1e-4b2e-a67f-6475f9a949bf" /> | <img width="500" height="500" alt="Right" src="https://github.com/user-attachments/assets/f8a5ce6d-800d-4e4c-b585-920f9dbad793" /> |

</div>

---

## Components and Hardware

| Component | Description | Image | Purchase Link |
|-----------|-------------|-------|----------------|
| **45544 LEGO MINDSTORMS Education EV3 Core Set** | Forms the foundational structure and chassis. | <div align="center"><img width="500" height="300" alt="EV3 Core Set" src="https://github.com/user-attachments/assets/a725c977-b28b-4b5d-b95c-506c84cd6706" /></div> | [Buy here](https://bricks-store.com/esp/item/585/66/45544-set-base-lego-mindstorms-education-ev3) |
| **OpenMV Cam H7 Plus** | Smart camera for navigation and obstacle detection. | <div align="center"><img width="500" height="300" alt="OpenMV Cam H7 Plus" src="https://github.com/user-attachments/assets/2f1dc12c-a2f9-4e47-b665-d9b37091a8ce" /></div> | [Buy here](https://openmv.io/products/openmv-cam-h7-plus) |
| **HC-SR04 Ultrasonic Sensor** | Distance measurement sensor. | <div align="center"><img width="500" height="300" alt="HC-SR04" src="https://github.com/user-attachments/assets/f55c9c1f-b8f7-4d51-9b24-01f51de329b8" /></div> | [Buy here](https://uelectronics.com/producto/sensor-ultrasonico-hc-sr04/) |
| **DFRobot URM09 Ultrasonic Sensor (Gravity Analog)** | This ultrasonic sensor features an open dual-probe design and uses the standard Gravity PH2.0-3P vertical connector. Compatible with controllers operating at 3.3V or 5V logic levels. | <div align="center"><img width="500" height="300" alt="DFRobot Ultrasonic Sensor" src="https://github.com/user-attachments/assets/354617dc-9558-4abc-8309-5ecb129ce5dc" /></div> | [Buy here](https://wiki.dfrobot.com/URM09_Ultrasonic_Sensor_(Gravity_Analog)_SKU_SEN0307) |
| **Arduino Nano** | ATmega328-based microcontroller for control tasks. | <div align="center"><img width="500" height="300" alt="Arduino Nano" src="https://github.com/user-attachments/assets/22e8f59c-909d-4ff2-b637-dc03e15f4de6" /></div> | [Buy here](https://www.steren.com.mx/placa-de-desarrollo-nano.html) |
| **4x4 RGB LED Matrix** | Compact display module consisting of 16 individual LEDs arranged in a 4-row by 4-column grid. | <div align="center"><img width="500" height="300" alt="4x4 RGB Matrix" src="https://github.com/user-attachments/assets/1dfe866c-7431-4e3f-93b5-e756a8c59637" /></div> | [Buy here](https://mvelectronica.com/producto/matriz-de-led-rgb-4x4-ws2812-16bits-a-5v-led-5050) |
| **Mini 560 Step-Down Regulator** | Converts a higher voltage power source to a lower voltage efficiently. | <div align="center"><img width="500" height="300" alt="Mini 560" src="https://github.com/user-attachments/assets/51c8abdf-98bc-41fd-a258-7c256c0dce49" /></div> | [Buy here](https://uelectronics.com/producto/mini-560-regulador-step-down/?srsltid=AfmBOooF0lIfgnTp_5_7mmjziZz1XquqOzfXZdxR7m-WYIGU82qSsVjV) |
| **DFRobot Gravity BNO055** | Intelligent 9-axis Absolute Orientation Sensor integrating a triaxial accelerometer, gyroscope, geomagnetic sensor, and a 32-bit microcontroller. | <div align="center"><img width="500" height="300" alt="BNO055" src="https://github.com/user-attachments/assets/928267d5-ceeb-4d6f-aa20-6b1da1306c2b" /></div> | [Buy here](https://es.aliexpress.com/i/32950220044.html?gatewayAdapt=glo2esp) |
| **Digital Voltmeter** | Measures the electrical potential difference between two points in a circuit. Ideal for monitoring battery voltage and ensuring stable power supply. | <div align="center"><img width="500" height="300" alt="Voltmeter" src="https://github.com/user-attachments/assets/414b7cc2-f94e-4dab-97d9-6bc6ab0df812" /></div> | [Buy here](https://www.amazon.com.mx/Volt%C3%ADmetro-pulgadas-volt%C3%ADmetro-protecci%C3%B3n-amarillo/dp/B07P1RV5B1/ref=asc_df_B07P1RV5B1?mcid=6387c2ef254231499e8362066332bfa1&tag=gledskshopmx-20&linkCode=df0&hvadid=709873384261&hvpos=&hvnetw=g&hvrand=1934067081071435740&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1010132&hvtargid=pla-1676003973055&psc=1&language=es_MX&gad_source=1) |
## Mobility Management

### Chassis
The main chassis consists of LEGO pieces selected for their accessibility and for enabling a compact and efficient design. Initially, the prototype was designed using Studio 2.0 software to ensure proper part selection and structural balance.  
For the second level, an acrylic base (acrylate polymer) was used to support the ultrasonic sensors. The shape of this base was customized as part of the design by applying heat to specific areas to mold it into the desired form.  
This level integrates five ultrasonic sensors, strategically distributed to enhance environmental detection and obstacle avoidance.  
This design was made in OnShape:

<div align="center">
<img width="1000" height="1000" alt="Ultrasonic and PCB Base" src="https://github.com/user-attachments/assets/48febdb7-b3fb-46fc-b429-0648d3b4971d" />
</div>

The elaboration process:

Using a heat gun, each side of the acrylic base designated for the sensors was carefully heated. Once the material reached the appropriate temperature, it was bent using a mold to achieve the 90° angle required for the optimal positioning and field of view of the sensors.

<div align="center">
<img width="500" height="500" alt="Acrylic bending" src="https://github.com/user-attachments/assets/53dec651-0a3b-47fa-895d-e4c19290b290" />     
<img width="500" height="500" alt="Molded base" src="https://github.com/user-attachments/assets/6d716c07-a7b4-4b70-b3c2-c8264ffc2f77" />
</div>

The final result is mounted on the robot:

<div align="center">
<img width="500" height="500" alt="Mounted base" src="https://github.com/user-attachments/assets/7e76597a-44b9-4264-923c-65cb95d99f65" />
</div>

This base is attached to the chassis using four screws in the middle to give it stability, and on top of this locate the PCB is located where the ultrasonic sensors are connected.

The measurements for the sensor support can be found in the datasheet.

<div align="center">
<img width="500" height="500" alt="sensor support" src="https://github.com/user-attachments/assets/034fa407-525b-413a-86d8-a455544e789a" />
</div>

## DATASHEET:

https://github.com/EduardoAG33/WRO-2025-Future-Engineers/blob/main/Others/HC-SR04_Datasheet_with_Dimensions%20(1).pdf

**base 3**

On the PCB board, we mounted an additional acrylic base to secure the camera, and to place a voltmeter and a switch for the 18650 batteries. The gyroscope sensor is located in the central part of the assembly for optimal orientation measurement.

<div align="center">
<img width="500" height="500" alt="PCB acrylic base" src="https://github.com/user-attachments/assets/331af2ce-0cce-4646-9e9a-bf1a7cc7884d" />
</div>

**view in the vehicle**

<div align="center">
<img width="500" height="500" alt="view in the vehicle" src="https://github.com/user-attachments/assets/f7fd1152-2a27-4d11-a5e7-b53cf4603675" />
</div>

And for the upper level of the robot, we have the support for the camera and the Neo pixel light:  

<div align="center">
<img width="500" height="500" alt="camera support" src="https://github.com/user-attachments/assets/e680e149-5586-4c7b-b0e2-6f53eb4f0bf5" />
</div>

The support is positioned at a 70° inclination to ensure the vehicle remains within the maximum allowed height. This angle was carefully chosen to optimize the camera’s field of view, as detailed in the Power and Sense Management section.

**Changes and improvements**

Initially, the robot used two cameras. The first camera detected walls, while the second read floor lines for lap counting and identified pillar colors in the Obstacle Challenge. This setup aimed to avoid extra sensors due to the cameras’ high precision.

However, issues arose with ambient light sensitivity, calibration time, and battery consumption. To improve reliability, the second camera was replaced with five ultrasonic sensors positioned at frontal, 90°, and 45° angles to measure distances to walls.

The sensors communicate with the EV3 via two Arduino Nanos: one collects the data, and the other sends it via I2C. The system is mounted on a custom PCB.

**Before:**

<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/bee38687-32cb-4b21-940e-3429a2b44f74" />

**Now**

<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/ba843fe4-d056-42f5-ae9d-76be0deb70ee" />




## Base for the VL53L0X

**Solidworks software design**(metric system in mm)

<div align="center">
<img width="500" height="500" alt="VL53 base design" src="https://github.com/user-attachments/assets/0357aaa9-5b2b-4398-9a27-d1c3b4e0fc45" />
</div>

**draw measurements**

<div align="center">
<img width="500" height="500" alt="draw measurements" src="https://github.com/user-attachments/assets/122f09ca-8fc3-44a3-8a7b-1d3dcdb98ac1" />
</div>


This custom piece is designed to fit perfectly with LEGO components, allowing it to be mounted on the chassis and securely hold the sensor according to the dimensions specified in its datasheet.

The custom piece and sensor are precisely positioned to ensure optimal alignment and secure integration with the LEGO chassis, based on the sensor’s datasheet dimensions.

<div align="center">
<img width="500" height="500" alt="custom piece" src="https://github.com/user-attachments/assets/677f5e71-31a7-43c6-98f3-dc6273959970" />
</div>

## Problems and solutions
**Change of the sensor** 

we decided to change the previous sensor (VL53L0X) since when doing tests we had performance failures based on the walls since the distances varied a lot because the sensor laser is affected by the black color of the walls. We determined this by changing to a white color and seeing that the distances no longer varied with this, at the time of having the error this causing it to collide with the stops.
Solution:
The change was implemented for an ultrasonic DF robot URM09, it is working better, the objective changed it was no longer necessary to use it for parking, but as an aid to the turn sensor at the end of the laps of the open challenge round in case the vehicle finished outside the section, this ultrasonic would mark the distance (or the one in front depending on the height at which the robot finishes) to join the final arrival area.
To place the sensor, it only fits on the base of the previous one.
<div align="center">
<img width="500" height="500" alt="image" src="https://github.com/user-attachments/assets/f3dd86f4-b4bb-4bd1-bec3-f6b2386d7e40" />

---

**Chassis render**
<div align="center">
<img width="500" height="500" alt="chassis render" src="https://github.com/user-attachments/assets/5a8c0801-5dba-4137-ac2b-e9e2eaf370f1" />
</div>

**Assembly manual:**
[chassis assambly instruction.pdf](https://github.com/user-attachments/files/22890187/chassis.assambly.instruction.pdf)

**material that makes up the structure of the chassis:**
<div align="center">
<img width="500" height="500" alt="material 1" src="https://github.com/user-attachments/assets/6be42468-d342-4a3f-bf52-336521bc3e64" />
</div>

<div align="center">
<img width="500" height="500" alt="material 2" src="https://github.com/user-attachments/assets/3d160bbb-81db-4c22-88aa-1f6bce73b8f8" />
</div>

<div align="center">
<img width="500" height="500" alt="material 3" src="https://github.com/user-attachments/assets/d0c6ef1d-8a5d-4c55-8a12-6d94522b6061" />
</div>

In the Mexican National Tournament, we only used one differential, and the robot dimensions were both wider and taller. For the updated version, we decided to implement two differentials, as this configuration provides significantly better control when moving forward. Additionally, reducing the robot’s overall dimensions helps prevent collisions with obstacles and makes it easier to maneuver around them.

---

### Steering System
The EV3’s middle motor converts rotational motion into steering movement through a gear train mechanism. The wheels are linked by a connecting rod, allowing them to move freely. With the assistance of the front differential, this setup transmits motion through the drivetrain to the rear motors, enabling smooth and controlled movement.

The steering rotation is limited to 45 degrees due to the chassis design; however, this range is sufficient for proper turning and obstacle avoidance. If needed, the rotation angle can be further reduced through the block programming.  
**Functionality:**

- **Pinion (engranaje circular):** The circular gear located at the center of the structure. When it rotates, it moves the rack from side to side.  
- **Rack (toothed bar):** A long bar with teeth that meshes with the pinion. When the pinion turns, the rack slides horizontally.  
- **Wheel connection:** The ends of the rack are linked to the wheels through steering arms. When the rack moves, it pushes or pulls these arms, causing the wheels to turn.

<div align="center">
  <img width="700" height="700" alt="steering system" src="https://github.com/user-attachments/assets/6fa1eabc-dd34-4a60-99e5-533a9b5d4c33" />
  <p><em>Steering system render</em></p>
</div>

**material that makes up the structure of the steering:**
<div align="center">
 <img width="500" height="500" alt="steering material" src="https://github.com/user-attachments/assets/5f12ed7e-0da7-49d1-aecc-cf8525e78320" />
</div>
  
**Assembly manual**
[Sterring system manual.pdf](https://github.com/user-attachments/files/22892572/Sterring.system.manual.pdf)

---

### Movement and Traction System
Two medium motors with differential system transmit energy to wheels. Transmission: 20-tooth → 12-tooth gears → 28-tooth → 20-tooth driving wheels. Position accuracy ±1°, torque 0.08 Nm, speed 240 RPM.  
According to the competition rules, the engines cannot be mounted directly on the wheels. Therefore, we chose to implement a transmission system connected to the differential, allowing the engine’s motion to be transferred to the tires, causing them to rotate.  
We decided to use two motors because they offer greater speed, power, and stability to the vehicle’s base compared to using only one. This configuration allows for a more balanced distribution of torque, improving traction and control during movement. After testing different options, we chose the medium LEGO motor because it provides an optimal balance between size, weight, and energy efficiency, making it ideal for our chassis design. Additionally, its compact structure facilitates integration into the transmission system while maintaining low power consumption and reliable performance.

<div align="center">
<img width="500" height="500" alt="traction system" src="https://github.com/user-attachments/assets/5b2d5fdf-bf02-4cb2-97f9-ac3fb9f56719" />
</div>

**Traction system render**

<div align="center">
 <img width="500" height="500" alt="traction render" src="https://github.com/user-attachments/assets/de4066aa-9ef0-4369-a0e5-4047937f75a1" />
</div>

**Traction system manual**
[traction system manual.pdf](https://github.com/user-attachments/files/22892680/traction.system.manual.pdf)

---

### About Differential
Distributes torque to wheels, enabling smooth cornering. Input via pinion and crown gears. Outer wheel rotates faster in turns, inner wheel slower, straight motion equal.

A differential is a mechanical component that allows wheels on the same axle to rotate at different speeds while transmitting power from the motor. This is especially important when a vehicle turns, as the outer wheel needs to travel a greater distance than the inner wheel. The differential distributes torque between the wheels, ensuring smooth and efficient movement, reducing tire wear, and improving traction and stability. In our design, the differential receives motion from the transmission and transfers it to the tires, enabling precise control of the vehicle’s movement.

<div align="center">
  <img width="500" height="500" alt="Differential example" src="https://github.com/user-attachments/assets/841f8551-b8cd-43e2-a964-24c97eb4f7ce" />
  <p><em>Image: Differential example</em></p>
</div>

**LEGO Differential Calculations – Gear Ratio Table**

| Gear Ratio (i) | Wheel Speed (m/s) | Wheel Torque (N·m) | Traction Force (N) |
|----------------|-------------------|--------------------|--------------------|
| 1:1            | 0.50              | 0.20               | 7.14               |
| 2:1            | 0.25              | 0.40               | 14.3               |
| 3:1            | 0.17              | 0.60               | 21.4               |
| 4:1            | 0.13              | 0.80               | 28.6               |
| 5:1            | 0.10              | 1.00               | 35.7               |

- Assumes **motor speed = 170 rpm**, **torque = 0.2 N·m**, **wheel radius = 0.028 m**.

## Impact of vehicle dimensions

The robot’s compact dimensions — 15 cm wide, 29 cm long, and 26 cm high — allow for the precise integration of both the steering and traction systems, enabling accurate and stable turns.
It was designed to be as narrow as possible, minimizing the risk of collisions with walls during sharp turns.

In the Open Challenge, our robot uses five ultrasonic sensors together with an OpenMV camera, creating an intelligent system that allows it to detect obstacles and move safely.
The front ultrasonic sensor detects when a curve begins. The camera and ultrasonic sensors work together through a PID control system, and we also correct measurement errors from the ultrasonic sensors using gain adjustments depending on their inclination.
This helps the robot identify whether a corridor is open or closed, effectively avoiding collisions with walls and improving navigation accuracy.

For the Obstacle Challenge, we took advantage of the robot’s width, length, and height to optimize its performance in different scenarios.
The width, being narrow, allows the vehicle to pass easily between pillars without collisions.
The length was optimized for the parking task — we extended the vehicle and added a rear spoiler to make the most of the rule that define the parking area as 1.5 times the vehicle’s length. This provides more freedom and precision when parking.
The height was designed to ensure better visibility of obstacles, allowing the sensors and camera to detect objects from their base to their top. This also prevents the robot from re-detecting the same obstacle after an evasive maneuver or a sharp turn, ensuring smoother navigation and preventing unnecessary repeated avoidance actions.

---

## Power and Sense Management
The Power and Sensor Management system of the vehicle is engineered to optimize energy distribution and ensure reliable operation of all electronic components. It carefully regulates the power supply to motors and sensors, maintaining stability and efficiency under varying load conditions. This system enables precise control over sensor readings and motor performance, supporting accurate navigation, obstacle detection, and overall vehicle functionality.
   
### Battery for EV3:
<div align="center">
<img width="500" height="500" alt="EV3 Battery" src="https://github.com/user-attachments/assets/baf83fc5-b1e4-444e-b0d3-33d77a03abcb" />
</div>

**Specifications:**

| Specification       | Details |
|--------------------|--------|
| **Battery Type**       | Rechargeable Lithium-Ion (Li-Ion) |
| **Nominal Voltage**     | 7.4 V (Li-Ion) |
| **Capacity**            | 2000 mAh (Li-Ion) |
| **Typical Usage Time**  | Approximately 1–2 hours with intensive use of motors and sensors |
| **Charging Time**       | 1.5 – 2 hours (Li-Ion) |
| **Weight**              | 160 g (Li-Ion) |
| **Connector**           | Integrated in EV3 Brick |
| **Note**                | Using the official rechargeable Li-Ion battery is recommended for optimal performance and to avoid voltage variation from AA batteries |

This battery is the recommended power source for the LEGO EV3. There are two options: the official rechargeable battery or six AA batteries. Using the official battery is preferable, as it provides a stable and consistent voltage, ensuring reliable operation of motors and sensors under varying loads. Additionally, it offers longer runtime, making it ideal for extended use and competitive.

### Battery 18650
<div align="center">
<img width="500" height="500" alt="18650 battery" src="https://github.com/user-attachments/assets/343775dc-0e65-4a3e-8732-99fa9c5848e2" />
</div>

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
In this setup, we use 18650 batteries to power the Arduino Nano for controlling the ultrasonic sensors. Two 18650 cells are connected to a DC-DC step-up module to increase the voltage, which is then supplied to the Arduino, ensuring stable operation and consistent sensor readings, we We use two 18650 batteries connected in series, providing an output voltage of approximately 7V.




### Microcontroller(Arduino nano)
<div align="center">
<img width="500" height="500" alt="Arduino Nano large" src="https://github.com/user-attachments/assets/0d45ec5e-d666-4185-be01-94dc062a9f37" />
</div>

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
It operates at 5V and can be powered through a Mini USB connection, a regulated 5V pin, or an external 7–12V input,

### Medium motor EV3
<div align="center">
<img width="500" height="500" alt="EV3 Medium Motor" src="https://github.com/user-attachments/assets/c0c91a6f-02e9-4b4f-8271-1a25b965384c" />
</div>

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
  <img width="500" height="500" alt="Medium Motor Voltage" src="https://github.com/user-attachments/assets/ea92cc7c-aa1b-4ce5-b05f-c80b4cd0d48a" />
  <p><em>Image: Medium Motor Voltage</em></p>
</div>

We found the information about the motor here:
[Hardware Developer Kit PDF](https://github.com/user-attachments/files/22328277/hardware_developer_kit.pdf)

## OpenMv H7 plus
<div align="center">
<img width="500" height="300" alt="OpenMV H7" src="https://github.com/user-attachments/assets/70af811b-02ed-4663-bd44-6418958fd6bd" />
</div

**PCB Design**
<div align="center">
<img width="605" height="513" alt="image" src="https://github.com/user-attachments/assets/7cf83de3-7098-41f8-abd3-0c67ef3e76e9" />
</div

**PCB Schematic**
<div align="center">
<img width="557" height="610" alt="image" src="https://github.com/user-attachments/assets/d05fcec9-58d9-4e48-892a-33a44d8ab74b" />
</div


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
<img width="500" height="500" alt="4x4 RGB Matrix large" src="https://github.com/user-attachments/assets/66861e06-8f1b-4c2e-b706-a11882cf633b" />
</div>


**Specifications**

| Specification               | Details                                                                 |
|------------------------------|-------------------------------------------------------------------------|
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

The 4x4 RGB LED matrix contains 16 individually addressable LEDs. Each LED operates at 5V DC and can draw approximately 60 mA at full brightness when displaying white (all three colors at maximum).

Typical current per LED: 60 mA (max)

Total current for 16 LEDs at full brightness: 16 × 60 mA = 960 mA

**P = V × I = 5V × 0.96A ≈ 4.8 Watts**

We use Neopixel LED to support the camera, as they help improve the distinction of colors in obstacles and the parking lot. The Neopixels are controlled using the NeoPixel library in Arduino, which then sends data to the EV3. This setup allows the EV3 to adjust the intensity of the Neopixels dynamically, enhancing the robot’s color detection and visual accuracy.

A 4x4 WS2812B matrix usually has 3 main pins:

- VCC (Power)
- GND (Ground)
- DIN (Data In)
- DOUT (Data Out) – optional for chaining

## Mini 560 Regulador Step down 

<div align="center">
<img width="500" height="500" alt="Mini 560 module" src="https://github.com/user-attachments/assets/7566dcf4-fe6a-4349-af80-0a458462fb7a" />
</div>

**Specifications**

| Specification | Description |
|----------------|-------------|
| **Model** | Mini 560 DC-DC Step-Down Converter |
| **Input Voltage (Vin)** | 4.5V – 28V DC |
| **Output Voltage (Vout)** | Adjustable from 0.8V – 20V DC |
| **Default Output (pre-set)** | 5V (depending on module version) |
| **Output Current (Iout)** | Up to 3A (recommended continuous current: 2A for stability) |
| **Efficiency** | Up to 95% (depending on voltage and load) |
| **Switching Frequency** | 1.5 MHz |
| **Voltage Ripple** | < 30 mV (typical) |
| **Load Regulation** | ±0.5% |
| **Conversion Type** | Step-Down (Buck) Converter |
| **Control IC** | MP2307 or similar synchronous rectifier chip |
| **Operating Temperature** | -40°C to +85°C |
| **Dimensions** | 22 mm x 17 mm x 4 mm |
| **Protection Features** | Short-circuit, over-temperature, and over-current protection |
| **Typical Applications** | Power supply for microcontrollers, sensors, cameras, LED strips, and communication modules |

The Mini 560 Step-Down Regulator is used to efficiently convert higher input voltages to lower, stable output voltages suitable for powering microcontrollers, sensors, and other electronic modules in the robot. Its compact design and high efficiency make it ideal for embedded and portable applications.

We use this module to regulate the voltage supplied to the two Arduino PCBs, stepping it down from 7V to 5V to ensure stable operation and optimal performance.

## RM09 Ultrasonic Distance Sensor

<img width="736" height="552" alt="image" src="https://github.com/user-attachments/assets/0776f173-76e5-4585-9830-a7792d0bcac7" />



## Specifications

| Parameter                  | Value                                      |
|-----------------------------|--------------------------------------------|
| **Supply Voltage**          | 3.3V to 5.5V DC                            |
| **Operating Current**       | 20 mA                                      |
| **Operating Temperature**   | -10°C to +70°C                             |
| **Measurement Range**       | 2 cm to 500 cm                              |
| **Resolution**              | 1 cm                                       |
| **Accuracy**                | ±1%                                        |
| **Acoustic Frequency**      | 40 ± 2 kHz                                 |
| **Ranging Frequency**       | Up to 25 Hz                                |
| **Dimensions**              | 47 mm × 22 mm (1.85" × 0.87")             |
| **Output Type**             | Analog voltage output                      |
| **Beam Angle**              | ±15°                                       |
| **Distance Formula**        | `Distance = Vout (mV) × 520 / Vin (mV)`   |

## Description

The RM09 Ultrasonic Distance Sensor (Gravity URM09) is a high-precision sensor designed for distance measurement applications. It operates by emitting ultrasonic waves and measuring the time it takes for the echo to return, providing accurate distance readings from 2 cm up to 500 cm. With a resolution of 1 cm and an accuracy of ±1%, it is suitable for robotics, automation, and obstacle detection projects.  

The sensor features analog voltage output, built-in temperature compensation, and fast ranging up to 25 measurements per second. Its compact design and wide voltage compatibility (3.3V to 5.5V).

We use this sensor to assist with turns. At the end of the three-turn sequence, the robot may exit the section. To address this, the sensor is implemented to measure the distance to the wall and guide the robot forward, ensuring accurate entry into the next section.

---

## DF Robot Gravity BNO055

<div align="center">
<img width="500" height="500" alt="BNO055 module" src="https://github.com/user-attachments/assets/f03d9b6b-f96a-4cee-b5f8-e8e562f1766e" />
</div>

| Specification | Description |
|----------------|-------------|
| **Model** | DFRobot Gravity BNO055 |
| **Sensor Type** | 9-Axis Absolute Orientation Sensor |
| **Integrated Sensors** | 3-axis accelerometer, 3-axis gyroscope, 3-axis magnetometer |
| **Operating Voltage (Vcc)** | 3.3V – 5V DC |
| **Communication Interface** | I²C (default) or UART |
| **I²C Address** | 0x28 (default) / 0x29 (configurable) |
| **Measurement Range (Accelerometer)** | ±2g / ±4g / ±8g / ±16g |
| **Measurement Range (Gyroscope)** | ±125°/s / ±250°/s / ±500°/s / ±1000°/s / ±2000°/s |
| **Magnetometer Range** | ±1300 µT (X, Y), ±2500 µT (Z) |
| **Absolute Orientation Output** | Quaternion, Euler angles, linear acceleration, gravity vector |
| **Output Data Format** | 16-bit data through I²C or UART |
| **Operating Temperature** | -40°C to +85°C |
| **Power Consumption** | ~12 mA (typical) |
| **Dimensions** | 30 mm × 22 mm × 7 mm |
| **Mounting Type** | Gravity compatible (3-pin interface) |
| **Applications** | Robotics, motion tracking, navigation, stabilization, and orientation detection |

---

### Description

The **DFRobot Gravity BNO055** is an intelligent 9-axis absolute orientation sensor that combines an accelerometer, gyroscope, and magnetometer with an onboard 32-bit microcontroller running Bosch sensor fusion algorithms.  
This integration allows the module to directly output orientation data (Euler angles or quaternions) without requiring complex calculations from the main microcontroller.

In our robot, this sensor is used to determine the **precise orientation and tilt** of the vehicle, improving stability and movement control during navigation tasks.

---

### Pinout and Function

| Pin | Name | Description |
|------|------|-------------|
| **VCC** | Power Input | Connect to 3.3V–5V DC power supply |
| **GND** | Ground | Common ground with the microcontroller |
| **SDA** | I²C Data | Data line for I²C communication |
| **SCL** | I²C Clock | Clock line for I²C communication |
| **RX / TX** | UART Communication | Optional serial communication interface |
| **RST** | Reset | Used to reset the sensor (optional) |

We use this sensor to count laps on the track, processing the data with the Arduino to send the information to the Ev3 and then with a programming block we decide the count of the laps based on its initial position where it will also end in the same place

**PCB**
During the PCB design process, we engraved the circuit using a laser machine. Afterward, we applied ferric chloride to etch away the excess copper, leaving only the designed traces. The board was then drilled, cleaned, and prepared for soldering and component assembly.

The PCBs designed for the ultrasonic sensors and camera are fully fabricated, cleaned, and ready for component mounting and final assembly.

<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/32ba56aa-95e7-4949-b6ce-f05d55db3b8c" />

**arduinos for the ultrasonic sensors design**

<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/8aa4a668-4f34-4dfe-ba09-587816f9b7b8" />

**ultrasonic connections**

<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/1251a371-980c-4cdc-afbc-804a4050db7c" />


This PCB is powered by two 18650 lithium batteries connected in series, providing a total supply voltage of approximately 8V. A voltage regulator steps down the voltage to 5V to reliably power the ultrasonic sensors and the NeoPixel LED module.

The system architecture includes two Arduino microcontrollers:

Arduino 1 handles the acquisition and processing of data from the ultrasonic sensors.

Arduino 2 manages data communication and transmits processed information to the LEGO EV3 brick via the I2C communication protocol.

This configuration enables seamless integration with the EV3 environment, allowing real-time data exchange and programming through EV3 graphical blocks.

**Arduino Code ultrasonic program**

<img width="513" height="875" alt="image" src="https://github.com/user-attachments/assets/ae30f8e3-6049-48ef-a321-f5ad86f52243" /> <img width="502" height="823" alt="image" src="https://github.com/user-attachments/assets/daba766a-c335-4639-b2ee-4213f9ee6e2d" />
<img width="662" height="862" alt="image" src="https://github.com/user-attachments/assets/86cf583d-b98d-42d5-9335-5e1cd355cfbd" /> <img width="536" height="836" alt="image" src="https://github.com/user-attachments/assets/810ae681-78ef-458c-b71c-ddbc244fcdb0" />
<img width="620" height="860" alt="image" src="https://github.com/user-attachments/assets/dd5aa331-13fe-4061-888c-75a2396dc782" />
## explication

### Libraries
- **`Wire.h`**: Handles I2C communication with the BNO055 sensor.  
- **`SoftwareSerial.h`**: Provides an extra serial port for communication with a master device.  
- **`NewPing.h`**: Efficient library for reading HC-SR04 ultrasonic sensors with filtering and timing control.  



### Ultrasonic Sensors
- Four `NewPing` objects are created for the sensors: `l90`, `l45`, `r45`, `r90`.  
- Maximum measurement distance is **200 cm**.  



### Lap Detection
- **`LAPS_METHOD = 3`**: Combines accumulated yaw and gate crossing for reliable lap counting.  
- **`LAP_TICKS16`**: 360° × 16 ticks per full rotation.  
- **`LAP_MIN_MS`**: Minimum time (ms) between lap counts to prevent false detections.  
- **`GATE_HALF_WIDTH`** + **`GATE_HYST`**: Gate angle thresholds for lap detection.  



### UART Communication
- Uses `SoftwareSerial` on **D2 (RX) / D3 (TX)** to send CSV-formatted sensor data to a master device.  


### BNO055 Sensor
- Custom minimal I2C implementation without external libraries.  
- Provides **yaw angle (heading)** in 16 ticks.  
- Initializes in **NDOF mode** and ensures valid heading data before operation.  


### Angle Utilities
- **`yawDelta16()`**: Calculates the difference between two yaw readings, accounting for ±360° wraparound.  
- **`angDiffDeg()`**: Calculates angular difference normalized to -180° … 180°.  



### State Variables
- Store previous yaw (`yaw_prev16`), accumulated yaw (`yaw_accum16`), lap count (`lap_count`), gate state, and BNO055 initialization status (`bno_ok`).  


### Lap Calculation Functions
- **`timeOk()`**: Ensures laps are not counted too quickly.  
- **`tryCountLapAccumYaw()`**: Counts laps based on accumulated yaw rotation.  
- **`tryCountLapGate()`**: Counts laps when crossing a gate angle threshold.  
- **`resolveLapMethod3()`**: Combines both methods for a reliable lap count.  



### Ultrasonic Filter
- **`filteredPing()`**: Applies a median + average filter on multiple readings to remove outliers and improve measurement stability.  

### Setup
- Initializes **Serial**, **SoftwareSerial**, and **I2C** communication.  
- Initializes **BNO055 sensor**.  
- Sends CSV header:  


## 🧠 Arduino Nano – Ultrasonic + IMU Sensor Fusion System

### Overview
This program is designed for an **Arduino Nano (ATmega328P)** that integrates **four HC-SR04 ultrasonic sensors** and a **BNO055 IMU**.  
The system measures distances, detects orientation, and counts laps, transmitting the processed data in **CSV format** via **UART** to a LEGO EV3 or another master controller.

---

### ⚙️ Features
- **Four ultrasonic sensors** (left/right at 45° and 90°) for wall and obstacle detection.  
- **BNO055 IMU** (communicated via I2C, no Adafruit libraries) for orientation tracking.  
- **Lap counting system** based on full rotations and angular gate detection.  
- **Median + range filter** for noise reduction in ultrasonic readings.  
- **UART serial communication** at 115200 baud, sending real-time data in CSV format:


**2 Arduino code for communication**

<img width="547" height="878" alt="image" src="https://github.com/user-attachments/assets/165ae61a-07fb-4665-89bd-e707babb8823" /> <img width="627" height="876" alt="image" src="https://github.com/user-attachments/assets/d3209595-8380-4189-9c9a-1a64bbec2a34" />


## Arduino Slave with NeoPixel & HC-SR04 Sensors – I2C Communication

This code runs on an Arduino acting as an **I2C slave** that collects sensor data, maps it, and sends it to a master device. It also controls a NeoPixel matrix for lighting feedback.



### Libraries
- **`Wire.h`**: Handles I2C communication as a slave device.  
- **`SoftwareSerial.h`**: Creates a secondary serial port to read CSV data from another Nano.  
- **`Adafruit_NeoPixel.h`**: Controls a 16-LED NeoPixel matrix.  
- **`NewPing.h`**: Manages ultrasonic HC-SR04 sensors efficiently.



### Sensors
- Front ultrasonic sensor (`frontU`) reads distance in cm.  
- Rear analog sensors connected to `A6` and `A7` are scaled to 0–500 units.  
- Additional distance sensors (`l45`, `r45`, `l90`, `r90`) and lap counter are read via a secondary Nano through SoftwareSerial.  


### Data Mapping
- Distance readings are mapped to **-100…100**.  
- Analog readings are mapped to **-127…127**.  
- `frontbyte`, `l45byte`, `r45byte`, `l90byte`, `r90byte`, `A6byte`, `A7byte` store the mapped values.



### NeoPixel Control
- Initializes a 16-LED matrix on pin 9.  
- Brightness is mapped using `POT_LUZ` from 0–100 to 0–255.  
- Shows initial static color on setup.



### I2C Communication
- Arduino acts as **slave with address 0x04**.  
- `sendData()` sends a requested byte depending on `mind_n_DATO_1`.  
- `onreceiveEvent()` reads commands from the master device.  
- Case 6 uses a **flag (`linkSent`)** to send a single pulse only once.  


### CSV Processing
- Receives lines from the secondary Nano via `SoftwareSerial`.  
- Each CSV line contains 5 values: `l90, l45, r45, r90, laps`.  
- `processLine()` parses the string and updates sensor variables.


### Loop Behavior
1. Reads front ultrasonic sensor and analog values.  
2. Reads CSV from the secondary Nano and parses it.  
3. Maps all sensor values to the specified ranges.  
4. Updates internal state for I2C requests.  

---

This setup allows **real-time sensor fusion**, mapping, and I2C data delivery to a master controller while providing visual feedback through the NeoPixel matrix.

**I2c Communication block to EV3**

<div align="center">
<img width="907" height="402" alt="image" src="https://github.com/user-attachments/assets/3cfa9a2d-41c9-4320-b84d-307c6e09d9fb" />

**Reference for connect the ev3 to Arduino**

https://www.dexterindustries.com/howto/connecting-ev3-arduino/

div align="center">
<img width="1356" height="427" alt="image" src="https://github.com/user-attachments/assets/e29b92d7-da73-4420-a06c-7068e7d26ca5" />

We use ultrasonic sensors connected via I²C to measure distances, and the robot turns using EV3 blocks.






---

## Obstacle management
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

## 💰 Material Cost Report 

| # | Component | Quantity | Unit Price (USD) | Total (USD) | Purchase Link |
|---|------------|-----------|------------------|--------------|----------------|
| 1 | *45544 LEGO MINDSTORMS Education EV3 Core Set* | 1 | 470.00 | *470.00* | [Buy here](https://bricks-store.com/esp/item/585/66/45544-set-base-lego-mindstorms-education-ev3) |
| 2 | *OpenMV Cam H7 Plus* | 1 | 75.00 | *75.00* | [Buy here](https://openmv.io/products/openmv-cam-h7-plus) |
| 3 | *HC-SR04 Ultrasonic Sensor* | 5 | 3.00 | *15.00* | [Buy here](https://uelectronics.com/producto/sensor-ultrasonico-hc-sr04/) |
| 4 | *DFRobot URM09 Ultrasonic Sensor (Gravity Analog)* | 1 | 12.00 | *12.00* | [Buy here](https://wiki.dfrobot.com/URM09_Ultrasonic_Sensor_(Gravity_Analog)_SKU_SEN0307) |
| 5 | *Arduino Nano* | 2 | 8.00 | *16.00* | [Buy here](https://www.steren.com.mx/placa-de-desarrollo-nano.html) |
| 6 | *4x4 RGB LED Matrix (WS2812)* | 1 | 5.00 | *5.00* | [Buy here](https://mvelectronica.com/producto/matriz-de-led-rgb-4x4-ws2812-16bits-a-5v-led-5050) |
| 7 | *Mini 560 Step-Down Regulator* | 1 | 4.00 | *4.00* | [Buy here](https://uelectronics.com/producto/mini-560-regulador-step-down/) |
| 8 | *DFRobot Gravity BNO055* | 1 | 30.00 | *30.00* | [Buy here](https://es.aliexpress.com/i/32950220044.html) |
| 9 | *Digital Voltmeter* | 1 | 3.00 | *3.00* | [Buy here](https://www.amazon.com.mx/Volt%C3%ADmetro-pulgadas-volt%C3%ADmetro-protecci%C3%B3n-amarillo/dp/B07P1RV5B1/) |
|   | *💵 Total Estimated Cost* |   |   | *650.00 USD* |   |

---





**LEGO SET use**
| BLItemNo | PartName | Qty | Price per Piece (USD) | Total Price (USD) |
|----------|-----------|-----|-----------------------|-------------------|
| 2780 | Technic, Pin with Short Friction Ridges | 17 | 0.08 | 1.36 |
| 2905 | Technic, Liftarm, Modified Triangle Thin 3 x 5 with Full Supports | 2 | 0.05 | 0.10 |
| 32034 | Technic, Axle and Pin Connector Angled #2 - 180 degrees | 1 | 0.50 | 0.50 |
| 32062 | Technic, Axle 2L Notched | 16 | 0.01 | 0.16 |
| 32073 | Technic, Axle 5L | 6 | 0.75 | 4.50 |
| 4265c | Technic Bush 1/2 Smooth | 1 | 0.08 | 0.08 |
| 32184 | Technic, Axle and Pin Connector Perpendicular 3L with Center Pin Hole | 1 | 3.50 | 3.50 |
| 32269 | Technic, Gear 20 Tooth Double Bevel | 7 | 0.15 | 1.05 |
| 32278 | Technic, Liftarm Thick 1 x 15 | 4 | 2.59 | 10.36 |
| 32316 | Technic, Liftarm Thick 1 x 5 | 1 | 1.21 | 1.21 |
| 32523 | Technic, Liftarm Thick 1 x 3 | 2 | 0.70 | 1.40 |
| 32524 | Technic, Liftarm Thick 1 x 7 | 5 | 1.74 | 8.70 |
| 32526 | Technic, Liftarm, Modified Bent Thick L-Shape 3 x 5 | 5 | 1.77 | 8.85 |
| 3713 | Technic Bush | 4 | 0.14 | 0.56 |
| 39367pb01 | Wheel 56 x 14 Technic with Axle Hole and 8 Pin Holes with Molded Medium Azure Hard Rubber Tire Pattern | 4 | 3.00 | 12.00 |
| 40490 | Technic, Liftarm Thick 1 x 9 | 1 | 2.59 | 2.59 |
| 4274 | Technic, Pin 1/2 without Friction Ridges | 8 | 0.10 | 0.80 |
| 4519 | Technic, Axle 3L | 6 | 0.43 | 2.58 |
| 46372 | Technic, Gear 28 Tooth Double Bevel | 1 | 0.50 | 0.50 |
| 48989 | Technic, Pin Connector Perpendicular 3L with 4 Pins | 7 | 1.22 | 8.54 |
| 55013 | Technic, Axle 8L with Stop | 2 | 1.18 | 2.36 |
| 55615 | Technic, Pin Connector Perpendicular 3 x 3 Bent with 4 Pins | 2 | 1.90 | 3.80 |
| 6538c | Technic, Axle Connector 2L (Smooth with x Hole + Orientation) | 5 | 0.40 | 2.00 |
| 62520c01 | Technic, Universal Joint 3L | 2 | 0.54 | 1.08 |
| 62821a | Technic, Gear Differential 28 Tooth Bevel - Inner Tabs with Open Center | 2 | 2.85 | 5.70 |
| 64179 | Technic, Liftarm, Modified Frame Thick 5 x 7 Open Center | 2 | 5.30 | 10.60 |
| 64781 | Technic, Gear Rack 1 x 13 with Axle and Pin Holes | 1 | 3.13 | 3.13 |
| 6558 | Technic, Pin 3L with Friction Ridges | 14 | 0.31 | 4.34 |
| 6589 | Technic, Gear 12 Tooth Bevel | 6 | 0.29 | 1.74 |
| 71710 | Technic, Liftarm, Modified Perpendicular Holes Thick 1 x 15 | 2 | 1.00 | 2.00 |
| 73507 | Technic, Liftarm, Modified Perpendicular Holes Thick 1 x 11 | 2 | 1.00 | 2.00 |
| 87083 | Technic, Axle 4L with Stop | 1 | 0.59 | 0.59 |
| 94925 | Technic, Gear 16 Tooth - Axle Hole with Closed Sides | 4 | 0.70 | 2.80 |
| 99455 | Electric, Motor EV3, Medium | 3 | 35.00 | 105.00 |
| 99773 | Technic, Liftarm, Modified Triangle Thin 3 x 5 with Short Supports | 6 | 1.20 | 7.20 |
| **95646** | **LEGO MINDSTORMS EV3 Intelligent Brick** | 1 | 245.00 | 245.00 |
| **—** | **TOTAL GENERAL** | **—** | **—** | **488.92 USD** |






## References
- [WRO 2025 Future Engineers – General Rules PDF](https://wro-association.org/wp-content/uploads/WRO-2025-Future-Engineers-Self-Driving-Cars-General-Rules.pdf)
- [Hardware Developer Kit PDF](https://github.com/user-attachments/files/22328277/hardware_developer_kit.pdf)

---

*End of README.md for Team Los Grises Superiores – WRO 2025 Future Engineers*

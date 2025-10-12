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

this support have a 70 degrees of inclination using a lego 
<div align="center">
<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/9702fe8a-fe0b-4031-91d4-b61f5b70ece4" />
</div>
The support is positioned at a 70° inclination to ensure the vehicle remains within the maximum allowed height. This angle was carefully chosen to optimize the camera’s field of view, as detailed in the Power and Sense Management section.

<div align="center">
  <img width="500" height="500" alt="Chassis" src="https://github.com/user-attachments/assets/f0f2ec53-35a1-495b-a551-b19bc37c49a3" />
  <p><em>Image 1.1: Chassis photo</em></p>
</div>

[Manual Direction PDF](https://github.com/user-attachments/files/22270572/manual.direction.pdf)

---

### Steering System
Medium motor from EV3 Core Set converts rotation into steering movement (max 45°). Gear train transfers motion, wheels connected via linkage bar.

<div align="center">
  <img width="300" height="300" alt="Steering system" src="https://github.com/user-attachments/assets/813a3d07-1033-4852-a699-a6eef89279d8" />
  <p><em>Image 1.2: Steering system photo</em></p>
</div>

<div align="center">
  <img width="300" height="300" alt="Set 1" src="https://github.com/user-attachments/assets/46e202f6-aba2-4c50-96f0-182f83e499fe" />
  <p><em>Image 2.1: Set 1</em></p>
</div>

<div align="center">
  <img width="300" height="300" alt="Render front part" src="https://github.com/user-attachments/assets/f3185aaf-427e-4545-b5fc-99059a3537b4" />
  <p><em>Image 2.2: Render front part</em></p>
</div>

---

### Movement and Traction System
Two medium motors with differential system transmit energy to wheels. Transmission: 20-tooth → 12-tooth gears → 28-tooth → 20-tooth driving wheels. Position accuracy ±1°, torque 0.08 Nm, speed 240 RPM.

<div align="center">
  <img width="300" height="300" alt="Set 2" src="https://github.com/user-attachments/assets/6d06e1fc-8637-4078-b9ca-1b4b27277880" />
  <p><em>Image 3.1: Set 2</em></p>
</div>

<div align="center">
  <img width="300" height="300" alt="Render back part" src="https://github.com/user-attachments/assets/992c28f3-348e-4574-af18-7d5bda827877" />
  <p><em>Image 3.2: Render back part</em></p>
</div>

[Differential Manual PDF](https://github.com/user-attachments/files/22326888/Diferencial.manual.pdf)

---

### Differential
Distributes torque to wheels, enabling smooth cornering. Input via pinion and crown gears. Outer wheel rotates faster in turns, inner wheel slower, straight motion equal.

<div align="center">
  <img width="500" height="400" alt="Differential example" src="https://github.com/user-attachments/assets/841f8551-b8cd-43e2-a964-24c97eb4f7ce" />
  <p><em>Image 4.1: Differential example</em></p>
</div>

---

## Power and Sense Management

<img width="825" height="237" alt="Power and Sense Diagram" src="https://github.com/user-attachments/assets/9167d4d9-a9f3-4ca6-bf3f-da7acba2cc4e" />  
<p><em>Image 5.1: Power and Sense Diagram</em></p>

### Power Management
EV3 Brick controls all motors. Powered by 10V 2050 mAh battery.  
- Movement motors (2): 150–250 mA  
- Steering motor (1): 120–250 mA

<div align="center">
  <img width="406" height="297" alt="EV3 Brick" src="https://github.com/user-attachments/assets/35571866-e5ca-4a87-aad3-f22cd2aee42c" />
  <p><em>Image 5.2: EV3 Brick</em></p>
</div>

<div align="center">
  <img width="326" height="96" alt="Medium Motor Voltage" src="https://github.com/user-attachments/assets/ea92cc7c-aa1b-4ce5-b05f-c80b4cd0d48a" />
  <p><em>Image 5.3: Medium Motor Voltage</em></p>
</div>

[Hardware Developer Kit PDF](https://github.com/user-attachments/files/22328277/hardware_developer_kit.pdf)

### Sense Management
Two OpenMV H7 cameras:  
- Camera 1 → Wall avoidance  
- Camera 2 → Color detection, line counting, parking recognition  
Powered at 3.3V, max 480 mA, connected via custom PCB to EV3.

<div align="center">
  <img width="452" height="567" alt="Camera Information" src="https://github.com/user-attachments/assets/e2bb0995-a4e0-47b4-b147-fb7336de7c5f" />
  <p><em>Image 5.4: Camera Information</em></p>
</div>

---

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

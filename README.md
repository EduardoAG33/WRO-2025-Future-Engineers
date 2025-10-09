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
* [Mobility Management](#mobility-management)
  * [Chassis](#chassis) - Image 1.1: Chassis photo
  * [Steering System](#steering-system) - Image 1.2: Steering system photo - Image 2.1: Set 1 - Image 2.2: Render front part
  * [Movement and Traction System](#movement-and-traction-system) - Image 3.1: Set 2 - Image 3.2: Render back part
  * [Differential](#differential) - Image 4.1: Differential example
* [Power and Sense Management](#power-and-sense-management)
  * [Power Management](#power-management) - Image 5.1: Power and Sense Diagram - Image 5.2: EV3 Brick - Image 5.3: Medium Motor Voltage
  * [Sense Management](#sense-management) - Image 5.4: Camera Information - Image 5.5: PCB Design
* [Obstacle Management](#obstacle-management)
  * [Vision System](#vision-system) - Image 6.1: Color detection example - Image 6.2: ROI example
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
## Vehicle photos


## Mobility Management

### Chassis
We built our vehicle using LEGO pieces, chosen for their accessibility and for allowing a compact and efficient design, which ensures good performance on the track. Initially, we designed the prototype using Studio 2.0 software to identify the most suitable LEGO parts for the chassis. Then, we evaluated different steering system methods and adapted them to our custom chassis, paying close attention to the required measurements and proportions.

<div align="center">
  <img width="500" height="500" alt="Chassis" src="https://github.com/user-attachments/assets/f0f2ec53-35a1-495b-a551-b19bc37c49a3" />
  <p><em>Image 1.1: Chassis photo</em></p>
</div>

[Manual Direction PDF](https://github.com/user-attachments/files/22270572/manual.direction.pdf)

---

### Steering System
For the steering system, we opted for the medium motor from the EV3 Core Set. The gear mechanism converts and transmits the motor’s rotation into steering movement, with a maximum steering angle of 45°. On the steering motor, a 12-tooth double bevel gear transmits motion to a 12-tooth single gear, which, through a proportional shaft, transfers the movement generated by the motor to the wheels. Additionally, the wheels are connected through a linkage bar that ensures both rotate simultaneously and in a coordinated manner, providing precise control during turns and track navigation.

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
We also designed the movement and traction system that will drive our vehicle. Initially, we considered using a single LEGO medium motor with a differential system to power both wheels; however, this motor did not provide enough power. To achieve more efficient movement, a second medium motor was added to the differential system, along with a transmission that converts the motor’s energy into mechanical energy for the wheels. Using medium motors provides fast and precise movements, with a position accuracy of ±1°, a torque of 0.08 Nm, and a no-load speed of 240 RPM. The transmission consists of 20-tooth gears directly connected to 12-tooth gears. This setup increases the rotational speed delivered to the differential, which then transmits the motion through shafts to a 28-tooth gear, subsequently connected to a 20-tooth gear that drives the wheels on both sides of the vehicle.

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
**What is a differential?** It is a mechanical component located on the drive axle of a vehicle. **Operating principle:** The differential distributes torque to the wheels, enabling smooth cornering while maintaining straight-line efficiency.

- **Power input:** Motor torque transmitted via pinion and crown gears.  
- **Torque distribution:**  
  - Straight motion → both wheels rotate equally.  
  - Turning → outer wheel rotates faster than inner wheel.  
- **Power output:** Appropriate torque delivered to each wheel axle.

<div align="center">
  <img width="500" height="400" alt="Differential example" src="https://github.com/user-attachments/assets/841f8551-b8cd-43e2-a964-24c97eb4f7ce" />
  <p><em>Image 4.1: Differential example</em></p>
</div>

---

## Power and Sense Management

<img width="825" height="237" alt="Power and Sense Diagram" src="https://github.com/user-attachments/assets/9167d4d9-a9f3-4ca6-bf3f-da7acba2cc4e" />  
<p><em>Image 5.1: Power and Sense Diagram</em></p>

### Power Management
Our main controller is the EV3 Brick from LEGO Mindstorms. The EV3 receives sensor information and controls all motors. Powered by a **10V 2050 mAh lithium battery**, the EV3 optimizes energy distribution for the three medium motors:

- **Movement motors (2)** → 150–250 mA each  
- **Steering motor (1)** → 120–250 mA  

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
Two **OpenMV H7 cameras** are integrated:  

- Camera 1 → Wall avoidance  
- Camera 2 → Color detection, line counting, parking recognition  

Cameras are powered at **3.3 V, max 480 mA**, connected via a custom **PCB** to EV3 using RX/TX, Vin, GND.  

<div align="center">
  <img width="452" height="567" alt="Camera Information" src="https://github.com/user-attachments/assets/e2bb0995-a4e0-47b4-b147-fb7336de7c5f" />
  <p><em>Image 5.4: Camera Information</em></p>
</div>

<div align="center">
  <img width="400" height="300" alt="PCB Design" src="https://github.com/user-attachments/assets/7615369a-8065-4bf4-945b-35ec4d5ec838" />
  <p><em>Image 5.5: PCB Design</em></p>
</div>

---

## Obstacle Management

### Vision System
OpenMV cameras allow real-time obstacle detection and decision-making. **Color calibration** and **ROI evolution** improve detection stability:  

- **ROIs:** Low, Middle, High, Black  
- **Red blobs → Right turn**, **Green blobs → Left turn**  

<div align="center">
  <img width="400" height="300" alt="Color detection example" src="https://github.com/user-attachments/assets/48693250-7ba7-493a-86be-2a29e5a18f01" />
  <p><em>Image 6.1: Color detection example</em></p>
</div>

<div align="center">
  <img width="400" height="300" alt="ROI example" src="https://github.com/user-attachments/assets/dee862a6-c428-40a0-a374-5bb7fc4154d8" />
  <p><em>Image 6.2: ROI example</em></p>
</div>

---

## Calibration
Camera parameters (auto-gain, auto-white balance, exposure) were fixed to reduce light variation instability. LAB thresholds were progressively adjusted for **white, red, green, blue, orange** colors.

---

## ROI Evolution
| Stage | Description |
|-------|------------|
| Initial | Central dynamic ROI anchored to white floor |
| Improvement | Trapezoidal ROIs for path and pillars |
| September | Three horizontal ROIs (low, middle, high) |
| Current | Four adaptive ROIs (Low, Middle, High, Black) covering full scene |

---

## Detection and Avoidance Strategies
**Main metric:** X coordinate at blob base  

| Problem | Solution |
|---------|---------|
| Light variations | Fixed auto-gain, auto-white balance, exposure |
| Lost far pillars in curves | Extended dynamic ROIs, blob base compensation |
| Oversized blobs | X coordinate as main metric |
| Redundant OpenMV scripts | Unified via LPF2 protocol |
| Non-reactive line follower | Corridor width as proportional KP |
| Missed pillars → collision risk | Dedicated Black ROI |

---

### Line Tracking
Dynamic horizontal ROIs provide position error, translated to proportional KP signal in EV3.

### Corridor Width Regulation
Proportional correction based on corridor width from lower ROIs.

### Obstacle Avoidance
Decision based on X coordinate vs predefined target: Red → right, Green → left.

### Data Communication (OpenMV → EV3)
LPF2 protocol: data unified into slots, redundancies removed.  

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


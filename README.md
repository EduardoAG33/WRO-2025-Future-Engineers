<div align="center">
  <img src="https://github.com/user-attachments/assets/b3e384a1-e19b-4c7f-addf-655aeb32bc3a" width="850">
  <h1>World Robot Olympiad 2025 – Future Engineers</h1>
  <h3>Team Los Grises Superiores</h3>
  <p><em>Official repository for the Future Engineers category of the World Robot Olympiad 2025.</em></p>
</div>

---

## Team Members

| Member | Role | Photo |
|--------|------|-------|
| **Eric Daniel Guerrero Uresti** | Programming & Mechanics | <img src="https://github.com/user-attachments/assets/9e1509ca-ad50-48b9-ab44-2787fcce8e0e" width="120"> |
| **Paulina Ibarra Martínez** | Programming & Electronics | <img src="https://github.com/user-attachments/assets/86413c8a-610a-4270-a92d-cb3ed135d41b" width="120"> |

<div align="center">
  <img src="https://github.com/user-attachments/assets/8c940a8b-cdcd-43a6-ab31-e2c4029053f1" width="400" alt="Team Photo">
  <p><em>Team Los Grises Superiores – 2025</em></p>
</div>

---

## Table of Contents
- [Mobility Management](#mobility-management)
- [Power and Sense Management](#power-and-sense-management)
- [Obstacle Management](#obstacle-management)
- [Calibration](#calibration)
- [ROI Evolution](#roi-evolution)
- [Detection and Avoidance Strategies](#detection-and-avoidance-strategies)
- [Resources](#resources)
- [Acknowledgments](#acknowledgments)
- [License](#license)

---
## Abstract
 
 We present a **development and implementation of a autonomous vehicle** for the **WORD ROBOT OLYMPIAD 2025** The category calls "Future engineers",that this consist in two types of challenges for solve with our vehicle(Open and ):
 **Open challenge:** the vehicle have to complete three laps on a track, the starts and direction of the vehicle is choose of random 
 **Obstacles:** In this case the same form the vehicle have complete 3 laps but while detect of pilars read and green that function is like a traffic signs. 
             **Red pilars**: The vehicle turn right of the side.
             **Green pilars**: The vehicle turn left of the side.
**Documentation**: The documentation is a important part of the challenge because this is a relevant part of a engineering process, So the teams need works with a public repository.

**For more information consult here:** https://wro-association.org/wp-content/uploads/WRO-2025-Future-Engineers-Self-Driving-Cars-General-Rules.pdf 


## Vehicle photos


## Mobility Management

### Chassis

The chassis was built using LEGO components, chosen for their accessibility, modularity, and precision.  
Initial design work was conducted in **Studio 2.0**, which allowed part optimization and dimension validation.  
After evaluating various steering mechanisms, a customized compact layout was selected to balance weight and stability.

<div align="center">
  <img width="400" src="https://github.com/user-attachments/assets/f0f2ec53-35a1-495b-a551-b19bc37c49a3" alt="Chassis Photo">
  <sub><em>Image 1.1: Chassis assembly</em></sub>
</div>

---

### Steering System

The steering system is powered by a **LEGO EV3 Medium Motor**.  
A gear mechanism converts the motor’s rotation into steering movement with a **maximum angle of 45°**.  
A 12-tooth double bevel gear transfers motion through a proportional shaft connected to the wheels.  
A linkage bar ensures synchronized wheel rotation for precise directional control.

<div align="center">
  <img width="300" src="https://github.com/user-attachments/assets/813a3d07-1033-4852-a699-a6eef89279d8" alt="Steering System">
  <sub><em>Image 1.2: Steering system</em></sub>
</div>

<div align="center">
  <img width="300" src="https://github.com/user-attachments/assets/46e202f6-aba2-4c50-96f0-182f83e499fe" alt="Set 1">
  <sub><em>Image 2.1: Set 1</em></sub>
</div>

<div align="center">
  <img width="300" src="https://github.com/user-attachments/assets/f3185aaf-427e-4545-b5fc-99059a3537b4" alt="Render Front Part">
  <sub><em>Image 2.2: Front render</em></sub>
</div>

---

### Movement and Traction System

The movement system employs **two EV3 Medium Motors** powering a **differential**.  
Initially, one motor was tested but lacked sufficient torque; thus, a second motor was added for improved performance.  

Each medium motor provides:
- **Position accuracy:** ±1°  
- **Torque:** 0.08 Nm  
- **Speed:** 240 RPM (no-load)

The transmission utilizes a **20-tooth to 12-tooth** gear ratio, increasing rotational speed at the differential input.  
This motion is transmitted to a **28-tooth to 20-tooth** system that drives both rear wheels.

<div align="center">
  <img width="300" src="https://github.com/user-attachments/assets/6d06e1fc-8637-4078-b9ca-1b4b27277880" alt="Set 2">
  <sub><em>Image 3.1: Traction system set</em></sub>
</div>

<div align="center">
  <img width="300" src="https://github.com/user-attachments/assets/992c28f3-348e-4574-af18-7d5bda827877" alt="Render Back Part">
  <sub><em>Image 3.2: Rear render</em></sub>
</div>

---

### Differential

The **differential** distributes torque between the left and right wheels.  
Its key functions include:

- **Straight motion:** both wheels rotate at equal speed.  
- **Turning:** the outer wheel rotates faster than the inner wheel, allowing smooth cornering.

<div align="center">
  <img width="500" src="https://github.com/user-attachments/assets/841f8551-b8cd-43e2-a964-24c97eb4f7ce" alt="Differential Example">
  <sub><em>Image 4.1: Differential example</em></sub>
</div>

---

## Power and Sense Management

<div align="center">
  <img width="800" src="https://github.com/user-attachments/assets/9167d4d9-a9f3-4ca6-bf3f-da7acba2cc4e" alt="Power and Sense Diagram">
  <sub><em>Image 5.1: Power and sense diagram</em></sub>
</div>

### Power Management

The main controller is the **LEGO EV3 Brick**, equipped with four motor and four sensor ports.  
It is powered by a **10V, 2050 mAh lithium battery**.  

**Power consumption:**
- Two movement motors: 150–250 mA each  
- Steering motor: 120–250 mA  

<div align="center">
  <img width="400" src="https://github.com/user-attachments/assets/35571866-e5ca-4a87-aad3-f22cd2aee42c" alt="EV3 Brick">
  <sub><em>Image 5.2: EV3 Brick</em></sub>
</div>

<div align="center">
  <img width="300" src="https://github.com/user-attachments/assets/ea92cc7c-aa1b-4ce5-b05f-c80b4cd0d48a" alt="Medium Motor Voltage">
  <sub><em>Image 5.3: Medium motor voltage reference</em></sub>
</div>

---

### Sense Management

Two **OpenMV H7 cameras** are integrated for environmental awareness:
- **Camera 1:** wall avoidance  
- **Camera 2:** traffic light detection, line counting, and parking area localization  

Each camera operates at **3.3V / 480 mA** and communicates with the EV3 through a custom **EasyEDA-designed PCB** via RX, TX, Vin, and GND.

<div align="center">
  <img width="400" src="https://github.com/user-attachments/assets/e2bb0995-a4e0-47b4-b147-fb7336de7c5f" alt="Camera Info">
  <sub><em>Image 5.4: Camera specifications</em></sub>
</div>

<div align="center">
  <img width="400" src="https://github.com/user-attachments/assets/7615369a-8065-4bf4-945b-35ec4d5ec838" alt="PCB Design">
  <sub><em>Image 5.5: Custom PCB design</em></sub>
</div>

---

## Obstacle Management

### Vision System

The vision system interprets the competition field in real time using **LAB color calibration**.  
Four **Regions of Interest (ROIs)** are defined for dynamic detection and decision-making:

- **Low ROI:** line tracking  
- **Middle ROI:** obstacle and color detection  
- **High ROI:** long-distance obstacle prediction  
- **Black ROI:** collision alerts  

Detected colors determine avoidance maneuvers:
- **Red = turn right**  
- **Green = turn left**

<div align="center">
  <img width="400" src="https://github.com/user-attachments/assets/48693250-7ba7-493a-86be-2a29e5a18f01" alt="Color Detection Example">
  <sub><em>Image 6.1: Color detection example</em></sub>
</div>

---

## Calibration

Initial tests revealed color detection instability under varying light conditions.  
To address this, **auto-gain**, **auto-white balance**, and **exposure** parameters were fixed, ensuring stable detection.  
Progressive LAB threshold tuning was conducted for white, red, green, blue, and orange.

---

## ROI Evolution

The ROI system evolved through iterative testing:

| Stage | Description |
|--------|-------------|
| Initial | Single central ROI for line following. |
| Intermediate | Trapezoidal ROIs covering both track and pillars. |
| September | Three horizontal dynamic ROIs anchored to the floor. |
| Current | Four ROIs: Low, Middle, High, and Black, ensuring full scene awareness. |

<div align="center">
  <img width="400" src="https://github.com/user-attachments/assets/dee862a6-c428-40a0-a374-5bb7fc4154d8" alt="ROI Example">
  <sub><em>Image 6.2: ROI configuration example</em></sub>
</div>

---

## Detection and Avoidance Strategies

| Identified Issue | Implemented Solution |
|------------------|----------------------|
| Light variations caused unstable color readings. | Fixed exposure, gain, and white balance parameters. |
| Far pillars lost during curves. | Introduced dynamic ROIs and base-X compensation. |
| Oversized blobs created confusion. | X coordinate at blob base adopted as main metric. |
| Redundant OpenMV scripts. | Unified data transmission using LPF2 protocol. |
| Poor line tracking in variable-width corridors. | Integrated corridor width as proportional control (KP adjustment). |
| Missed collision cases. | Added dedicated Black ROI for collision alerts. |

---

### Line Tracking

Dynamic horizontal ROIs provide responsive feedback for line deviation.  
The position error is converted into a proportional control signal within the EV3 (initial **KP = 1**).

---

### Corridor Width Regulation

Using corridor width data from the **Middle ROI**, the EV3 dynamically adjusts motor speeds to maintain central alignment within narrow or wide corridors.

---

### Obstacle Avoidance

Avoidance behavior follows WRO rules:
- **Red pillar → right turn**  
- **Green pillar → left turn**

The maneuver direction is defined by comparing the blob’s X coordinate to a predefined reference.

---

### Data Communication (OpenMV → EV3)

Communication is achieved via the **LPF2 protocol**, streamlining data exchange.  

| Source | Metric | Application |
|---------|---------|-------------|
| OpenMV – Low ROI | Line error | Main trajectory correction |
| OpenMV – Middle ROI | Corridor width & color | Width regulation & obstacle prediction |
| OpenMV – High ROI | Distant obstacles | Curve anticipation |
| OpenMV – Black ROI | Dark area detection | Collision alerts |
| OpenMV – Color Blobs | X position (base Y) | Avoidance side |
| EV3 – Motor Encoders | Speed & distance | Smooth control |
| EV3 – Internal Logic | KP variable | Dynamic correction tuning |

---

## Resources

| Document | Description |
|-----------|-------------|
| [Manual Direction PDF](https://github.com/user-attachments/files/22270572/manual.direction.pdf) | Assembly and steering system guide |
| [Differential Manual PDF](https://github.com/user-attachments/files/22326888/Diferencial.manual.pdf) | Differential system documentation |
| [Hardware Developer Kit PDF](https://github.com/user-attachments/files/22328277/hardware_developer_kit.pdf) | Hardware and electrical reference |

---

## Acknowledgments

This project was developed for the **World Robot Olympiad 2025 – Future Engineers** category.  
Special thanks to mentors, partners, and supporting institutions for their guidance throughout the design and testing stages.

---

## License

This repository is released under the [MIT License](LICENSE).

---

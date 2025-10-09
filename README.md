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
- [Project Overview](#project-overview)
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

## Project Overview

### Abstract

This project presents the **development and implementation of an autonomous vehicle** designed for the **World Robot Olympiad (WRO) 2025 – Future Engineers** category.  
The competition challenges participants to design, construct, and program a self-driving car capable of completing specific tasks under varying environmental and rule-based conditions.

The **Future Engineers** category includes two types of challenges that must be solved using the same autonomous system:

- **Open Challenge:**  
  The vehicle must autonomously complete three laps on a predefined track. The **starting position** and **driving direction** (clockwise or counterclockwise) are **randomly assigned** before each run.

- **Obstacle Challenge:**  
  Similar to the Open Challenge, the vehicle must complete three laps while **detecting and responding to colored pillars** that simulate traffic signals:  
  - **Red pillars → Turn right**  
  - **Green pillars → Turn left**

In addition to performance, **technical documentation** is a critical evaluation component. Teams are required to maintain a **public repository** showcasing their engineering process, including code, CAD designs, and validation results.

For full competition details, refer to the official WRO guidelines:  
🔗 [WRO 2025 Future Engineers – General Rules (PDF)](https://wro-association.org/wp-content/uploads/WRO-2025-Future-Engineers-Self-Driving-Cars-General-Rules.pdf)

---

## Mobility Management

### Chassis

The chassis was built using LEGO components, chosen for their accessibility, modularity, and precision.  
Initial design work was conducted in **Studio 2.0**, allowing for part optimization and dimension validation.  
After evaluating several steering configurations, a compact and lightweight design was selected to balance performance and stability.

<div align="center">
  <img width="400" src="https://github.com/user-attachments/assets/f0f2ec53-35a1-495b-a551-b19bc37c49a3" alt="Chassis Photo">
  <sub><em>Image 1.1: Chassis assembly</em></sub>
</div>

---

### Steering System

The steering mechanism is powered by a **LEGO EV3 Medium Motor**.  
A gear system translates rotational movement into steering action with a **maximum steering angle of 45°**.  
A linkage bar ensures synchronous wheel movement for accurate directional control.

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

The drive system utilizes **two EV3 Medium Motors** connected through a **differential gear**.  
Initially, a single motor configuration was tested but lacked the required torque; thus, a second motor was integrated for enhanced performance and stability.

Each motor delivers:
- **Position accuracy:** ±1°  
- **Torque:** 0.08 Nm  
- **Speed:** 240 RPM (no-load)

The transmission uses a **20-tooth to 12-tooth** gear ratio for speed amplification, followed by a **28-tooth to 20-tooth** differential system driving both rear wheels.

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

The **differential** distributes torque between the left and right wheels, enabling smooth turning behavior:
- **Straight motion:** both wheels rotate equally.  
- **Turning:** the outer wheel spins faster for smooth cornering.

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

The system’s core is the **LEGO EV3 Brick**, powered by a **10V, 2050 mAh lithium battery**.  
It provides energy to all motors and sensors through dedicated ports.  

**Power consumption:**
- Movement motors: 150–250 mA each  
- Steering motor: 120–250 mA  

<div align="center">
  <img width="400" src="https://github.com/user-attachments/assets/35571866-e5ca-4a87-aad3-f22cd2aee42c" alt="EV3 Brick">
  <sub><em>Image 5.2: EV3 Brick</em></sub>
</div>

---

### Sense Management

Two **OpenMV H7 cameras** enable real-time environmental awareness:
- **Camera 1:** wall avoidance  
- **Camera 2:** color detection, line counting, and parking recognition  

Each camera communicates with the EV3 through a custom **EasyEDA-designed PCB** via UART (RX/TX).

<div align="center">
  <img width="400" src="https://github.com/user-attachments/assets/7615369a-8065-4bf4-945b-35ec4d5ec838" alt="PCB Design">
  <sub><em>Image 5.5: Custom PCB design</em></sub>
</div>

---

## Obstacle Management

The vision system uses **LAB color calibration** and defines **four ROIs** for multi-level perception:
- Low ROI – line tracking  
- Middle ROI – color and obstacle detection  
- High ROI – long-distance anticipation  
- Black ROI – collision alerts  

Color detection governs the reaction:
- **Red → Right turn**  
- **Green → Left turn**

<div align="center">
  <img width="400" src="https://github.com/user-attachments/assets/48693250-7ba7-493a-86be-2a29e5a18f01" alt="Color Detection Example">
  <sub><em>Image 6.1: Color detection example</em></sub>
</div>

---

## Calibration

To ensure stable color detection under different lighting conditions, **auto-gain**, **auto-white balance**, and **exposure** were disabled and manually adjusted.  
Each LAB threshold (for white, red, green, blue, orange) was fine-tuned through iterative testing.

---

## ROI Evolution

| Stage | Description |
|--------|-------------|
| Initial | Single ROI for basic line tracking. |
| Intermediate | Trapezoidal multi-zone configuration. |
| September | Three dynamic horizontal ROIs. |
| Current | Four adaptive ROIs (Low, Middle, High, Black) providing full-scene coverage. |

---

## Detection and Avoidance Strategies

| Issue | Solution |
|--------|-----------|
| Light variation caused unstable readings | Fixed exposure, gain, and white balance |
| Distant pillars lost in turns | Dynamic ROIs with base-X compensation |
| Oversized blobs caused misclassification | Blob base X used for stability |
| Multiple OpenMV scripts | Unified via LPF2 protocol |
| Poor line following in variable-width corridors | Proportional control based on corridor width |
| Missed black zones | Dedicated Black ROI for collision detection |

---

## Resources

| Document | Description |
|-----------|-------------|
| [Manual Direction PDF](https://github.com/user-attachments/files/22270572/manual.direction.pdf) | Assembly and steering guide |
| [Differential Manual PDF](https://github.com/user-attachments/files/22326888/Diferencial.manual.pdf) | Differential documentation |
| [Hardware Developer Kit PDF](https://github.com/user-attachments/files/22328277/hardware_developer_kit.pdf) | Hardware reference |

---

## Acknowledgments

Developed by **Team Los Grises Superiores** for the **World Robot Olympiad 2025 – Future Engineers**.  
We extend our gratitude to mentors, partners, and collaborators for their technical support and guidance.

---

## License

Released under the [MIT License](LICENSE).

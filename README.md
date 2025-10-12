# WRO-2025-Future-Engineers

Official repository of **Team Los Grises Superiores** for the *Future Engineers – World Robot Olympiad 2025*.  
<img width="1000" height="500" alt="team-banner" src="https://github.com/user-attachments/assets/b3e384a1-e19b-4c7f-addf-655aeb32bc3a" />

---

## 🧑‍🤝‍🧑 Team Photo
<div align="center">
  <img width="500" height="500" alt="Team photo" src="https://github.com/user-attachments/assets/8c940a8b-cdcd-43a6-ab31-e2c4029053f1" />
</div>

---

### 👨‍💻 Eric Daniel Guerrero Uresti
<div align="center">
  <img src="https://github.com/user-attachments/assets/9e1509ca-ad50-48b9-ab44-2787fcce8e0e" alt="Eric Guerrero photo" width="200" height="200">
</div>

**Role:** Programming & Mechanics  

I started participating in robotics tournaments from 2016 to 2019, achieving **two second places** in the Mexican Robotics Tournament (TMR). Due to the **Covid-19 pandemic**, I couldn’t compete again until 2024, when I returned as a **coach** in TMR and WRO, earning a spot at the international competition. I am currently in my final year of **Mechatronics Engineering**.

---

### 👩‍💻 Paulina Ibarra Martínez
<div align="center">
  <img src="https://github.com/user-attachments/assets/86413c8a-610a-4270-a92d-cb3ed135d41b" alt="Paulina Martinez photo" width="200" height="200">
</div>

**Role:** Programming & Electronics  

I have been part of the **Robotics Club** at *Escuela Normal Superior “Profr. Moisés Sáenz Garza”* for three years, participating in **two Mexican Robotics Tournaments**, achieving **5th place** in the most recent one. Starting in 2024, I became a **junior coach**, achieving **third place** in WRO 2024 and **first place nationally** in the Mexican Robotics Tournament 2025.

---

## 📚 Contents
- [Project Overview](#project-overview)
- [Vehicle Photos](#vehicle-photos)
- [Components and Hardware](#components-and-hardware)
- [Mobility Management](#mobility-management)
- [Power and Sense Management](#power-and-sense-management)
- [Obstacle Management](#obstacle-management)
- [Calibration](#calibration)
- [ROI Evolution](#roi-evolution)
- [Detection and Avoidance Strategies](#detection-and-avoidance-strategies)
- [Downloads and Documentation](#downloads-and-documentation)

---

## 🚗 Project Overview

The **Future Engineers** category challenges participants to design and program a **self-driving car** capable of completing specific tasks autonomously.

### 🏁 Competition Challenges
1. **Open Challenge** – 3 laps on a random track direction (clockwise/counterclockwise).  
2. **Obstacle Challenge** – Same as above, but with colored pillars:  
   - 🟥 **Red** → Turn right  
   - 🟩 **Green** → Turn left  

📄 [WRO 2025 Future Engineers – General Rules (PDF)](https://wro-association.org/wp-content/uploads/WRO-2025-Future-Engineers-Self-Driving-Cars-General-Rules.pdf)

---

## 📸 Vehicle Photos
*(Add vehicle photos here)*

---

## ⚙️ Components and Hardware

| Component | Description | Image | Purchase Link |
|-----------|--------------|--------|----------------|
| **45544 LEGO MINDSTORMS Education EV3 Core Set** | Forms the foundational structure and chassis. | <img width="100" height="100" src="https://github.com/user-attachments/assets/a725c977-b28b-4b5d-b95c-506c84cd6706" /> | [Buy here](https://bricks-store.com/esp/item/585/66/45544-set-base-lego-mindstorms-education-ev3) |
| **OpenMV Cam H7 Plus** | Smart camera for navigation and obstacle detection. | <img width="100" height="100" src="https://github.com/user-attachments/assets/2f1dc12c-a2f9-4e47-b665-d9b37091a8ce" /> | [Buy here](https://openmv.io/products/openmv-cam-h7-plus) |
| **HC-SR04 Ultrasonic Sensor** | Distance measurement sensor. | <img width="100" height="100" src="https://github.com/user-attachments/assets/f55c9c1f-b8f7-4d51-9b24-01f51de329b8" /> | [Buy here](https://uelectronics.com/producto/sensor-ultrasonico-hc-sr04/) |
| **Arduino Nano** | ATmega328-based microcontroller for control tasks. | <img width="100" height="100" src="https://github.com/user-attachments/assets/22e8f59c-909d-4ff2-b637-dc03e15f4de6" /> | [Buy here](https://www.steren.com.mx/placa-de-desarrollo-nano.html) |
| **4x4 RGB LED Matrix** | Compact display module with 16 RGB LEDs (4x4 grid). | <img width="100" height="100" src="https://github.com/user-attachments/assets/1dfe866c-7431-4e3f-93b5-e756a8c59637" /> | [Buy here](https://mvelectronica.com/producto/matriz-de-led-rgb-4x4-ws2812-16bits-a-5v-led-5050) |
| **LTC1871 DC-DC Step-up Boost Converter** | Increases low input voltage to a stable higher output. | <img width="100" height="100" src="https://github.com/user-attachments/assets/5ebb04f5-a49e-4a5f-b0ff-865bd1fc2c5e" /> | [Buy here](https://mvelectronica.com/producto/elevador-de-voltaje-ltc1871-dc-dc-step-up-boost-entrada-3-35v-salida-3-5-35v-6a#2) |

---

## 🧩 Mobility Management

### 🧱 Chassis
Constructed with **LEGO components** and an **acrylic platform** for ultrasonic sensors, shaped with heat bending at 90° for precise alignment.  
The assembly ensures sensor stability and efficient cable routing.

<div align="center">
  <img width="700" src="https://github.com/user-attachments/assets/48febdb7-b3fb-46fc-b429-0648d3b4971d" />
</div>

📄 [HC-SR04 Datasheet with Dimensions (PDF)]()

---

### ⚙️ Steering System
EV3 medium motor controls steering via gear train and linkage bar (±45° range).  

<div align="center">
  <img width="300" src="https://github.com/user-attachments/assets/813a3d07-1033-4852-a699-a6eef89279d8" />
</div>

---

### 🚙 Movement and Traction System
Two EV3 medium motors drive wheels through differential gearing:
- **Transmission:** 20T → 12T → 28T → 20T  
- **Accuracy:** ±1°  
- **Torque:** 0.08 Nm  
- **Speed:** 240 RPM  

📄 [Differential Manual (PDF)](https://github.com/user-attachments/files/22326888/Diferencial.manual.pdf)

---

### ⚖️ Differential
Balances wheel speed during turns for stability and smooth motion.

<div align="center">
  <img width="500" src="https://github.com/user-attachments/assets/841f8551-b8cd-43e2-a964-24c97eb4f7ce" />
</div>

---

## 🔋 Power and Sense Management

### ⚡ Power
- EV3 Brick (main controller) powered by **10 V / 2050 mAh** battery  
- Movement motors: 150–250 mA  
- Steering motor: 120–250 mA  

📄 [Hardware Developer Kit (PDF)](https://github.com/user-attachments/files/22328277/hardware_developer_kit.pdf)

---

### 👁️ Sensors
Two **OpenMV H7** cameras handle wall and pillar detection.  
Powered at 3.3 V / 480 mA via PCB linked to EV3.

---

## 🚧 Obstacle Management
OpenMV cameras detect colors:
- 🟥 Red → Turn right  
- 🟩 Green → Turn left  
ROIs dynamically adapt to track color and light variation.

---

## 🧭 Calibration
- Manual tuning of **gain**, **exposure**, and **white balance**.  
- LAB color thresholds for white, red, green, blue, orange.

---

## 📊 ROI Evolution
| Stage | Description |
|--------|-------------|
| Initial | Central ROI on white surface |
| Intermediate | Trapezoidal ROIs for edges |
| September | Three horizontal ROIs |
| Current | Four adaptive ROIs covering full scene |

---

## 🤖 Detection and Avoidance Strategies
| Problem | Solution |
|----------|-----------|
| Lighting variation | Fixed gain and white balance |
| Pillar loss | Dynamic ROI compensation |
| Big color blobs | X-position filtering |
| Multi-script delays | Unified via LPF2 |
| Line lag | KP dynamic adjustment |
| Missed pillars | Black ROI detection |

---

### Communication (OpenMV → EV3)
Protocol: **LPF2 data exchange**

| Source | Metric | Purpose |
|---------|---------|----------|
| Low ROI | Line error | Path correction |
| Middle ROI | Width | Regulation |
| High ROI | Obstacles | Predictive turn |
| Black ROI | Shadow | Collision alert |
| Color ROI | X coord | Turn direction |
| Motors | Speed | Stability |
| EV3 logic | KP | Dynamic correction |

---

## 📥 Downloads and Documentation

### 📂 PDFs
| File | Description | Link |
|------|--------------|------|
| **Manual Direction** | Vehicle direction manual | [Download PDF](https://github.com/user-attachments/files/22270572/manual.direction.pdf) |
| **Differential Manual** | Explanation of differential system | [Download PDF](https://github.com/user-attachments/files/22326888/Diferencial.manual.pdf) |
| **Hardware Developer Kit** | Electrical and power schematics | [Download PDF](https://github.com/user-attachments/files/22328277/hardware_developer_kit.pdf) |

---

### 💾 Code and Data
| Folder | Description |
|---------|-------------|
| `/code/EV3/` | EV3 programs and logic |
| `/code/OpenMV/` | Vision and detection scripts |
| `/hardware/` | PCB layouts, circuit schematics |
| `/docs/` | Manuals, datasheets, and design files |

---

### 🔗 External Media
🎥 [Competition Video – YouTube](https://youtu.be/6IZq3YB_JEY)  
🎥 [Demonstration Video – YouTube](https://youtu.be/ddZvpzC4xFE)

---

### 🏆 Acknowledgments
Special thanks to **WRO México**, **TMR**, and **Autotecno** for the technical support and learning resources that made this project possible.

---

### © 2025 Team Los Grises Superiores
All rights reserved. Repository for **educational and competition purposes only**.

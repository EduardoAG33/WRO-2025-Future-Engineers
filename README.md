<div align="center">
  <img src="https://github.com/user-attachments/assets/b3e384a1-e19b-4c7f-addf-655aeb32bc3a" width="800">
  <h1>Team Los Grises Superiores – WRO 2025 Future Engineers</h1>
  <p><em>Official repository for the World Robot Olympiad 2025 – Future Engineers Category</em></p>
</div>

---

## **Project Summary**

This project showcases the autonomous vehicle developed by *Los Grises Superiores* for the **WRO 2025 – Future Engineers** category. It integrates computer vision, differential drive control, and gyroscopic stabilization to achieve adaptive navigation and obstacle avoidance. Built on the LEGO SPIKE Prime platform, the system demonstrates precision, modularity, and intelligent response in real-world conditions.

---

## **Introduction**

We present the **development and implementation of an autonomous vehicle** designed for the **World Robot Olympiad 2025 – Future Engineers** category. This competition challenges teams to apply principles of robotics, computer vision, and control systems to design a self-driving car capable of operating fully autonomously.

The category includes two main challenges:

- **Open Challenge:**  
  The vehicle must complete three laps on a defined track. The starting position and driving direction (clockwise or counterclockwise) are determined randomly before each attempt.

- **Obstacle Challenge:**  
  In this challenge, the vehicle must again complete three laps, but while detecting and responding to colored pillars that act as traffic signs:  
  - **Red pillars:** The vehicle must turn to the right.  
  - **Green pillars:** The vehicle must turn to the left.  

Documentation is a key part of the competition, representing the engineering process behind the development. Each team is required to maintain a **public repository** containing source code, design documentation, and technical reports that detail the evolution of the project.

For additional details about the competition and official requirements, please refer to the official document:  
🔗 [WRO 2025 Future Engineers – General Rules (PDF)](https://wro-association.org/wp-content/uploads/WRO-2025-Future-Engineers-Self-Driving-Cars-General-Rules.pdf)

---

## **Team Members**

| Member | Role | Photo |
|--------|------|-------|
| **Eric Daniel Guerrero Uresti** | Programming & Mechanics | <img src="https://github.com/user-attachments/assets/9e1509ca-ad50-48b9-ab44-2787fcce8e0e" width="120"> |
| **Paulina Ibarra Martínez** | Programming & Electronics | <img src="https://github.com/user-attachments/assets/86413c8a-610a-4270-a92d-cb3ed135d41b" width="120"> |

---

## **Team Photo**

<div align="center">
  <img src="https://github.com/user-attachments/assets/ff0b7a13-bbde-4b50-88b0-5091e2c41d46" width="500">
</div>

---

## **Mobility Management**

The vehicle uses a differential drive configuration with two main motors controlled by a proportional gain (KP) system for precise navigation. This setup ensures smooth turns and stable forward motion, even when the gyro readings vary. The control loop dynamically adjusts motor speeds to maintain trajectory stability.

---

## **Power and Sense Management**

The system integrates several sensors to maintain environmental awareness:
- **HuskyLens** for visual recognition and object detection.
- **Gyroscope** for orientation and angular correction.
- **Internal sensors** from the SPIKE Prime hub for motion feedback and stability control.

Power management ensures that motor performance remains consistent across the full battery cycle.

---

## **Obstacle Management**

During the Obstacle Challenge, the HuskyLens identifies pillar colors and sends commands to adjust direction:
- Red pillars trigger a **right turn** sequence.
- Green pillars trigger a **left turn** sequence.

The detection routine is optimized for low latency to maintain fluid movement during lap transitions.

---

## **Calibration**

Calibration routines are implemented at the beginning of each run to reset gyro and position readings. This prevents cumulative drift errors, ensuring accurate orientation and alignment throughout all laps.

---

## **ROI Evolution**

The **Region of Interest (ROI)** dynamically adapts during image processing. The system continuously updates the ROI based on detected object size and position, improving both detection accuracy and response time.

---

## **Detection and Avoidance Strategies**

The detection algorithm integrates camera input with motion data to anticipate obstacle positions. Combined with PID-based motor control, the robot can perform smooth avoidance maneuvers while maintaining track position. 

The control logic prioritizes obstacle detection while ensuring lap completion efficiency.

---

## **Resources**

| Document | Description |
|-----------|-------------|
| [Manual Direction PDF](https://github.com/user-attachments/files/22270572/manual.direction.pdf) | Assembly and operation of steering system |
| [Differential Manual PDF](https://github.com/user-attachments/files/22326888/Diferencial.manual.pdf) | Mechanical differential documentation |
| [Hardware Developer Kit PDF](https://github.com/user-attachments/files/22328277/hardware_developer_kit.pdf) | Electrical and hardware reference manual |

---

## **Acknowledgments**

This project was developed by **Team Los Grises Superiores** as part of the **World Robot Olympiad 2025 – Future Engineers** category.  
Special thanks to our mentors and supporting institutions for their guidance and collaboration.

---

## **License**

This repository is released under the [MIT License](LICENSE).


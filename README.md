# Ball Balancing Platform using Raspberry Pi and Stepper Motors

This project involves building a platform that balances a ball on top of a moving surface using stepper motors controlled by a Raspberry Pi. The system uses inverse kinematics to compute precise arm angles and stabilize the platform based on the ball's real-time position.

## Features

- Precision control using **NEMA 17 stepper motors** and **microstep drivers**.
- Platform motion calculated using **inverse kinematics**.
- **Raspberry Pi** used for control and computation.
- Modular mechanical setup with brackets, platform, arms, and motor mounts.


## Hardware Used

- Raspberry Pi 
- NEMA 17 Stepper Motors
- Microstep Driver 
- 3D-printed platform and frame
- Metal brackets, linkages, ball joint connectors
- Power supply unit
  

## Software & Tools

- Python 
- Inverse Kinematics calculations
- MATLAB (for kinematic model verification)
- Raspberry Pi OS

## Algorithm Overview

1. **Platform Setup:** Align 3 motor-driven prismatic arms supporting a moving platform.
2. **Initial Calibration:** Define home positions for all motors.
3. **IK Calculations:** Compute necessary stepper angles from desired platform tilt.
4. **Control Loop:** (Upcoming) Use camera input to detect ball position and feed it to the IK model.




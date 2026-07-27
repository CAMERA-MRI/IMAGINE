---
layout: component
title: "Field Mapping Robot"
scanner_id: ernie
category: "robot"
description: "A automated 3-axis translation stage driven by stepper motors and programmed to profile the magnet's field homogeneity."
video_url: "/ERNIE/Build your own Design/Robot/Robot introductory video/ernie_robot_intro.mp4"
downloads:
  - name: "Sipan's Robot Repository"
    path: "https://github.com/SipanHovsep/Field_mapper_robot"
bom:
  - item: "Arduino Mega 2560 Board"
    qty: 1
    price: "$74.72"
    link: "https://www.amazon.ca/Arduino-A000067-ARDUINO-MEGA2560-REVISION/dp/B0046AMGW0"
  - item: "NEMA 17 Stepper Motors"
    qty: 3
    price: "$35.00"
  - item: "A4988 Stepper Motor Driver Boards"
    qty: 3
    price: "$10.00"
  - item: "Power Supply for the Robot (12V 5A)"
    qty: 1
    price: "$23.00"
  - item: "Jumper Wires & Breadboard Pack"
    qty: 1
    price: "$23.00"
  - item: "Hall Effect Probe (e.g. Lakeshore or custom)"
    qty: 1
    price: "Varies"
assembly_guide: |
  #### Phase 1: Gantry Assembly
  1. Print the 3-axis slider parts (X, Y, Z translation mounts) in PLA or PETG.
  2. Assemble the smooth rods and lead screws on the gantry frame.
  3. Mount the three NEMA 17 stepper motors onto the linear stages.
  
  #### Phase 2: Electronics Wiring
  1. Mount the A4988 drivers onto the Arduino CNC shield or wire directly on a breadboard.
  2. Connect the stepper motor coils to the driver outputs.
  3. Connect the stepper drivers' STEP and DIR pins to the designated digital outputs on the Arduino Mega.
  4. Wire the 12V power supply to the driver power rails.
  
  #### Phase 3: Firmware Upload
  1. Clone the firmware repository: [Field Mapper Robot Repository](https://github.com/SipanHovsep/Field_mapper_robot).
  2. Upload the Arduino stepper driver control sketch using the Arduino IDE.
testing_guide: |
  #### Robot Calibration and Hall Probe Verification
  1. Power on the robot and verify that each axis moves smoothly without binding.
  2. Perform axis homing commands and measure actual travel distance against commanded steps.
  3. Wire the Hall probe to the analog/digital read pins.
  4. Run a 1D scan sweep along the Z-axis (through the center of the magnet bore) and compare the readings to the expected Halbach field curve.
---
The **Field Mapping Robot** is an essential part of the ERNIE educational toolkit. To achieve high-contrast MR imaging, the magnetic field must be extremely homogeneous. The robot automates the tedious task of measuring the magnetic field in 3D space, logging the data to a host computer where shimming algorithms calculate the required shim magnet correction configurations.

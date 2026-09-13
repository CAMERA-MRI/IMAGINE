---
layout: component
title: "ERNIE Robot Controller & Drivers"
scanner_id: ernie
category: "robot"
description: "The microcontroller electronics and motor drivers controlling the 3-axis field mapping robot."
downloads:
  - name: "Motor Driver & Arduino Casing STL"
    path: "/ERNIE/Build your own Design/Magnet/Scanner parts for 3D printing/Motor Driver Casing.stl"
  - name: "Robot Control Firmware (Arduino)"
    path: "/ERNIE/Build your own Design/Robot/Field Mapping Software/Robot_code/Code_field_mapping_robot/Code_field_mapping_robot.ino"
bom:
  - item: "Arduino Uno R4 Minima"
    part_number: "ABX00080"
    qty: 1
    price: "$33.50 CAD"
    link: "https://thepihut.com/products/arduino-uno-r4-minima"
  - item: "Stepper Motor Drivers"
    qty: 3
    price: "$34.62 CAD"
    link: "https://www.aliexpress.com/item/1005005967708477.html"
  - item: "Motor Driver + Arduino Casing (3D Printed PLA)"
    qty: 1
    price: "3D Printed (PLA)"
  - item: "Connecting Hookup Wires (22 AWG)"
    qty: 25
    price: "$23.99 CAD"
    link: "https://www.amazon.ca/TUOFENG-Hookup-Wires-6-Different-Colored/dp/B0CM2Y7V1Z"
  - item: "DC Power Supply (24V, 3A, 72W)"
    part_number: "CA-24V-3A-72W"
    qty: 1
    price: "$22.99 CAD"
    link: "https://www.amazon.ca/dp/B0B9XGQQSR"
assembly_guide: |
  #### Controller Wiring & Flashing
  1. Mount the Arduino Uno and 3 stepper motor driver modules into the 3D-printed casing.
  2. Connect motor step and direction pins to the designated digital pins on the Arduino.
  3. Wire the 24V power supply to the motor driver power inputs.
  4. Flash the Arduino with `Code_field_mapping_robot.ino` from the repository.
testing_guide: |
  #### Driver & Motion Testing
  1. Issue serial motion commands (G-code style coordinates) via serial monitor.
  2. Verify step accuracy: 10 mm commanded motion equals 10.0 mm measured on calipers.
---
## Overview

The **Robot Controller & Drivers** subsystem handles precise microstepping for all three axes. It interprets Cartesian coordinates sent from the host computer and controls the stepper motors synchronously.

---
layout: component
title: "ERNIE Gaussmeter & Hall Sensor"
scanner_id: ernie
category: "robot"
description: "High-precision AlphaLab GM2 Gaussmeter, 3D-printed probe holder, and zero-gauss calibrator chamber for B0 field mapping."
downloads:
  - name: "Gaussmeter Probe Holder STL"
    path: "/ERNIE/Build your own Design/Magnet/Scanner parts for 3D printing/Sensor_mount_1.stl"
bom:
  - item: "AlphaLab GM2 Gaussmeter"
    part_number: "GM2"
    qty: 1
    price: "$1,200.00 CAD"
    link: "https://www.alphalabinc.com/products/gm2/"
  - item: "Gauss Meter Probe Holder Mount (3D Printed PLA)"
    qty: 1
    price: "3D Printed (PLA)"
  - item: "Zero Gauss Chamber (Probe Calibrator, ZGC)"
    part_number: "ZGC"
    qty: 1
    price: "$196.00 CAD"
    link: "https://www.alphalabinc.com/products/zgc/"
  - item: "Gauss Meter Protective Hard Casing"
    part_number: "HC-GM2"
    qty: 1
    price: "$33.00 CAD"
    link: "https://www.alphalabinc.com/products/hc-gm2/"
  - item: "9V Replacement Batteries (Interstate DRY0196)"
    part_number: "DRY0196"
    qty: "1 Set (12)"
    price: "$35.43 CAD"
assembly_guide: |
  #### Sensor Installation and Alignment
  1. Mount the AlphaLab GM2 Hall effect probe into the 3D-printed probe holder attached to the Z-axis carriage.
  2. Align the sensor active area with the longitudinal axis of the bore.
  3. Connect the GM2 serial/analog output to the data acquisition laptop.
testing_guide: |
  #### Probe Calibration & Mapping Routine
  1. Place the Hall probe inside the Zero Gauss Chamber (ZGC) and zero the meter.
  2. Execute an automated 3D raster scan across a 50×50×50 mm grid at 2 mm resolution.
  3. Plot B0 field distribution and verify 50 mT field center.
---
## Overview

The **Gaussmeter & Hall Sensor** subsystem measures the magnetic field with high precision (0.01 mT resolution). In conjunction with the 3D gantry and Python mapping software, it produces high-resolution 3D field maps used to evaluate magnet assembly quality and homogeneity.

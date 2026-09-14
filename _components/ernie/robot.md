---
layout: component
title: "ERNIE 3-Axis Cartesian Gantry"
scanner_id: ernie
category: "robot"
description: "The 3-axis automated mechanical positioning system used to move the Hall probe inside the magnet bore."
video_url: "/assets/videos/ernie_robot_intro.mp4"
video_caption: "ERNIE 3-Axis Field Mapping Robot Setup & Operation Video"
downloads:
  - name: "Scanner Base for Field Mapping STL"
    path: "/ERNIE/Build your own Design/Magnet/Scanner parts for 3D printing/Scanner Base for field mapping.stl"
bom:
  - item: "Linear Motion Rails (Set of 3, 150mm X/Y/Z, T06)"
    part_number: "T06"
    qty: 3
    price: "$273.78 CAD"
    link: "https://www.aliexpress.com/item/1005005534966065.html"
  - item: "M4 & M3 Mounting Screws"
    qty: 8
    price: "Included with rails"
  - item: "Scanner Base for Field Mapping (3D Printed PLA)"
    qty: 4
    price: "3D Printed (PLA)"
assembly_guide: |
  #### 🤖 Mechanical Gantry Construction & Setup

  Watch the introductory and assembly video above demonstrating the 3-axis robot mechanics, motion stages, and stepper drive alignment.

  1. **Base Mounting**: Secure the 4 3D-printed PLA Scanner Base brackets to the rigid non-magnetic assembly table.
  2. **X-Axis Installation**: Mount the primary horizontal linear rail onto the base brackets and tighten the M4 fastening screws.
  3. **Y-Axis & Z-Axis Assembly**: Attach the vertical Y-axis stage perpendicularly to the X carriage, then mount the forward Z-axis probe carriage.
  4. **Smooth Travel Verification**: Manually slide each stage across its full 150 mm range to verify zero mechanical binding or backlash before attaching motor couplings.
testing_guide: |
  #### ⚙️ Travel, Orthogonality & Raster Mapping Validation
  1. **Orthogonality Check**: Use a precision machinist square to verify 90° orthogonality across X, Y, and Z stages.
  2. **Automated Motion Test**: Run test raster scan routines via the Arduino firmware (as demonstrated in the robot intro video) to confirm smooth step response, speed ramps, and reproducible return-to-origin positioning.
  3. **Probe Clearance**: Verify that the Hall probe carriage translates safely into and out of the magnet bore without contacting ring inner walls.
---
## Overview

The **3-Axis Cartesian Gantry** provides smooth, automated scanning across the central bore of the ERNIE magnet. With 150 mm travel on all axes, it raster-scans the Hall sensor throughout the target field of view.

---
layout: component
title: "ERNIE 3-Axis Cartesian Gantry"
scanner_id: ernie
category: "robot"
description: "The 3-axis automated mechanical positioning system used to move the Hall probe inside the magnet bore."
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
  #### Mechanical Gantry Construction
  1. Fasten the 4 PLA Scanner Base mounting brackets to the work table.
  2. Assemble the X-axis linear slide onto the base mounts.
  3. Mount the Y-axis stage vertically perpendicular to X, then mount the Z-axis probe stage.
  4. Ensure all stages move smoothly along their full 150 mm travel without binding.
testing_guide: |
  #### Travel & Orthogonality Validation
  1. Check stage orthogonality with a precision machinist square.
  2. Test travel limits and zero position repeatability.
---
## Overview

The **3-Axis Cartesian Gantry** provides smooth, automated scanning across the central bore of the ERNIE magnet. With 150 mm travel on all axes, it raster-scans the Hall sensor throughout the target field of view.

---
layout: component
title: "ERNIE Halbach Magnet Rings"
scanner_id: ernie
category: "magnet"
description: "The primary B0 field source for the ERNIE educational scanner: 7 3D-printed rings housing 98 N48 Neodymium magnets in an optimized Halbach geometry."
video_url: "/ERNIE/Build your own Design/Magnet/Instructions/Animation/Assembly_Animation.mp4"
downloads:
  - name: "Ring 42 STL"
    path: "/ERNIE/Build your own Design/Magnet/Scanner parts for 3D printing/ERNIE 1&2 rings and lids (.stl)/Ring 42 (105mm_length ).stl"
  - name: "Ring 251 STL"
    path: "/ERNIE/Build your own Design/Magnet/Scanner parts for 3D printing/ERNIE 1&2 rings and lids (.stl)/Ring 251.stl"
  - name: "Ring 288 STL"
    path: "/ERNIE/Build your own Design/Magnet/Scanner parts for 3D printing/ERNIE 1&2 rings and lids (.stl)/Ring 288.stl"
  - name: "Ring 321 STL"
    path: "/ERNIE/Build your own Design/Magnet/Scanner parts for 3D printing/ERNIE 1&2 rings and lids (.stl)/Ring 321 (105mm_length).stl"
  - name: "Lid for Ring 42 STL"
    path: "/ERNIE/Build your own Design/Magnet/Scanner parts for 3D printing/ERNIE 1&2 rings and lids (.stl)/Lid_For_Ring_42.stl"
  - name: "Lid for Rings 251 and 288 STL"
    path: "/ERNIE/Build your own Design/Magnet/Scanner parts for 3D printing/ERNIE 1&2 rings and lids (.stl)/Lid_For_Rings 288 and 251.stl"
bom:
  - item: "Ring 42 (3D Printed PLA, ~134g each)"
    qty: 2
    price: "3D Printed (PLA)"
  - item: "Ring 251 (3D Printed PLA, ~134g each)"
    qty: 2
    price: "3D Printed (PLA)"
  - item: "Ring 288 (3D Printed PLA, ~134g each)"
    qty: 2
    price: "3D Printed (PLA)"
  - item: "Ring 321 (3D Printed PLA, ~134g)"
    qty: 1
    price: "3D Printed (PLA)"
  - item: "Lids for Ring 42 (~45g PLA each)"
    qty: 2
    price: "3D Printed (PLA)"
  - item: "Lids for Rings 251 & 288 (~45g PLA each)"
    qty: 4
    price: "3D Printed (PLA)"
  - item: "Lid for Ring 321 (~45g PLA)"
    qty: 1
    price: "3D Printed (PLA)"
  - item: "N48 Neodymium Magnets (12x12x12mm, Magfine)"
    qty: 98
    price: "$575.26 CAD"
    link: "https://www.magfine.ca/products/neodymium-magnet-square-13mm-x-12mm-x-5mm"
  - item: "Reference Neodymium Magnets (marked polarity)"
    qty: 4
    price: "$23.48 CAD"
assembly_guide: |
  #### Ring Printing and Magnet Loading
  1. **3D Printing**: Print the 7 housing rings (Rings 42 x2, Rings 251 x2, Rings 288 x2, Ring 321 x1) and corresponding lids using PLA with 20% infill.
  2. **Install Heat-Set Inserts**: Press M3 brass heat-set inserts into each ring housing hole.
  3. **Polarity Marking**: Using a compass and reference magnet, mark the north pole of all 98 NdFeB magnets.
  4. **Magnet Insertion**: Carefully insert magnets into their slots following the exact rotational angles defined by the genetic algorithm.
  5. **Cover Fastening**: Fasten the 3D-printed lids over the magnet pockets using M3 brass screws.
testing_guide: |
  #### Ring Field Verification
  1. Measure magnetic field direction of each completed ring with a handheld Hall compass.
  2. Verify that there are no inverted or misaligned magnets prior to final stacking on the gantry rods.
---
## Overview

The **ERNIE Halbach Magnet Rings** form the core of the educational scanner. The array consists of 7 modular rings containing 98 permanent neodymium magnet cubes (12×12×12 mm, grade N48).

The angular distribution and axial ring positions were determined using genetic algorithm optimization to yield a 50 mT target field with maximal central uniformity.

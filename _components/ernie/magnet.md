---
layout: component
title: "ERNIE Halbach Magnet Rings"
scanner_id: ernie
category: "magnet"
description: "The primary B0 field source for the ERNIE educational scanner: 7 3D-printed rings housing 98 N48 Neodymium magnets in an optimized Halbach geometry."
video_url: "/assets/videos/Assembly_Animation.mp4"
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
  ### 🛠️ Magnet Assembly Procedure

  The complete step-by-step magnet assembly guide is available as a PDF:  
  👉 [How to assemble the magnet (PDF)](https://github.com/CAMERA-MRI/IMAGINE/blob/gh-pages/ERNIE/Build%20your%20own%20Design/Magnet/Instructions/How%20to%20assemble%20the%20magnet.pdf)

  <p align="center"><img src="/IMAGINE/images/magnet_procedure.png" alt="Magnet Assembly Procedure Steps A through F" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);" /></p>

  The sequence of steps for the scanner magnet assembly is summarized as follows:
  1. **(A) Polarity Determination**: Determine and mark all 98 NdFeB magnet polarities using a reference magnet and compass.
  2. **(B) Magnet Installation & Alignment**: Install magnets into the ring slots and verify alignment for each ring using a compass.
  3. **(C) Lid Covering**: Cover each loaded ring with its corresponding 3D-printed lid.
  4. **(D) Fastening**: Screw down each lid with non-magnetic brass screws.
  5. **(E) Rod & Spacer Stacking**: Assemble all 7 rings on threaded brass rods, supported by precision 3D-printed spacers.
  6. **(F) Complete Halbach Array**: Secure the full array assembly as designed to produce the target homogeneous transverse B0 field.

testing_guide: |
  ### 🧪 Field Homogeneity & Verification Testing
  1. **Compass Alignment Check**: Pass a magnetic compass around each individual ring perimeter prior to fastening lids to ensure no reversed poles exist.
  2. **Hall Probe Field Measurement**: Using the 3-axis Field Mapping Robot, map the central field profile across a 20×20×20 mm DSV to verify B0 field strength (~50 mT) and calculate field homogeneity.
  3. **Multi-Site Reproducibility**: Cross-reference field maps against benchmarks recorded in the [Reproducibility Experiment](https://github.com/CAMERA-MRI/IMAGINE/blob/gh-pages/ERNIE/Training%20sessions/Reproducibility%20experiment.md).
---
## Overview

This section provides the **.stl** files that can be 3D printed out to assemble the ERNIE 1&2 scanners. The scanner magnet array is made up of **7 rings** and their corresponding lids:

* **Ring_321**: Placed at the center of the Halbach array.
* **Ring_288**: Positioned on both sides of the center ring.
* **Ring_251**: Positioned next on both outer sides.
* **Ring_42**: Positioned at the outer ends of the array.

The angular distribution and positions were optimized via a Genetic Algorithm (GA) to maximize central magnetic field homogeneity at approximately 50 mT.

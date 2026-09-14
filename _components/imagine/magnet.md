---
layout: component
title: "120mm Bore Halbach Magnet Array"
scanner_id: imagine
category: "magnet"
description: "The primary B0 magnetic field source for the IMAGINE rat/preclinical scanner: a 120mm clear bore Halbach array producing ~50 mT with high homogeneity."
video_url: "/assets/videos/Assembly_Animation.mp4"
video_caption: "Halbach Magnet Array Stacking & Assembly Demonstration Animation"
testing_video_url: "/assets/videos/ernie_robot_intro.mp4"
testing_video_caption: "Automated 3D Field Mapping Robot Operation Video"
downloads:
  - name: "Full Magnet Assembly (Inventor IAM)"
    path: "/Hardware/Halbach Array/IAM files/Rat_Scanner_120_Ass.iam"
  - name: "Central Ring 842 (STEP)"
    path: "/Hardware/Halbach Array/STP Files/Ring_842.stp"
  - name: "Ring 0 (STEP)"
    path: "/Hardware/Halbach Array/STP Files/Ring_0.stp"
  - name: "Ring 1 (STEP)"
    path: "/Hardware/Halbach Array/STP Files/Ring_1.stp"
  - name: "Ring 945 (STEP)"
    path: "/Hardware/Halbach Array/STP Files/Ring_945.stp"
  - name: "Ring 1050 (STEP)"
    path: "/Hardware/Halbach Array/STP Files/Ring_1050.stp"
  - name: "Ring 10 Front (STEP)"
    path: "/Hardware/Halbach Array/STP Files/Ring_10_front.stp"
  - name: "Ring 10 Back (STEP)"
    path: "/Hardware/Halbach Array/STP Files/Ring_10_back.stp"
  - name: "Shim Tray (Inventor IPT)"
    path: "/Hardware/Halbach Array/ITP Files/Shim_Tray.ipt"
bom:
  - item: "M4 Threaded Brass Rods (262mm long)"
    part_number: "Brass_Rod_M4.ipt"
    qty: 8
    price: "$35.00 CAD"
  - item: "M4x3.2mm Hex Nuts (Brass/Non-magnetic)"
    part_number: "M4x3.2mm Hex Nut.ipt"
    qty: 160
    price: "$15.00 CAD"
  - item: "M4 Dome Nuts"
    part_number: "M4 Dome nut.ipt"
    qty: 16
    price: "$12.00 CAD"
  - item: "M4 Nylon Washers"
    part_number: "M4_Nylon_Washer.ipt"
    qty: 16
    price: "$4.00 CAD"
  - item: "M3x8mm Screws (Lid fasteners)"
    part_number: "M3x8.ipt"
    qty: 125
    price: "$14.00 CAD"
  - item: "Lid Loose (for Rings 842, 945, 1050)"
    part_number: "Lid_Loose.ipt"
    qty: 5
    price: "3D Printed (PLA)"
  - item: "Lid Tight (for Rings 0, 1, 10)"
    part_number: "Lid_tight.ipt"
    qty: 6
    price: "3D Printed (PLA)"
  - item: "N48/N52 Neodymium Permanent Magnets (12x12x12mm)"
    qty: 168
    price: "Approx. $420.00 CAD"
    link: "https://www.supermagnete.de/"
  - item: "M3 Brass Heat-Set Inserts"
    qty: 125
    price: "$18.00 CAD"
  - item: "Passive Shim Trays"
    part_number: "Shim_Tray.ipt"
    qty: 16
    price: "3D Printed (PLA)"
assembly_guide: |
  #### Mirrored Halbach Magnet Assembly Procedure

  *Watch the assembly demonstration animation above to observe the mechanical sequence of inserting permanent magnet cubes into 3D-printed ring housings, fastening retention lids, and stacking rings onto non-magnetic brass rods with precise axial spacing.*

  ##### Ring Housing & Lid Preparation
  1. **Print Components**: 3D print all ring housings (`Ring_842`, `Ring_0`, `Ring_1`, `Ring_10_front`, `Ring_10_back`, `Ring_945`, `Ring_1050`) and their respective lids (`Lid_Loose` and `Lid_tight`).
  2. **Install Heat Inserts**: Using a soldering iron with a heat-set insert tip, carefully install M3 brass heat-set inserts into the 4.2mm holes of each ring housing.
  3. **Insert Permanent Magnets**: Slide the 12x12x12mm N48/N52 neodymium magnet cubes into the designated pockets, strictly observing the Halbach rotation angles for each azimuth.
  4. **Fasten Lids**: Secure the lids with M3x8mm brass screws to physically retain the magnets against repulsive forces.

  ##### Mirrored Stacking on Brass Rods
  5. **Central Reference**: Position `Ring_842` at the geometric center ($z = 0$) along the 8 M4 brass rods (262mm length).
  6. **Mirrored Stacking**: Stack the rings symmetrically on either side of `Ring_842`:
     - Front section: `Ring_842` -> `Ring_1` -> `Ring_0` -> `Ring_10_front`
     - Back section: `Ring_842` -> `Ring_945` -> `Ring_1050` -> `Ring_10_back`
  7. **Orientation Rule**: Although ring positions are mirrored along $z$, **the direction they face is not**. All rings must be stacked with the magnet-facing side oriented in the exact same axial direction.
  8. **Lock Spacing**: Use M4 hex nuts on either side of each ring housing to precisely set axial ring-to-ring spacings as determined by the genetic optimization algorithm. Cap rod ends with M4 nylon washers and M4 dome nuts.
testing_guide: |
  #### B0 Field Mapping and Homogeneity Verification

  *Refer to the automated 3D field mapping robot video above to inspect how the 3-axis Cartesian gantry and Hall sensor probe conduct raster mapping across the magnet bore.*

  1. **Geometric Alignment**: Align the assembled Halbach magnet array on the non-magnetic scanner frame. Verify the 120mm bore clearance.
  2. **Robotic 3D Field Mapping**: Mount the Hall probe of the 3-axis Field Mapping Robot at the center of the bore. Run automated grid raster scans covering the target spherical DSV.
  3. **Homogeneity Computation**: Compute peak-to-peak and RMS homogeneity ($\Delta B_0 / B_0$ in ppm). The target field strength is ~50 mT ($47–52$ mT).
  4. **Passive Shimming**: Insert shim trays into the front and back slots of `Ring_10` with custom small magnet cartridges to cancel residual low-order spherical harmonics ($Z_1, X, Y, Z_2$).
---
## Overview

The **120mm Bore Halbach Magnet Array** is the primary magnetic field ($B_0$) source of the IMAGINE rat/preclinical MRI scanner. It produces a transverse static field of approximately 50 mT with high spatial homogeneity across the central volume.

<p align="center">
  <img src="/IMAGINE/images/imagine_magnet_assembly.png" alt="120mm Preclinical Halbach Magnet Array 3D CAD Assembly" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 16px rgba(0,0,0,0.25);" />
</p>

The array consists of stacked discrete rings housing 12×12×12 mm NdFeB permanent magnets. The ring positions, magnet orientations, and inter-ring spacings are optimized via genetic algorithms to maximize field uniformity while preserving an ample 120 mm internal clear bore for preclinical animal imaging, RF coils, and gradient inserts.

### Structural Architecture

- **Central Ring (Ring 842)**: Sits at the axial midpoint and establishes the baseline field.
- **Mirrored Stacking**: Rings are positioned symmetrically around Ring 842 along 8 non-magnetic M4 brass rods (262 mm length), secured by brass hex nuts and finished with dome nuts.
- **Passive Shimming**: Ring 10 front and Ring 10 back feature integrated mounting slots for 16 passive shim trays, enabling fine-tuning of the $B_0$ homogeneity.

### Design Documentation
- Full assembly guide and parts: [Part and build description.md](../../Hardware/Halbach%20Array/Part%20and%20build%20description.md)
- Optimization theory: [How to design magnet rings using genetic algorithms.md](../../Hardware/Halbach%20Array/How%20to%20design%20magnet%20rings%20using%20genetic%20algorithms.md)

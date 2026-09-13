---
layout: component
title: "Gradient Coils (CAD & Winding)"
scanner_id: imagine
category: "gradient"
description: "Spatially encodes the MR signals using 3D-printed cylindrical formers with AWG copper wire wound in computer-optimized grooves based on the Discrete Wire Method."
downloads:
  - name: "X Gradient Coil Former STL"
    path: "/Hardware/Gradients/CAD/X_Gradient_Coil_Former_Rat_Scanner.stl"
  - name: "Y Gradient Coil Former STL"
    path: "/Hardware/Gradients/CAD/Y_Gradient_Coil_Former_Rat_Scanner.stl"
  - name: "Z Gradient Coil Former STL"
    path: "/Hardware/Gradients/CAD/Z_Gradient_Coil_Former_Rat_Scanner.stl"
  - name: "Gradients CAD Documentation"
    path: "/Hardware/Gradients/CAD/README.md"
bom:
  - item: "X Gradient Former (3D Printed, Bambu PLA Basic Light Green)"
    qty: "90.38 g"
    price: "$2.26 CAD"
    link: "https://ca.store.bambulab.com/products/pla-basic-filament"
  - item: "Y Gradient Former (3D Printed, Bambu PLA Basic)"
    qty: "118.9 g"
    price: "$2.97 CAD"
    link: "https://ca.store.bambulab.com/products/pla-basic-filament"
  - item: "Z Gradient Former (3D Printed, Bambu PLA Basic)"
    qty: "99.7 g"
    price: "$2.50 CAD"
    link: "https://ca.store.bambulab.com/products/pla-basic-filament"
  - item: "Enamelled Copper Wire for X Gradient (AWG)"
    qty: "350 inches"
    price: "$4.86 CAD"
  - item: "Enamelled Copper Wire for Y Gradient (AWG)"
    qty: "350 inches"
    price: "$4.86 CAD"
  - item: "Enamelled Copper Wire for Z Gradient (AWG)"
    qty: "350 inches"
    price: "$4.86 CAD"
  - item: "Gradient Splice Connectors (18-22 AWG crimp, WM13851-ND)"
    qty: 10
    price: "$1.44 CAD"
    link: "https://www.digikey.ca/en/products/detail/molex/0192150009/2436407"
  - item: "Kapton Insulating Tape (10mm)"
    qty: 3
    price: "$11.96 CAD"
assembly_guide: |
  #### AutoCAD CAD Design & 3D Fabrication Procedure

  The complete manufacturing workflow for the gradient coil formers follows a four-phase procedure in Autodesk AutoCAD and FDM 3D printing:

  ##### Phase 1: Coordinate Import and Path Creation
  1. **Data Preparation**: Extract the optimized $x, y, z$ wire coordinates from the optimization script into CSV format. Ensure coordinates for each quadrant are formatted separately.
  2. **Coordinate Import**: Use the `LINE` command in AutoCAD to import the wire track coordinates and visualize each quadrant.
  3. **Spiral Construction**: Trim and connect the segments to form continuous spirals for each quadrant. Ensure current direction in adjacent quadrants is opposite to yield the gradient field. Define distinct input and output ports for each quadrant.
  4. **Path Integration**: Join individual lines within each quadrant using `PEDIT` / `JOIN` to form a single continuous `3D POLYLINE`.

  ##### Phase 2: 3D Modeling and Sweeping
  5. **Workspace Setup**: Switch AutoCAD workspace to **3D Modelling** and change viewport to a 3D isometric view.
  6. **Profile Selection**: Draw a circular profile with a diameter matching the wire gauge (including insulation), centered exactly on the starting port of each quadrant.
  7. **Sweep Operation**: Execute the `SWEEP` command. Select the circular profile and set the continuous 3D polyline as the sweeping path.
  8. **Visual Verification**: Switch to multiple viewports (Top, Side, Front) in Realistic Visual Style to verify wire groove spacing and clearances.

  ##### Phase 3: Cylinder and Groove Construction
  9. **Base Geometry**: Draw a concentric circle at the origin $(0, 0)$ matching the outer radius of the cylindrical gradient former.
  10. **Wall Thickness**: Offset this circle inward by 3 mm to form the inner cylinder wall.
  11. **Extrusion**: Extrude the concentric profile to half the coil former length ($L/2$). Draw and extrude the remaining half in the opposite direction.
  12. **Boolean Operations**: Execute `UNION` to merge the half-cylinders into one solid former. Merge the four quadrant wire sweeps into a single solid using `UNION`.
  13. **Groove Creation**: Execute `SUBTRACT` to remove the swept coil paths from the cylinder former, creating the precise wire-winding grooves.

  ##### Phase 4: Prototyping, Winding, and Assembly
  14. **STL Export**: Export the model using `STLOUT` for 3D printing.
  15. **3D Printing**: Print using PETG or PLA with 100% concentric infill to ensure mechanical rigidity and heat resistance.
  16. **Wire Winding**: Carefully press and wind the enamelled AWG copper wire into the manufactured grooves. Secure windings with Kapton tape and epoxy potting.
testing_guide: |
  #### Electromagnetic Simulation and Verification
  1. **DC Resistance & Inductance Measurement**: Measure DC resistance ($R$) and self-inductance ($L$) for each coil channel ($G_x$, $G_y$, $G_z$) using an LCR meter at 1 kHz and 10 kHz. Confirm zero inter-axis shorts.
  2. **Field Profile Verification (Simulation vs. Measurement)**: Compare measured magnetic field gradients against CST Studio Suite electromagnetic simulation predictions.
  3. **Gradient Efficiency ($T/m/A$)**: Determine gradient coil efficiency by driving calibrated test currents (1–5 A) and recording field variation with a Hall magnetometer along each spatial axis.
  4. **Thermal Dissipation Test**: Run continuous gradient pulses mimicking echo planar imaging (EPI) or fast spin echo (FSE) duty cycles. Verify thermal equilibrium remains well within former material limits (< 50 °C).
---
## Overview

The **Gradient Coils** provide spatial encoding in the three orthogonal directions ($X$, $Y$, and $Z$) for the IMAGINE low-field rat/preclinical MRI scanner. The coils are wound on concentric cylindrical former surfaces with precisely manufactured grooves produced via high-resolution 3D printing.

The wire trajectories are optimized using the **Discrete Wire Method** to produce highly linear magnetic field gradients over the target spherical diameter volume (DSV), minimizing unwanted concomitant fields and heat dissipation.

### Design and Optimization Reference

The scientific methodology, boundary conditions, and genetic/boundary-element optimization for these gradient coils are published in:

> **Kassahun, H.B., Nayebare, M., Machtelinckx, T., Yazdanbakhsh, P., Obungoloch, J., Du Plessis, S. and Anazodo, U.**, 2025, July. *Design and Optimization of Gradient Coils for Low-field Halbach Array Scanners Using the Discrete Wire Method*. In *2025 47th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC)* (pp. 1–6). IEEE.

### CAD Model Files

STL files for manufacturing the X, Y, and Z gradient coil formers are available directly in the repository:
- [X Gradient Coil Former STL](../../Hardware/Gradients/CAD/X_Gradient_Coil_Former_Rat_Scanner.stl)
- [Y Gradient Coil Former STL](../../Hardware/Gradients/CAD/Y_Gradient_Coil_Former_Rat_Scanner.stl)
- [Z Gradient Coil Former STL](../../Hardware/Gradients/CAD/Z_Gradient_Coil_Former_Rat_Scanner.stl)
- [Design Guide Markdown](../../Hardware/Gradients/Gradient_Design.md)

---
layout: component
title: "Gradient Coils (CAD & Winding)"
scanner_id: imagine
category: "gradient"
description: "Spatially encodes the MR signals using 3D-printed formers with AWG copper wire wound in computer-optimized grooves."
downloads:
  - name: "Gradient Coil CAD Files (AutoCAD)"
    path: "/Hardware/Gradients/CAD files"
bom:
  - item: "AWG copper wire (American Wire Gauge)"
    qty: "Varies"
    price: "$20.00"
  - item: "3D Printed Former (PETG/PLA)"
    qty: 1
    price: "$30.00"
  - item: "Gradient Connectors (Splices)"
    qty: 1
    price: "$15.00"
assembly_guide: |
  #### AutoCAD CAD Design & Print
  The steps for the CAD design of the gradient winding grooves in AutoCAD:
  1. **Coordinate Import**: Copy x, y, z coordinates from simulation outputs into Excel and save as a CSV. Use the `LINE` command in AutoCAD to import and visualize each quadrant.
  2. **Spiral Construction**: Connect lines to form spirals, ensuring the current direction in adjacent quadrants is opposite. Each quadrant must have two distinct ports (input/output). Join lines into a single continuous `3D POLYLINE`.
  3. **3D Sweeping**: Draw a circle equal to the wire width. Centering it on one of the ports, run `SWEEP` along the polyline path.
  4. **Groove Creation**: Draw concentric circles representing the former cylinder walls. Extrude them to the required height ($L/2$). Use `UNION` to combine cylinder half sections. Merge all four coil quadrant sweeps using `UNION`. Finally, execute `SUBTRACT` to subtract the coil quadrants from the cylinder, creating the winding grooves.
  5. **Fabrication**: Export the STL file using `STLOUT`. 3D print the former and wind the AWG copper wires into the manufactured grooves.
testing_guide: |
  #### Electromagnetic Simulation and Verification
  1. Measure coil resistance and inductance using a multimeter/LCR meter. Verify there are no short circuits between the X, Y, Z channels or the system frame.
  2. Save the final CAD coordinates and simulate the expected magnetic field profile ($G_x$, $G_y$, $G_z$) using CST Studio Suite or EM simulation packages.
  3. Verify gradient efficiency (field gradient amplitude per unit current: T/m/A).
  4. Run testing currents through the coils and measure heat dissipation over time.
---
The **Gradient Coils** provide spatial encoding in the three orthogonal directions ($X$, $Y$, and $Z$). The coils are wound on cylindrical former surfaces, with grooves manufactured directly by 3D printing. The wire patterns are optimized using the **Discrete Wire Method** to produce highly linear gradients over the target field of view (FOV).

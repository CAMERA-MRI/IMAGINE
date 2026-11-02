# ERNIE MRI Phantoms: Design and Fabrication

## Overview

This folder contains the CAD designs and fabrication specifications for two cylindrical phantoms developed for the IMAGINE ERNIE low-field MRI scanner. The designs include a single-compartment cylindrical phantom and a two-compartment cylindrical phantom. Both phantoms are designed for 3D printing and filled with olive oil to demonstrate MRI signal acquisition and image formation.

## 1. Single-Compartment Cylindrical Phantom

The single-compartment phantom consists of a cylindrical container with an upper cover and a bottom layer, each 3 mm thick. The phantom is designed to hold olive oil for MRI imaging experiments.

### Design Specifications

| Parameter | Specification |
|---|---|
| Phantom type | Single-compartment cylinder |
| Outer radius | 19.76 mm |
| Inner radius | 17.26 mm |
| Total height | 50 mm |
| Fillable height | 44 mm |
| Cylindrical wall thickness | 2.50 mm |
| Upper cover thickness | 3 mm |
| Bottom layer thickness | 3 mm |
| Filling-hole radius | 1.5 mm |
| Calculated filling volume | 41.18 mL |
| Filling material | Olive oil |

### CAD Design and Fabrication

1. Create two concentric circles with outer and inner radii of 19.76 mm and 17.26 mm, respectively.
2. Extrude the outer cylindrical geometry to a total height of 50 mm.
3. Create the internal cavity with a radius of 17.26 mm and a fillable height of 44 mm.
4. Maintain a 3 mm bottom layer and a 3 mm upper cover.
5. Create a filling hole with a radius of 1.5 mm in the upper cover.
6. Export the completed CAD design as an STL file for 3D printing.
7. Fabricate the components using a suitable 3D printing material and assemble the phantom.

### Filling Volume

The theoretical filling volume is calculated using:

**V = πr²h**

where:
- r = 17.26 mm (inner radius)
- h = 44 mm (fillable height)

The calculated volume is approximately **41.18 mL**.

## 2. Two-Compartment Cylindrical Phantom

The two-compartment phantom consists of two identical cylindrical cavities positioned symmetrically inside a larger cylindrical housing. The compartments are designed to be filled with olive oil and used to evaluate MRI image formation and spatial separation of two distinct regions.

### Design Specifications

| Parameter | Specification |
|---|---|
| Phantom type | Two-compartment cylinder |
| Outer cylinder radius | 19.76 mm |
| Outer cylinder centre | (0, 0, 0) mm |
| Total phantom height | 50 mm |
| Fillable height | 44 mm |
| Upper cover thickness | 3 mm |
| Bottom layer thickness | 3 mm |
| First compartment centre | (9.63, 0, 0) mm |
| Second compartment centre | (-9.63, 0, 0) mm |
| Radius of each compartment | 8.63 mm |
| Separation between compartments | 2 mm |
| Number of filling holes | 2 |
| Radius of each filling hole | 1.5 mm |
| Total calculated filling volume | 20.59 mL |
| Filling material | Olive oil |

### CAD Design and Fabrication

1. Create the outer cylindrical geometry with a radius of 19.76 mm, centred at the origin (0, 0, 0).
2. Create two internal circular cavities with radii of 8.63 mm.
3. Position the first cavity at (9.63, 0, 0) mm and the second at (-9.63, 0, 0) mm.
4. Extrude the phantom body to a total height of 50 mm.
5. Maintain a fillable cavity height of 44 mm, with 3 mm thick upper and bottom layers.
6. Create two filling holes, each with a radius of 1.5 mm, in the upper cover.
7. Export the completed CAD components as STL files for 3D printing.
8. Fabricate and assemble the phantom components.

### Filling Volume

The theoretical filling volume is calculated as:

**V = 2πr²h**

where:
- r = 8.63 mm (radius of each compartment)
- h = 44 mm (fillable height)
- Number of compartments = 2

The calculated total filling volume is approximately **20.59 mL**, equivalent to approximately 10.30 mL per compartment.

## 3. Phantom Filling and MRI Imaging

Olive oil is used as the filling material for both phantom designs.

### Filling Procedure

1. Inspect the 3D-printed phantoms for defects or leakage.
2. Fill the internal cavities with olive oil through the designated filling holes.
3. Minimize trapped air bubbles to reduce image artifacts.
4. Seal the filling holes securely to prevent leakage.
5. Place the filled phantom inside the RF coil of the ERNIE low-field MRI scanner.
6. Position the phantom within the scanner's imaging region.
7. Acquire MRI signals and images using the appropriate imaging sequence.

## 4. CAD Files

The CAD designs and STL files for the single-compartment and two-compartment phantoms are provided in this folder. These files can be used to reproduce, fabricate, or modify the phantoms for similar low-field MRI experiments.

### Notes

- All geometric dimensions are specified in millimetres (mm).
- The calculated volumes represent ideal cylindrical cavities and may differ slightly from actual filling volumes due to manufacturing tolerances and additional CAD features.
- The outer diameter of both phantom designs is 39.52 mm.
- Verify dimensional accuracy, cover fit, and liquid tightness before conducting MRI experiments.
- The exact positions of filling holes and the cover assembly should follow the provided CAD files.

ERNIE MRI Phantoms: Single-Cylinder and Two-Compartment Designs
Overview
This directory contains the CAD designs and fabrication specifications for two cylindrical imaging phantoms developed for the IMAGINE ERNIE low-field MRI scanner:
1. A single-compartment cylindrical phantom.
2. A two-compartment cylindrical phantom.
The phantoms are designed for 3D printing and are filled with olive oil for MRI experiments. All geometric dimensions are in millimetres (mm). The coordinates provided below refer to the cross-sectional (XY) CAD plane.
1. Single-Compartment Cylindrical Phantom
This phantom has one cylindrical cavity within a larger cylindrical housing, with 3 mm thick bottom and top layers.
Parameter	Specification
Phantom geometry	Single cylindrical compartment
Outer radius	19.76 mm
Inner (cavity) radius	17.26 mm
Radial wall thickness	2.50 mm
Total height	50 mm
Fillable cavity height	44 mm
Bottom layer thickness	3 mm
Upper cover thickness	3 mm
Filling-hole radius	1.50 mm
Filling material	Olive oil
Ideal cylindrical cavity volume	41.18 mL
Previously reported volume	54 mL — see verification note below


Volume calculation: Using the inner radius and fillable height, the ideal cavity volume is

V = π × (17.26 mm)² × 44 mm / 1000 = 41.18 mL.
Volume verification required: The previously reported 54 mL corresponds approximately to a 19.76 mm cavity radius and 44 mm fillable height, rather than to the corrected 17.26 mm inner radius. Verify the CAD geometry or experimentally measured fill volume before reporting 54 mL as the capacity of this phantom.

2. Two-Compartment Cylindrical Phantom
This phantom contains two equal cylindrical cavities positioned symmetrically along the X-axis within an outer cylindrical housing. Both compartments are filled with olive oil.
Parameter	Specification
Phantom geometry	Two cylindrical compartments
Outer housing radius	19.76 mm
Outer circle centre (XY plane)	(0, 0) mm
Total height	50 mm
Fillable cavity height	44 mm
Bottom layer thickness	3 mm
Upper cover thickness	3 mm
Centre of compartment 1 (XY plane)	(9.63, 0) mm
Centre of compartment 2 (XY plane)	(-9.63, 0) mm
Radius of each compartment	8.63 mm
Minimum wall thickness between compartments	2.00 mm
Number of filling holes	2
Radius of each filling hole	1.50 mm
Filling material	Olive oil
Ideal total cavity volume	20.59 mL (approximately 21 mL)


Volume calculation: For two equal cylindrical cavities,

V = 2 × π × (8.63 mm)² × 44 mm / 1000 = 20.59 mL.

The two cavity centres are 19.26 mm apart, giving a 2 mm separation between cavity edges (19.26 − 2 × 8.63 = 2.00 mm).
3. CAD Modelling and Fabrication
1. Create the housing: Model the outer cylinder at the specified radius and total height of 50 mm.
2. Define the cavities: Create one cavity with a 17.26 mm radius for the single-cylinder design, or two cavities with 8.63 mm radii at the specified XY centres for the two-compartment design.
3. Set the axial dimensions: Maintain a 44 mm fillable cavity height with 3 mm of material at the bottom and a 3 mm top cover. Use extrusion or subtraction operations consistent with the CAD assembly.
4. Add filling holes: Include the 1.5 mm radius filling hole (single-compartment design) or two 1.5 mm radius holes (two-compartment design). Follow the actual CAD model for hole placement and cover attachment.
5. Export for printing: Export the printable bodies and covers as STL files. Retain editable CAD source files where available.
6. Print and inspect: Print the parts, confirm dimensional fit and inspect the cavities for defects before filling.
Reproducibility note: Printer model, filament/resin, print orientation, layer height, wall/perimeter count, sealing method, and exact hole positions have not been specified here. Record these alongside the CAD files when the fabrication method is finalized.
4. Filling and MRI Preparation
1. Inspect each printed phantom and verify that its openings can be sealed.
2. Fill the cavity or cavities with olive oil, minimizing trapped air bubbles.
3. Secure the cover and seal the filling holes using a method compatible with the selected printing material and olive oil.
4. Check the assembly for leaks before placing it inside the ERNIE scanner.
5. Position the phantom inside the RF coil and perform MRI acquisition using the selected imaging sequence.
6. Record the actual fill volume and imaging parameters for reproducibility.
5. CAD Files
Store the 3D-printable STL files and editable CAD designs for both phantoms in the corresponding CAD directory. Use descriptive filenames to distinguish the single-compartment and two-compartment designs, including their covers if saved separately.

Before reproduction: Verify the single-compartment volume discrepancy and document the exact placement of the filling holes and cover-sealing mechanism in the released CAD designs.

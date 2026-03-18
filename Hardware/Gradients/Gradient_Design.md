# How to build your own MRI Gradients
## CAD Design
The steps for the CAD design and 3D printing of the gradient coils using Autodesk AutoCAD

**Phase 1: Coordinate Import and Path Creation**

1. Data Preparation: Copy the x, y, and z coordinates into Excel and save them as a CSV file. Ensure that coordinates for each quadrant are saved separately.
2. Coordinate Import: Use the LINE command in AutoCAD to import the coordinates and visualize each quadrant.
3. Spiral Construction: Trim and connect the lines to form a spiral for each quadrant. Ensure the current direction in adjacent quadrants is opposite. Each quadrant must have two distinct ports: one for input and one for output.
4. Path Integration: Join the individual lines within each quadrant to create a single, continuous 3D POLYLINE.

**Phase 2: 3D Modeling and Sweeping**

5. Workspace Setup: Switch the AutoCAD workspace to 3D Modelling and change the viewport to a 3D View.
6. Profile Selection: Draw a circle with a diameter equal to the wire width. Center this circle on one of the ports of each quadrant.
7. Sweep Operation: Execute the SWEEP command. Select the circle as the object to sweep, press Enter, and then select the 3D polyline (the wire path) as the sweeping path.
8. Visual Verification: Change the workspace to multiple viewports (Top, Side, and Front). In the Front view, click the "Home" (house) icon and change the Visual Style to Realistic. (Alternatively, select Realistic directly from the View section).
9. Display Reset: Revert the workspace to a single viewport.
10. Workspace Transition: Return to the Drafting and Annotation view.

**Phase 3: Cylinder and Groove Construction**

11. Base Geometry: Draw a circle at the center (0, 0) with a radius equal to the outer radius of the gradient coil.
12. Shelling: Offset this circle inward by 3mm to create an inscribed circle.
13. Initial Extrusion: Extrude these circles to half the total height of the gradient coil (L/2) to create a half-cylinder.
14. Secondary Geometry: Draw a second set of circles (using the same offsets from steps 11 and 12) at the center (0, 0), positioned at either the top or bottom face of the first cylinder.
15. Full Extrusion: Extrude these circles in the opposite direction (positive or negative Z) to complete the other half of the coil height.
16. Merging Cylinder: Use the UNION command to merge the two half-cylinders into one solid, full-length cylinder for the gradient coil former.
17. Merging Coil Paths: Use the UNION command to merge all four coil quadrants into a single object.
18. Groove Creation: Use the SUBTRACT command to remove the quadrant coil objects from the cylinder, thereby creating the winding grooves.

**Phase 4: Prototyping and Testing**

19. Export: Generate an STL file for 3D printing using the STLOUT command.
20. Fabrication: 3D print the former and carefully wind the AWG (American Wire Gauge) wires into the manufactured grooves.
21. Simulation: Save the quadrant geometries independently and test the coil performance using CST Studio Suite or another electromagnetic simulation package.


  
## Gradient Optimization 
The optimization details for the gradient coils are available in this paper: 
Kassahun, H.B., Nayebare, M., Machtelinckx, T., Yazdanbakhsh, P., Obungoloch, J., Du Plessis, S. and Anazodo, U., 2025, July. Design and Optimization of Gradient Coils for Low-field Halbach Array Scanners Using the Discrete Wire Method. In 2025, the 47th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC) (pp. 1-6). IEEE.

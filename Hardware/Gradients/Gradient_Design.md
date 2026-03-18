### How to build your own MRI Gradients
- CAD Design
Phase 1: Coordinate Import and Path Creation

Data Preparation: Copy the x, y, and z coordinates into Excel and save them as a CSV file. Ensure that coordinates for each quadrant are saved separately.

Coordinate Import: Use the LINE command in AutoCAD to import the coordinates and visualize each quadrant.

Spiral Construction: Trim and connect the lines to form a spiral for each quadrant. Ensure the current direction in adjacent quadrants is opposite. Each quadrant must have two distinct ports: one for input and one for output.

Path Integration: Join the individual lines within each quadrant to create a single, continuous 3D POLYLINE.

Phase 2: 3D Modeling and Sweeping

Workspace Setup: Switch the AutoCAD workspace to 3D Modeling and change the viewport to a 3D View.

Profile Selection: Draw a circle with a diameter equal to the wire width. Center this circle on one of the ports of each quadrant.

Sweep Operation: Execute the SWEEP command. Select the circle as the object to sweep, press Enter, and then select the 3D polyline (the wire path) as the sweeping path.

Visual Verification: Change the workspace to multiple viewports (Top, Side, and Front). In the Front view, click the "Home" (house) icon and change the Visual Style to Realistic. (Alternatively, select Realistic directly from the View section).

Display Reset: Revert the workspace to a single viewport.

Workspace Transition: Return to the Drafting and Annotation view.

Phase 3: Cylinder and Groove Construction

Base Geometry: Draw a circle at center $(0, 0)$ with a radius equal to the outer radius of the gradient coil.

Shelling: Offset this circle inward by $0.002\text{m}$ ($2\text{mm}$) to create an inscribed circle.

Initial Extrusion: Extrude these circles to half the total height of the gradient coil ($L/2$) to create a half-cylinder.

Secondary Geometry: Draw a second set of circles (using the same offsets from steps 11 and 12) at center $(0, 0)$, positioned at either the top or bottom face of the first cylinder.

Full Extrusion: Extrude these circles in the opposite direction (positive or negative $Z$) to complete the other half of the coil height.

Merging Cylinder: Use the UNION command to merge the two half-cylinders into one solid, full-length cylinder for the gradient coil former.

Merging Coil Paths: Use the UNION command to merge all four coil quadrants into a single object.

Groove Creation: Use the SUBTRACT command to remove the quadrant coil objects from the cylinder, thereby creating the winding grooves.

Phase 4: Prototyping and Testing

Export: Generate an STL file for 3D printing using the STLOUT command.

Fabrication: 3D print the former and carefully wind the AWG (American Wire Gauge) wires into the manufactured grooves.

Simulation: Save the quadrant geometries independently and test the coil performance using CST Studio Suite or another electromagnetic simulation package.

Electronic Integration: Connect the physical coil to the gradient amplifiers.

System Testing: Assemble the coil with the other MRI components and conduct a full-system performance test.
  
- Gradient Optimization 

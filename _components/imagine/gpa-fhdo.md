---
layout: component
title: "GPA-FHDO Power Amplifier"
scanner_id: imagine
category: "gradient"
description: "The Gradient Power Amplifier (GPA) design from FHDO Dortmund, delivering controlled high-current drives to the gradient coils."
bom:
  - item: "Schaffner FN7563-63-M6 Filter Capacitor"
    qty: 3
    price: "Included in GPA budget"
  - item: "High-Current DC Power Supply for FHDO"
    qty: 1
    price: "Varies"
  - item: "High-current output terminal connectors"
    qty: 6
    price: "$10.00"
assembly_guide: |
  #### GPA Installation and Integration
  1. Mount the GPA-FHDO boards on a secure chassis with passive/active heatsink cooling.
  2. Setup the high-current DC power supply, ensuring proper voltage and current limits are configured.
  3. Wire the outputs of the RedPitaya GPA adapter to the GPA-FHDO input channels.
  4. Connect the output of the GPA-FHDO to the low-pass filter circuit.
testing_guide: |
  #### GPA Calibration & Protection Test
  1. Power up the GPA board and verify the bias currents and voltage references.
  2. With dummy load resistors (equivalent to gradient coil resistance/inductance), apply test pulses (e.g. 1A, 2A steps).
  3. Monitor current waveforms on an oscilloscope using a current probe. Verify there is no waveform distortion or excessive ringing.
  4. Verify that thermal shutdown and over-current protection trigger at correct thresholds.
---
The **GPA-FHDO** is a specialized Gradient Power Amplifier design developed by the Fachhochschule Dortmund (FHDO). Unlike traditional audio amplifiers, GPAs are designed to drive highly inductive loads (like gradient coils) with fast rise times and stable, controlled currents, which is essential for accurate spatial encoding in MR imaging.

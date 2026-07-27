---
layout: component
title: "Gradient Low-Pass Filter"
scanner_id: imagine
category: "gradient"
description: "A high-performance filter network designed to suppress high-frequency noise from the GPA outputs, preventing RF interference in the scanner bore."
bom:
  - item: "Schaffner FN7563-63-M6 Filter Capacitor"
    qty: 3
    price: "Included in GPA budget"
  - item: "Shielding copper enclosure"
    qty: 1
    price: "Custom"
  - item: "Low-resistance grounding cables"
    qty: 1
    price: "Custom"
assembly_guide: |
  #### Filter Fabrication
  1. Mount the Schaffner FN7563 filter capacitors inside a grounded copper shielding box.
  2. Wire the inputs of the filters to the GPA output lines.
  3. Connect the outputs of the filters to the gradient coil splices.
  4. Ensure a solid, low-resistance connection between the copper box and the main system ground.
testing_guide: |
  #### Filter Performance Verification
  1. Use a network analyzer (VNA) or oscilloscope to perform a frequency sweep from 1 kHz to 10 MHz.
  2. Verify that the filter provides strong attenuation at the Larmor frequency range (~2 MHz).
  3. Measure the DC resistance of the filter to ensure power losses are minimal.
---
The **Gradient Low-Pass Filter** prevents high-frequency switching noise from the GPA-FHDO from radiating into the scanner bore. Since the Larmor frequency is close to 2 MHz, any high-frequency switching noise on the gradient lines can directly couple into the RF coil and saturate the LNA, causing severe image artifacts.

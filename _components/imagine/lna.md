---
layout: component
title: "Low Noise Amplifier (LNA)"
scanner_id: imagine
category: "rf"
description: "Amplifies the microvolt-level MRI echo signals directly from the Tx/Rx switch, establishing the system's receiver noise figure."
bom:
  - item: "Low Noise Amplifier (LNA) Module"
    qty: 1
    price: "Included in budget"
  - item: "Shielding copper/aluminum enclosure box for LNA"
    qty: 1
    price: "Custom"
  - item: "LNA DC Power Supply (KD3005D)"
    qty: 1
    price: "$129.47"
    link: "https://www.digikey.ca/en/products/detail/sra-soldering-products/KD3005D/10709902"
assembly_guide: |
  #### LNA Mounting & Grounding
  1. Mount the LNA module inside a fully shielded copper box.
  2. Ground the box chassis to the main RF shield of the scanner.
  3. Wire the DC power input through a feedthrough capacitor to block power line noise.
  4. Connect the output of the Tx/Rx Switch to the LNA input using short, double-shielded RG-223 coaxial cables.
testing_guide: |
  #### LNA Gain & Noise Floor Test
  1. Connect a 50 Ohm dummy resistor to the LNA input.
  2. Measure the LNA output on a spectrum analyzer to check the noise floor.
  3. Apply a weak reference signal (e.g. -80 dBm at 2 MHz) and verify LNA gain (expected: ~20-30 dB) and stability.
  4. Verify that the LNA does not oscillate under different loading conditions.
---
The **Low Noise Amplifier (LNA)** is the first stage in the MRI receiver chain. Because the nuclear magnetic resonance (NMR) signal from a 50 mT scanner is in the microvolt range, the LNA must provide high gain with extremely low added noise (low Noise Figure) to prevent drowning the signal in the thermal noise of the electronics.

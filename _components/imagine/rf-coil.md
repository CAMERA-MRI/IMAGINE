---
layout: component
title: "RF Coil & Tuning and Matching"
scanner_id: imagine
category: "rf"
description: "A 27-turn solenoid radiofrequency coil tuned to the Larmor frequency (2.035 - 2.1 MHz) with integrated tuning and matching capacitors."
downloads:
  - name: "RF Coil Holder 3D Model (STL)"
    path: "/Hardware/RF coil/RF COIL with 27 turns, inner diameter 58.8mm.stl"
  - name: "RF Coil CAD Drawing (DWG)"
    path: "/Hardware/RF coil/RF COIL with 27 turns, inner diameter 58.8mm.dwg"
bom:
  - item: "3D Printed Coil Holder (PETG/PLA)"
    qty: 1
    price: "$10.00"
  - item: "Tuning Capacitor 330pF (High-Q, Passive Plus)"
    qty: 1
    price: "$32.69"
    link: "https://www.digikey.ca/en/products/detail/passive-plus/PPZN30100/19235833"
  - item: "Variable Capacitors (GKG60015, 60pF)"
    qty: 10
    price: "$12.00"
    link: "https://www.digikey.ca/en/products/detail/ew-electronics/GKG60015/11689267"
  - item: "nanoVNA Vector Network Analyzer"
    qty: 1
    price: "$79.99"
    link: "https://www.amazon.ca/Seesii-Analyzer-10KHz-1-5GHz-Measuring-Parameters/dp/B08132DJLS"
  - item: "Enclosure Box for Tuning & Matching Circuit"
    qty: 1
    price: "Custom"
  - item: "SMA panel mount sockets"
    qty: 2
    price: "$10.00"
assembly_guide: |
  #### Coil Winding & Assembly
  1. Print the RF coil holder (inner diameter 58mm, outer diameter 63mm).
  2. Wind exactly 27 turns of 1.65mm thick copper wire into the grooved tracks of the 3D printed holder.
  3. Ensure a winding length of 117mm and pitch of 4.33mm.
  4. Solder the coil ends to the tuning and matching board inside the shielded tuning enclosure.
  5. Setup the capacitors:
     - **Tuning Capacitance**: 330pF + 24pF + 25pF variable.
     - **Matching Capacitance**: 47pF + 18pF.
testing_guide: |
  #### Tuning and Impedance Matching Guide
  1. **Integration**: Place the RF coil inside the MRI scanner, complete with gradient coils and the RF shield.
  2. **VNA Connection**: Connect the coil to the nanoVNA (calibrated at the center frequency).
  3. **Tuning**: Observe the $S_{11}$ reflection dip on the VNA screen. Adjust the capacitors on the tuning side to align the center frequency to exactly 2.035 MHz (or 2.1 MHz depending on your magnet's B0 field strength).
  4. **Quality Factor (Q)**: Once tuned, measure the quality factor loaded (with sample) and unloaded (empty bore). The Q-value should be greater than 1.
  5. **Matching**: Adjust the matching channel capacitors until the impedance is close to 50 Ohms on the Smith chart and the reflected power ($S_{11}$ dip) is closer to -30.7 dB or lower (ideally approaching -50 dB).
---
The **RF Coil** transmits the excitation pulse and receives the echo signal. It is built as a solenoid coil wound on a 3D-printed former. Since low-field MRI signals are weak, the RF coil must be tuned to the exact Larmor frequency of the system and matched to 50 Ohms to ensure maximum power transfer and high signal-to-noise ratio (SNR).

---
layout: component
title: "Tx/Rx Switch"
scanner_id: imagine
category: "rf"
description: "A passive/active transmit-receive switch that isolates the sensitive Low Noise Amplifier (LNA) from the high-voltage transmit pulses."
downloads:
  - name: "OSII Passive TR Switch Repository"
    path: "https://gitlab.com/osii/rf-system/tr-switches/passive-tr-switch"
bom:
  - item: "BAT6804WH6327XTSA1 Diodes"
    qty: 20
    price: "$7.14 (pack)"
    link: "https://www.digikey.ca/en/products/detail/infineon-technologies/BAT6804WH6327XTSA1/2337549"
  - item: "Inductors (4.0uH, Coilcraft SER2014-402MLD)"
    qty: 4
    price: "$42.55"
    link: "https://www.digikey.ca/en/products/detail/coilcraft/SER2014-402MLD/21381062"
  - item: "Capacitors (820pF, Kemet C2220C821JZGACTU)"
    qty: 6
    price: "$42.54"
    link: "https://www.digikey.ca/en/products/detail/kemet/C2220C821JZGACTU/1086644"
  - item: "SMA PCB Right Angle Jacks (WR-SMA)"
    qty: 3
    price: "$28.80"
    link: "https://www.digikey.ca/en/products/detail/w%C3%BCrth-elektronik/60311002114501/10106987"
  - item: "Aluminum Box for Switch Enclosure"
    qty: 1
    price: "$19.86"
    link: "https://www.digikey.ca/en/products/detail/bud-industries/CU-234/387028"
  - item: "Expensive Diode Passive Switch (UMX9989AP)"
    qty: 1
    price: "$45.77"
    link: "https://www.digikey.ca/en/products/detail/microchip-technology/UMX9989AP/13179363"
assembly_guide: |
  #### Switch Assembly & Solder
  1. Position the passive switch PCB (from the Open Source Imaging Initiative design) on your workbench.
  2. Solder the surface-mount BAT6804 diodes and the passive capacitors (820pF).
  3. Solder the high-power Coilcraft inductors and the right-angle WR-SMA connectors.
  4. Solder the high-speed passive switch diode (UMX9989AP).
  5. Mount the board inside the Bud aluminum box, connecting the SMA ground pins securely to the chassis.
testing_guide: |
  #### VNA Reflection & Transmission Calibration
  Using a VNA calibrated to the magnet's working Larmor frequency, measure the reflection (S11/S22) and transmission (S21/S12) coefficients in both **Transmit Mode** (Switch ON) and **Receive Mode** (Switch OFF). All ports not under test must be terminated with a 50 Ohm load.
  
  Verify your switch measurements match the reference performance table:
  
  | Measurement Type | Signal Source | Reference (dB) | Your Switch (dB) |
  | :--- | :--- | :--- | :--- |
  | **S11 (Reflection)** | | | |
  | Transmit Mode (Switch ON) | Tx | -23.0 | |
  | Transmit Mode (Switch ON) | Coil | -21.2 | |
  | Receive Mode (Switch OFF) | Coil | -22.9 | |
  | Receive Mode (Switch OFF) | Rx | -22.4 | |
  | **S21 (Transmission)** | | | |
  | Transmit Mode (Switch ON) | Tx - Coil | -0.24 | |
  | Transmit Mode (Switch ON) | Tx - Rx | -39.5 | |
  | Transmit Mode (Switch ON) | Coil - Rx | -40.4 | |
  | Receive Mode (Switch OFF) | Tx - Coil | -53.4 | |
  | Receive Mode (Switch OFF) | Tx - Rx | -50.0 | |
  | Receive Mode (Switch OFF) | Coil - Rx | -0.21 | |
---
The **Tx/Rx Switch** acts as a fast RF router. During transmission, it blocks the high-voltage RF pulses (which could destroy the sensitive LNA receiver) and directs them straight to the RF Coil. During reception, it acts as a low-loss path to route the extremely weak MRI echo signals from the RF Coil to the LNA. The passive switch design is based on the **Open Source Imaging Initiative (OSI²)** passive TR switch reference.

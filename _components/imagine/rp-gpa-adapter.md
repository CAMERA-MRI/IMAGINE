---
layout: component
title: "RedPitaya to GPA Adapter Board"
scanner_id: imagine
category: "gradient"
description: "Custom adapter interface board matching the RedPitaya analog and digital outputs to the inputs of the GPA-FHDO amplifier."
bom:
  - item: "Custom PCB for Red Pitaya to GPA-FHDO Adapter"
    qty: 1
    price: "Included in budget"
  - item: "Schmitt Trigger ICs (SN74LVC1G17DBVR)"
    qty: 10
    price: "$10.60"
    link: "https://www.digikey.ca/en/products/detail/texas-instruments/SN74LVC1G17DBVR/389051"
  - item: "IDC Female Extension Connector (SFH11-PBPC-D13-ST-BK)"
    qty: 4
    price: "$7.64"
    link: "https://www.digikey.ca/en/products/detail/sullins-connector-solutions/SFH11-PBPC-D13-ST-BK/1990091"
  - item: "Pin Header Male (WR-BHD, 61304011121)"
    qty: 3
    price: "$6.03"
    link: "https://www.digikey.ca/en/products/detail/w%C3%BCrth-elektronik/61304011121/4846884"
  - item: "Dual Row Pin Header Male (PR20203VBDN)"
    qty: 10
    price: "$10.10"
    link: "https://www.digikey.ca/en/products/detail/metz-connect-usa-inc/PR20203VBDN/12342894"
  - item: "Capacitor (CL21A106KAYNNNE, 10uF)"
    qty: 10
    price: "$1.22"
    link: "https://www.digikey.ca/en/products/detail/samsung-electro-mechanics/CL21A106KAYNNNE/3888549"
  - item: "Pin headers female (various)"
    qty: 30
    price: "$10.47"
assembly_guide: |
  #### PCB Assembly & Soldering
  1. Position the custom adapter PCB on a soldering stand.
  2. Solder the surface-mount Schmitt trigger ICs (SN74LVC1G17DBVR) first, checking pin alignment.
  3. Solder the passives: capacitors (10uF) and resistors.
  4. Solder the IDC connectors and male/female pin headers.
  5. Inspect all solder joint connections under a microscope to ensure no solder bridges.
testing_guide: |
  #### Connectivity & Level Shifting Test
  1. Mount the adapter board onto the Red Pitaya GPIO pins.
  2. Apply a 3.3V power supply.
  3. Generate a digital pulse sequence from the Red Pitaya.
  4. Verify that the output pulses from the Schmitt triggers are clean, level-shifted if needed, and noise-free using an oscilloscope.
---
The **RedPitaya GPA Adapter** is an interface board that bridges the Red Pitaya console board and the Gradient Power Amplifiers. It provides buffering, signal isolation, and clean level shifting via Schmitt triggers, protecting the console from currents and ensuring noise-free gradient control signals.

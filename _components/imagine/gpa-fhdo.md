---
layout: component
title: "GPA-FHDO Power Amplifier"
scanner_id: imagine
category: "gradient"
description: "The open-source 4-channel Gradient Power Amplifier (GPA-FHDO) from Fachhochschule Dortmund, adapted to drive the X, Y, and Z gradient coils in the IMAGINE scanner."
downloads:
  - name: "IMAGINE GPA Bill of Materials (Excel)"
    path: "/Hardware/Gradient_Power_Amplifier/IMAGINE_GPA_BOM.xlsx"
  - name: "IMAGINE GPA Bill of Materials (CSV)"
    path: "/Hardware/Gradient_Power_Amplifier/IMAGINE_GPA_BOM.csv"
  - name: "GPA-FHDO Schematic Diagram (SVG)"
    path: "/images/gradients1.svg"
bom:
  - item: "OPA549 Power Operational Amplifier"
    part_number: "OPA549T-ND"
    qty: 8
    price: "$430.80 CAD"
    link: "https://www.digikey.ca/en/products/detail/texas-instruments/OPA549T/379854"
  - item: "TekPower TP1560E Switching DC Power Supply (15V, 60A)"
    part_number: "TP1560E"
    qty: 1
    price: "$623.09 CAD"
    link: "https://www.amazon.ca/TekPower-TP1560E-Switching-Power-Supply/dp/B073XJBN4F"
  - item: "ADS8684 4-Channel 16-Bit ADC"
    part_number: "ADS8684IDBTR"
    qty: 1
    price: "$23.11 CAD"
    link: "https://www.digikey.ca/en/products/detail/texas-instruments/ADS8684IDBTR/4988771"
  - item: "DAC80504 4-Channel 16-Bit Voltage Output DAC"
    part_number: "296-51043-1-ND / DAC80504RTER"
    qty: 1
    price: "$20.93 CAD"
    link: "https://www.digikey.ca/en/products/detail/texas-instruments/DAC80504RTER/10134444"
  - item: "ADUM4150 High-Speed SPI Isolator"
    part_number: "505-ADUM4150BRIZ-ND"
    qty: 1
    price: "$26.01 CAD"
    link: "https://www.digikey.ca/en/products/detail/analog-devices-inc/ADUM4150BRIZ/4462118"
  - item: "Differential Operational Amplifiers"
    part_number: "29630028-2-ND"
    qty: 4
    price: "$56.20 CAD"
    link: "https://www.digikey.ca/en/products/detail/texas-instruments/THS4521IDR/2353347"
  - item: "MP725 200mΩ 25W DPAK Shunt Resistors"
    part_number: "MP725-0.20-FTR-ND"
    qty: 4
    price: "$44.29 CAD"
    link: "https://www.digikey.ca/en/products/detail/caddock-electronics-inc/MP725-0.20-1/237207"
  - item: "Precision 5K Resistors"
    part_number: "804-Y40225K00000T9RTR-ND"
    qty: 2
    price: "$38.24 CAD"
  - item: "Precision 50K Resistors"
    part_number: "PLTT50.0KACT-ND"
    qty: 2
    price: "$15.72 CAD"
  - item: "FHDO GPA Printed Circuit Boards"
    part_number: "JLCPCB 4-layer"
    qty: 5
    price: "$59.52 CAD"
  - item: "Extruded Aluminum Heatsinks"
    part_number: "HS-343-ND"
    qty: 4
    price: "$33.48 CAD"
  - item: "Voltage Regulators (12V & 5V) + 2.5V Reference"
    part_number: "497-7767-1-ND, 497-2957-5-ND, 296-39165-1-ND"
    qty: 3
    price: "$8.92 CAD"
  - item: "Molex High-Current Output Coil Connectors & Plugs"
    part_number: "WM-13112, WM 3701-ND"
    qty: 8
    price: "$11.16 CAD"
  - item: "Shielded 20 AWG Data Cable (16 feet)"
    part_number: "4903-CF211-05-02-02-DS-ND"
    qty: 1
    price: "$149.51 CAD"
assembly_guide: |
  #### GPA Installation and Integration
  1. **PCB Inspection & Preparation**: Verify solder joints on the JLCPCB 4-layer boards, particularly thermal pads beneath the OPA549 high-current power op-amps and MP725 DPAK shunt resistors.
  2. **Heatsink Assembly**: Secure the four extruded aluminum heatsinks (HS-343-ND) to the OPA549 amplifier pairs using thermal paste and retaining clips (115000F00000G-ND).
  3. **Power Bus Wiring**: Connect the high-current DC switching power supply (TekPower TP1560E) to the VCC barrier strip (WM 21 367-ND), ensuring polarity and ground bonding.
  4. **Interface Connection**: Wire the SPI control bus from the RedPitaya GPA adapter board through the ADUM4150 digital isolators to the DAC80504 and ADS8684 ADC channels.
  5. **Output Routing**: Route the high-current coil output connectors (WM-13112) through the gradient filter circuit before connecting to the physical gradient coils.
testing_guide: |
  #### GPA Calibration & Protection Test
  1. **Power-On Voltage Verification**: Power up the low-voltage auxiliary rails (+12V, +5V, +2.5V reference). Check U7, U21, and U22 outputs on a digital multimeter.
  2. **Dummy Load Pulsing**: Connect non-inductive high-power dummy load resistors (matched to coil impedance, ~1–2 Ω, 100 μH) across each channel.
  3. **Step Response & Linearity**: Inject trapezoidal gradient pulse sequences from MaRGE / MaRCoS (0.5A to 5A steps). Measure output current using an oscilloscope with a current probe (CP6220-EU).
  4. **Feedback Loop Tuning**: Verify that differential feedback op-amps (THS4521) provide stable closed-loop regulation without overshoot, oscillation, or excessive ringing.
  5. **Thermal & Over-Current Safeguards**: Verify that thermal shutdown and limit protection trip correctly under sustained maximum-current conditions.
---
## Overview

The IMAGINE MRI scanner uses the open-source **[GPA-FHDO gradient power amplifier](https://github.com/menkueclab/GPA-FHDO)** developed by the Fachhochschule Dortmund (FHDO) to drive the $X$, $Y$, and $Z$ gradient coils.

The GPA-FHDO is a modular four-channel gradient power amplifier specifically designed for low-field MRI applications. In the IMAGINE preclinical scanner, three channels are dedicated to driving the orthogonal gradient axes ($G_x$, $G_y$, $G_z$), with the fourth channel available for auxiliary $B_0$ shimming or secondary coils.

> **Implementation Note:** The GPA used in the IMAGINE scanner is based directly on the original GPA-FHDO design. Several active and passive components and implementation details were customized for our scanner configuration, including dedicated filter networks, upgraded current sensing shunts, and direct integration with the RedPitaya STEMlab / MaRCoS platform.

### Bill of Materials

The complete procurement bill of materials for the IMAGINE GPA implementation is tracked in the repository:
- [Download IMAGINE GPA BOM (XLSX)](../../Hardware/Gradient_Power_Amplifier/IMAGINE_GPA_BOM.xlsx)
- [View IMAGINE GPA BOM (CSV)](../../Hardware/Gradient_Power_Amplifier/IMAGINE_GPA_BOM.csv)

The BOM encompasses active ICs, passive feedback networks, PCB fabrication via JLCPCB, external power supply, cabling, and dedicated testing equipment (TekPower supply, current probe, and Arduino diagnostic tools).

### Original GPA-FHDO Reference Documentation
- Original GitHub Repository: [menkueclab/GPA-FHDO](https://github.com/menkueclab/GPA-FHDO)
- Official ReadTheDocs Documentation: [https://gpa-fhdo.readthedocs.io/en/latest/](https://gpa-fhdo.readthedocs.io/en/latest/)

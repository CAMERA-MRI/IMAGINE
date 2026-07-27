---
layout: component
title: "MaRCoS & Control System"
scanner_id: imagine
category: "control"
description: "The digital control core of the preclinical scanner, leveraging MaRCoS firmware on a RedPitaya SDR and controlled via the MARGE GUI."
downloads:
  - name: "MaRCoS GitHub Repository"
    path: "https://github.com/marcos-mri"
  - name: "MaRGE GUI Repository"
    path: "https://github.com/josalggui/MaRGE"
bom:
  - item: "Red Pitaya STEMlab 125-14 Board"
    qty: 1
    price: "Included in budget"
  - item: "Aluminum MaRCoS Enclosure Box"
    qty: 1
    price: "$205.25"
    link: "https://www.digikey.ca/en/products/detail/hammond-manufacturing/1590Z166/1090767"
  - item: "Panel Mount SMA sockets"
    qty: 6
    price: "$19.99"
    link: "https://www.amazon.ca/BOOBRIE-Connector-Bulkhead-Extendable-Antennas/dp/B07WFLD2MX"
  - item: "SMA to SMA Male-Male Cables"
    qty: 2
    price: "$31.98"
    link: "https://www.amazon.ca/Superbat-Connector-Coaxial-Antenna-Analyzer/dp/B0BFPWJ3J9"
  - item: "Ethernet Port Panel Mount Extensions"
    qty: 2
    price: "$27.98"
    link: "https://www.amazon.ca/Ethernet-Extension-Shielded-Compatibility-Network/dp/B0D5QGCM3D"
  - item: "Panel Mount BNC Connectors"
    qty: 4
    price: "$10.69"
    link: "https://www.amazon.ca/Connector-Bulkhead-Adapters-Coaxial-Adapter/dp/B09CG7WVHQ"
assembly_guide: |
  #### Phase 1: Software Setup
  1. Download the MaRCoS SD card image and flash it onto a high-speed MicroSD card.
  2. Insert the SD card into the Red Pitaya board.
  3. Install Python 3, numpy, scipy, and the `marcos-client` package on the Host PC.
  4. Clone and install the MARGE GUI repository: [MARGE GitHub](https://github.com/josalggui/MaRGE).
  
  #### Phase 2: Enclosure Fabrication
  1. Take the Hammond 1590Z166 Aluminum Box and mark hole placements for:
     - 4x RF Ports (BNC / SMA).
     - 1x Ethernet extension jack.
     - 1x DC power input.
     - 1x TTL pulse outputs.
  2. Drill the holes carefully using a step drill bit.
  3. Mount the panel sockets, routing the internal coaxial cables to the Red Pitaya RF input/output headers.
testing_guide: |
  #### Red Pitaya Signal Verification
  1. Connect the Red Pitaya to the host PC via Ethernet.
  2. Launch the MARGE GUI.
  3. Wire the RF Outputs of the Red Pitaya to an external oscilloscope.
  4. Run a simple test sequence in MARGE (e.g. pulse generator) and verify that the expected pulses appear on the oscilloscope with correct amplitude and duration.
---
The **Control System** handles the execution of MRI pulse sequences. It coordinates the radiofrequency (RF) transmit/receive timing and the gradient coil currents. **MaRCoS** (Magnetic Resonance Control System) is an open-source console console firmware running on a Red Pitaya board, replacing traditional expensive commercial consoles. The console is fully controlled via the **MARGE** graphical user interface.

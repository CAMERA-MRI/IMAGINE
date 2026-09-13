---
layout: component
title: "ERNIE Mechanical Frame & Spacers"
scanner_id: ernie
category: "magnet"
description: "The non-magnetic structural frame holding the ERNIE Halbach rings at their exact optimized axial spacing."
downloads:
  - name: "Ring Spacers STL"
    path: "/ERNIE/Build your own Design/Magnet/Scanner parts for 3D printing/ERNIE 1&2 rings and lids (.stl)/Ring_spacers.stl"
bom:
  - item: "M4 Threaded Brass Rods (180 mm, McMaster-Carr)"
    part_number: "90162A050"
    qty: 8
    price: "$39.54 CAD"
    link: "https://www.mcmaster.com/catalog/131/3633/90162A050"
  - item: "Ring Spacers (3D Printed PLA, ~100g total)"
    qty: 48
    price: "3D Printed (PLA)"
  - item: "M4 Brass Hex Nuts (Pack of 50)"
    part_number: "B0CQGYC7JZ"
    qty: 8
    price: "$11.33 CAD"
    link: "https://www.amazon.ca/100pcs-Solid-Brass-Copper-Screw/dp/B0CQGYC7JZ"
  - item: "M3 Brass Screws (60/pack)"
    part_number: "a23122400ux0074"
    qty: 54
    price: "$13.99 CAD"
    link: "https://www.amazon.ca/dp/B0CT3W8148"
  - item: "M4 Dome Nuts (McMaster-Carr)"
    part_number: "90527A505"
    qty: 8
    price: "$22.96 CAD"
    link: "https://www.mcmaster.com/products/dome-nuts/thread-size~m4/"
  - item: "M4 Nylon Washers"
    part_number: "95610A150"
    qty: 16
    price: "$7.70 CAD"
    link: "https://www.mcmaster.com/catalog/131/3696/95610A150"
  - item: "M3 Brass Heat-Set Inserts"
    part_number: "a24062300ux0395"
    qty: 54
    price: "$17.69 CAD"
    link: "https://www.amazon.ca/dp/B0DC43HJKN"
assembly_guide: |
  #### Frame Assembly and Spacing
  1. Cut two 1-meter M4 solid brass threaded rods into ten 180 mm lengths (8 active rods + 2 spares).
  2. Slide the central ring onto the 8 brass rods.
  3. Thread PLA ring spacers and brass M4 hex nuts between consecutive rings to fix the precise inter-ring distance.
  4. Secure outer ends with nylon washers and brass dome nuts.
testing_guide: |
  #### Structural & Parallelism Check
  1. Measure inter-ring distances using digital Vernier calipers at 4 circumferential quadrants.
  2. Confirm parallelism tolerance is within ±0.2 mm across all rings.
---
## Overview

The **Mechanical Frame & Spacers** maintain rigid structural integrity and precise axial positioning of the Halbach rings. All structural elements are non-magnetic (brass and PLA) to prevent distortion of the 50 mT field.

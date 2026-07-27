---
layout: component
title: "ERNIE 7-Ring Halbach Magnet"
scanner_id: ernie
category: "magnet"
description: "The primary B0 field source for the ERNIE scanner: a 7-ring, 50 mT Halbach array optimized for a homogeneous bore field."
video_url: "/ERNIE/Build your own Design/Magnet/Instructions/Animation/Assembly_Animation.mp4"
downloads:
  - name: "Ring 42 STL"
    path: "/ERNIE/Build your own Design/Magnet/Scanner parts for 3D printing/ERNIE 1&2 rings and lids (.stl)/Ring 42 (105mm_length ).stl"
  - name: "Ring 251 STL"
    path: "/ERNIE/Build your own Design/Magnet/Scanner parts for 3D printing/ERNIE 1&2 rings and lids (.stl)/Ring 251.stl"
  - name: "Ring 288 STL"
    path: "/ERNIE/Build your own Design/Magnet/Scanner parts for 3D printing/ERNIE 1&2 rings and lids (.stl)/Ring 288.stl"
  - name: "Ring 321 STL"
    path: "/ERNIE/Build your own Design/Magnet/Scanner parts for 3D printing/ERNIE 1&2 rings and lids (.stl)/Ring 321 (105mm_length).stl"
  - name: "Ring Spacers STL"
    path: "/ERNIE/Build your own Design/Magnet/Scanner parts for 3D printing/ERNIE 1&2 rings and lids (.stl)/Ring_spacers.stl"
  - name: "Lid for Ring 42 STL"
    path: "/ERNIE/Build your own Design/Magnet/Scanner parts for 3D printing/ERNIE 1&2 rings and lids (.stl)/Lid_For_Ring_42.stl"
  - name: "Lid for Ring 321 STL"
    path: "/ERNIE/Build your own Design/Magnet/Scanner parts for 3D printing/ERNIE 1&2 rings and lids (.stl)/Lid_For_Ring_321.stl"
bom:
  - item: "Neodymium Magnets (N48, 12x12x12mm)"
    qty: 98
    price: "Approx. $2.50 each"
    link: "https://www.supermagnete.de/"
  - item: "M4 Threaded Brass Rods (262mm long)"
    qty: 8
    price: "$1.50 each"
  - item: "M3x8mm Screws (to fasten lids)"
    qty: 125
    price: "$5.00 pack"
  - item: "M4 Hex Nuts (spacing adjustment)"
    qty: 160
    price: "$4.00 pack"
  - item: "M4 Dome Nuts"
    qty: 16
    price: "$3.00 pack"
  - item: "M4 Nylon Washers"
    qty: 16
    price: "$2.00 pack"
assembly_guide: |
  #### Phase 1: 3D Printing & Prep
  1. Print the 7 housing rings (Rings 42, 251, 288, 321, etc.) and matching lids.
  2. Prepare 8 M4 brass rods, cut to exactly 262mm.
  
  #### Phase 2: Magnet Insertion
  1. Carefully slide the 12x12x12mm neodymium magnets into the ring slots.
  2. **WARNING**: Magnets must be placed in their exact Halbach orientations. Check polarity before locking!
  3. Secure the lids onto each ring using M3x8mm screws.
  
  #### Phase 3: Ring Stacking
  1. Stack the rings along the 8 brass rods in a mirrored fashion.
  2. Ring 842 acts as the central ring. Stack the others on either side symmetrically: 842 -> 1 -> 0 -> 10 on one side, and 842 -> 945 -> 1050 -> 10B on the other.
  3. All rings must face the same direction (magnet-side forward).
  4. Secure spacer rings in between to establish the correct axial spacing.
testing_guide: |
  #### B0 Field Homogeneity Mapping
  1. Position the assembled magnet array on a flat, non-magnetic surface.
  2. Assemble the 3-axis Field Mapping Robot and position its Hall probe at the geometric center of the bore.
  3. Run the mapping script to measure the B0 field.
  4. Calculate homogeneity (expected: ~50 mT +/- 100 ppm over the target DSV).
  5. If necessary, insert custom shimming magnets into the shim trays to adjust homogeneity.
---
The magnet is the heart of the ERNIE educational scanner. It is a 7-ring Halbach magnet array that produces an ultra-low-field of approximately 50 mT. The design leverages genetic algorithm optimization to define the magnet placements and ring spacings, creating a homogeneous field without the need for complex, heavy electromagnetic coils.

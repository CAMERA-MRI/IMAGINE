---
layout: scanner
scanner_id: imagine
title: "IMAGINE Preclinical Scanner"
description: "The main IMAGINE scanner is an open-source, ultra-low-field (50 mT) preclinical MRI scanner designed for rodent and sample imaging. It implements modular, affordable electronics, custom gradient amplifiers, and a solenoid RF coil."
permalink: /scanners/imagine/
---
The **IMAGINE Preclinical Scanner** is designed to sustainably democratize diagnostic imaging and make preclinical MR systems accessible to clinicians and researchers in resource-limited settings globally. It incorporates:
- A 120mm bore Halbach array magnet assembly.
- Custom-wound 3D-printed gradient coils driven by the GPA-FHDO amplifier.
- A custom 27-turn RF solenoid coil and passive/active TxRx switches.
- An open-source electronic control system (MaRCoS) controlled via the user-friendly MARGE GUI.

All modules are designed using standard parts, making them easy to purchase and assemble with local tools. Follow the interactive block diagrams on the left to inspect the design details of the Control System, Gradient Circuit, and RF Circuit.

---

## 🛠️ Visual Assembly & Quality Assurance Media

The following videos demonstrate the mechanical assembly techniques and automated field mapping procedures used to construct and calibrate the IMAGINE preclinical scanner:

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem; margin: 1.5rem 0;">
  <div class="video-player-container" style="margin: 0;">
    <video controls preload="metadata" playsinline class="assembly-video">
      <source src="{{ site.baseurl }}/assets/videos/Assembly_Animation.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
    <div class="video-footer-meta">
      <span class="video-caption"><i class="fa-solid fa-circle-play"></i> Halbach Magnet Array Assembly Animation</span>
      <a href="{{ site.baseurl }}/assets/videos/Assembly_Animation.mp4" target="_blank" download class="video-fallback-link"><i class="fa-solid fa-arrow-down"></i> Download Animation (MP4)</a>
    </div>
  </div>
  <div class="video-player-container" style="margin: 0;">
    <video controls preload="metadata" playsinline class="assembly-video">
      <source src="{{ site.baseurl }}/assets/videos/ernie_robot_intro.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
    <div class="video-footer-meta">
      <span class="video-caption"><i class="fa-solid fa-circle-play"></i> 3-Axis Field Mapping Robot Demonstration</span>
      <a href="{{ site.baseurl }}/assets/videos/ernie_robot_intro.mp4" target="_blank" download class="video-fallback-link"><i class="fa-solid fa-arrow-down"></i> Download Video (MP4)</a>
    </div>
  </div>
</div>

---

## 🎓 Low-Field MRI Engineering Masterclasses

To support researchers, clinicians, and engineers replicating the IMAGINE preclinical system, comprehensive recorded lectures detailing low-field MRI engineering principles are provided below:

#### 🎥 Lecture 1: Building Your Own Low-Field MRI Scanner
Presented by **Dr. Johnes Obungoloch** (Mbarara University of Science & Technology / MRI Uganda), this masterclass covers the full hardware pipeline of open-source low-field MRI: permanent magnet Halbach arrays, gradient coils, RF probes, transmit/receive switching, and spectrometer instrumentation.

<div class="video-player-container">
  <video controls preload="metadata" playsinline class="assembly-video">
    <source src="{{ site.baseurl }}/ERNIE/Training sessions/Training material/Building your own Low field MRI_Dr Johnes_( MRI Uganda ).mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <div class="video-footer-meta">
    <span class="video-caption"><i class="fa-solid fa-circle-play"></i> Building Your Own Low-Field MRI — Dr. Johnes Obungoloch (MRI Uganda)</span>
    <a href="{{ site.baseurl }}/ERNIE/Training sessions/Training material/Building your own Low field MRI_Dr Johnes_( MRI Uganda ).mp4" target="_blank" download class="video-fallback-link"><i class="fa-solid fa-arrow-down"></i> Download Video (MP4 - 506 MB)</a>
  </div>
</div>

#### 🎥 Lecture 2: Introductory Lecture on Low-Field MRI Theory
Presented by **Guillermo Sahonero-Alvarez**, this foundational lecture provides the theoretical framework of magnetic resonance physics: spin dynamics, RF excitation, relaxation mechanisms ($T_1$/$T_2$), k-space sampling trajectories, and gradient encoding considerations at 50 mT.

<div class="video-player-container">
  <video controls preload="metadata" playsinline class="assembly-video">
    <source src="{{ site.baseurl }}/ERNIE/Training sessions/Training material/Introductory lecture on MRI_Guillermo.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <div class="video-footer-meta">
    <span class="video-caption"><i class="fa-solid fa-circle-play"></i> Introductory Lecture on MRI Physics & Gradient Encoding — Guillermo Sahonero-Alvarez</span>
    <a href="{{ site.baseurl }}/ERNIE/Training sessions/Training material/Introductory lecture on MRI_Guillermo.mp4" target="_blank" download class="video-fallback-link"><i class="fa-solid fa-arrow-down"></i> Download Video (MP4 - 183 MB)</a>
  </div>
</div>

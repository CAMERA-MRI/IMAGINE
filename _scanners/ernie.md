---
layout: scanner
scanner_id: ernie
title: "ERNIE Scanner (Educational)"
description: "The CAMERA-IMAGINE-MRI Education (ERNIE) toolkit is a frugal educational toolkit for on-site construction of a 50 mT 'mice-like' brain MRI scanner. It is designed to facilitate hands-on learning of open-source low-field MRI engineering."
permalink: /scanners/ernie/
---
The **ERNIE Toolkit** was designed as a reusable teaching resource consisting of:
- A 30-minute introductory lecture on open-source low-field MR engineering concepts.
- An assembly animation and guide of scanner, robot, and field mapping (quality assurance).
- Bill of materials and 3D printing files for the magnet and robotic field mapping parts.
- Simple, accessible tools for onsite assembly.
- Software to run the robot and map the magnet's field homogeneity.

### Two identical kits: ERNIE 1 & ERNIE 2
To demonstrate the reproducibility of open science hardware:
- **ERNIE 1** was first assembled at the 2025 ESMRMB pre-congress workshop in Vienna, and then re-assembled at the 2026 ISMRM conference in Cape Town, South Africa.
- **ERNIE 2** was first assembled at the Montreal Neurological Institute (MNI - The Neuro) and then re-assembled multiple times at the Montreal General Hospital, Polytechnique Montreal, The Douglas Mental Health University Institute, and the 2026 ISMRM conference.

---

## 👥 Educational Training Sessions & Multi-Site Reproducibility

To evaluate the reproducibility of the ERNIE toolkit, multi-site reconstruction experiments were conducted in which independent teams rebuilt the scanner and robot across geographically distinct institutions using the same documentation, design package, and physical kit.

### Evaluated Reproducibility Dimensions
1. **Assembly Reproducibility**: Validating that independent teams of students, researchers, and engineers can successfully construct the 7-ring Halbach magnet array and 3-axis robot without specialized tooling.
2. **Operational Reproducibility**: Confirming that the Cartesian gantry, Arduino motor controller, and Hall gaussmeter consistently execute automated 3D raster field scans.
3. **Field Map Consistency**: Demonstrating that reconstructed magnets produce the target ~50 mT field strength with reproducible spatial homogeneity profiles.

### Participating Institutions & Workshops
- **ESMRMB Pre-Congress Workshop** (Vienna, Austria) – *ERNIE 1*
- **The Neuro / Montreal Neurological Institute** (Montreal, Canada) – *ERNIE 2*
- **Polytechnique Montréal** (Montreal, Canada) – *ERNIE 2*
- **Montreal General Hospital** (Montreal, Canada) – *ERNIE 2*
- **The Douglas Mental Health University Institute** (Montreal, Canada) – *ERNIE 2*
- **ISMRM Annual Meeting Workshop** (Cape Town, South Africa) – *ERNIE 1 & ERNIE 2*

All participating sites successfully reconstructed the scanner and robot using the provided kit, confirming the operational reproducibility of the open-hardware architecture.

### Curriculum & Training Materials
Participants in the training sessions received preparatory educational resources and recorded masterclasses:

#### 🎥 Lecture 1: Building Your Own Low-Field MRI Scanner
Presented by **Dr. Johnes Obungoloch** (Mbarara University of Science & Technology / MRI Uganda), this lecture breaks down the frugal engineering principles, permanent magnet Halbach arrays, gradient coils, RF probes, and spectrometer design necessary to build accessible low-field MRI scanners in low-resource environments.

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
Presented by **Guillermo Sahonero-Alvarez**, this foundational session covers the core physics of magnetic resonance imaging, including nuclear precession, Larmor frequency, RF excitation pulses, $T_1$ and $T_2$ relaxation times, spatial frequency encoding (k-space), and gradient switching dynamics at 50 mT.

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

---

## 🛠️ Visual Assembly & Field Mapping Media

The following demonstration and animation videos guide builders through constructing the 7-ring Halbach magnet array and assembling the automated 3-axis Cartesian robot for quality-assurance field mapping:

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem; margin: 1.5rem 0;">
  <div class="video-player-container" style="margin: 0;">
    <video controls preload="metadata" playsinline class="assembly-video">
      <source src="{{ site.baseurl }}/assets/videos/Assembly_Animation.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
    <div class="video-footer-meta">
      <span class="video-caption"><i class="fa-solid fa-circle-play"></i> 7-Ring Halbach Magnet Assembly Animation</span>
      <a href="{{ site.baseurl }}/assets/videos/Assembly_Animation.mp4" target="_blank" download class="video-fallback-link"><i class="fa-solid fa-arrow-down"></i> Download Animation (MP4)</a>
    </div>
  </div>
  <div class="video-player-container" style="margin: 0;">
    <video controls preload="metadata" playsinline class="assembly-video">
      <source src="{{ site.baseurl }}/assets/videos/ernie_robot_intro.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
    <div class="video-footer-meta">
      <span class="video-caption"><i class="fa-solid fa-circle-play"></i> 3-Axis Robot Setup & Mapping Video</span>
      <a href="{{ site.baseurl }}/assets/videos/ernie_robot_intro.mp4" target="_blank" download class="video-fallback-link"><i class="fa-solid fa-arrow-down"></i> Download Video (MP4)</a>
    </div>
  </div>
</div>

### Additional Workshop Resources
- **Curriculum and Reading List**: Comprehensive syllabus and publication repository for low-field magnetic resonance engineering.
- **Pre- and Post-Workshop Surveys**: Empirical evaluation of knowledge gain and participant confidence in open-source MRI engineering.

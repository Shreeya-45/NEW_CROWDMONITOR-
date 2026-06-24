# 👁️‍🗨️ Advanced Crowd Monitoring System

![Version](https://img.shields.io/badge/version-2.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-brightgreen.svg)
![YOLOv8](https://img.shields.io/badge/model-YOLOv8-yellow.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-Enabled-blue.svg)

An enterprise-grade crowd monitoring and analytics system that provides **perspective-correct density estimation**, **automated ground-plane calibration**, and **localized congestion alerts**.

---

## ✨ Key Features

- **Perspective-Correct Density**: Computes true density (people/m²) regardless of camera angle using homography transformations.
- **Accurate Foot-Point Localization**: Maps exact ground-contact geometry rather than relying on center bounding boxes.
- **AI Walkable Area Segmentation**: Automatically defines monitoring boundaries using BiSeNetV2.
- **Grid-Based Congestion Alerts**: Granular, real-time warning systems for highly localized crowding.
- **Flicker-Free UI**: Advanced Exponential Moving Average (EMA) temporal filtering.
- **Live Calibration UI**: Interactive 4-point homography calibration wizard.

---

## 🏗️ System Architecture

\\mermaid
flowchart TD
    A[CAMERA FEED] -->|YOLOv8| B[HUMAN DETECTION]
    B -->|head_localizer.py| C[FOOT POINT EXTRACTOR]
    C -->|homography.npy| D[PERSPECTIVE TRANSFORM]
    D -->|wx, wy| E[WORLD COORDINATES]
    E --> F[DBSCAN CLUSTERING & HULL AREA]
    F -->|Real m²| G[DENSITY METRICS]
    G --> H[CONGESTION DETECTOR]
    H -->|EMA Smoothing| I[LIVE DASHBOARD & ALERTS]
\
---

## 🧠 Methodology & Workflow

### 1. Calibration & Segmentation
The system avoids the common pitfall of assuming 1 pixel = 1 meter. 
Through an interactive calibration phase (\calibration_tool.py\), a **3x3 Homography Matrix** is generated. Additionally, an AI Ground Segmentor optionally isolates the walkable physical bounds of the room, disregarding walls and ceilings.

### 2. Detection & Ground Mapping
Using YOLOv8, humans are detected in the frame. Instead of using the generic center of the bounding box, our custom \head_localizer.py\ determines the precise foot-to-ground contact point, which is then projected into physical world coordinates (meters) using the perspective matrix.

### 3. Density & Congestion Analysis
With physical coordinates secured, the system applies DBSCAN clustering and calculates the Concave Hull area of the crowd. This yields highly accurate \people/m²\ metrics. A cell-based grid tracks localized bottlenecks over time and automatically triggers flashing \WARNING\ or \CRITICAL\ alerts on the dashboard.

---

## 💻 Technology Stack

| Layer | Technology | Purpose |
|-----------|------------|---------|
| **Core Logic** | Python, OpenCV | Image processing, matrices, rendering |
| **Object Detection** | Ultralytics YOLOv8 | Human bounding box extraction |
| **Semantic Segmentation**| mmsegmentation | Walkable floor surface detection |
| **Math & Algorithms** | NumPy, SciPy | Hull volume computation, EMA smoothing |
| **UI & Overlays** | OpenCV, Tkinter | Interactive HUDs and calibration menus |

---

## 🚀 Quick Start

### 1. Configure your floor space
Update \config.py\ to define your physical monitored dimensions:
\\python
WORLD_GRID_W = 10.0 # meters (Width)
WORLD_GRID_H = 8.0  # meters (Depth)
\
### 2. Run Calibration
\\ash
python calibration_tool.py
\*Follow the interactive wizard to click 4 reference points on your floor.*

### 3. Start Monitoring
\\ash
python main.py
\*Note: Press \C\ during runtime to access live recalibration menus without restarting the server.*

---

## 📚 Complete Documentation Index

Dive deeper into the individual components and technical methodologies:

| Guide | Description |
|-------|-------------|
| 🚀 **[Quickstart Guide](docs/QUICKSTART.md)** | 5-minute setup and configuration TL;DR |
| 📖 **[Calibration Guide](docs/CALIBRATION_GUIDE.md)** | Comprehensive tutorial on perspective calibration |
| ⚙️ **[Config Reference](docs/CONFIG_REFERENCE.md)** | Explanation of system variables and tuning |
| 📐 **[Density Math](docs/density_calculation_explanation.md)** | How physical m² metrics are derived and clustered |
| 🧠 **[Architecture Deep-Dive](docs/ARCHITECTURE.md)** | Deep dive into technical data flows and pipelines |
| 📋 **[Implementation Summary](docs/IMPLEMENTATION_SUMMARY.md)**| Overview of robustness features and version history |


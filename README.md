# TEAMS – Tiger-AI Effectiveness Assessment & Monitoring System

## Overview
TEAMS is a prototype AI-driven system designed to evaluate the effectiveness of Project Tiger conservation efforts using data-driven metrics. The system focuses on combining biological outcomes and administrative inputs to generate meaningful insights for decision-making.

This project was developed as a technical assignment to demonstrate data extraction, modeling, and application development capabilities.

---

## Problem Statement
Current tiger conservation assessment relies on periodic census cycles and manual monitoring. This project aims to provide a continuous, data-driven effectiveness measurement by correlating population growth, reserve management, funding, and threat indicators.

---

## Modules Implemented

### Module D – Tiger Success Index (Core Module)
- Built a composite effectiveness score using:
  - Tiger population growth
  - Reserve area
  - Funding allocation
- Used regression and weighted scoring to identify underperforming reserves.

### Module C – Anti-Poaching Risk Analysis
- Used clustering techniques to identify high-risk poaching zones.
- Compared poaching hotspots with patrol coverage to highlight under-patrolled areas.

---

## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Flask (for lightweight web interface)
- Matplotlib / Seaborn
- Jupyter Notebook

---

## Assumptions
- Sample and synthetic datasets are used due to limited access to real government data.
- The focus is on system design, metrics, and modeling approach rather than data volume.
- The architecture is designed to scale with real-world data sources.

---

## How to Run the Project

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Jupyter notebooks
```bash
jupyter notebook
```
Run the notebooks in the following order:
1. 01_data_exploration.ipynb
2. 02_module_d_regression.ipynb
3. 03_module_c_risk_clustering.ipynb
These steps generate processed datasets inside the data/processed folder.

### 3. Run the web application
```bash
python app/app.py
```
Open your browser and navigate to:
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## Key Outputs
- merged_data.csv – merged and cleaned dataset
- features.csv – engineered features including Tiger Success Index
- Identified poaching risk clusters
- Simple dashboard displaying overall effectiveness score

---

## Future Improvements
- Integrate real-time GIS and satellite imagery
- Automate data ingestion pipelines
- Add explainability for effectiveness metrics
- Deploy on cloud infrastructure
- Expand to additional conservation indicators

---

## Author
Jayanthi Challa
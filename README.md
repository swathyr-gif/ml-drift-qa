# ML Data Drift Detection for QA

## Overview
This project demonstrates how QA teams can detect data drift in ML systems.
It compares training (reference) data with daily incoming data and generates
a drift report to support model re-validation decisions.

## Why this matters
ML models can fail silently when input data changes.
Traditional QA tests cannot detect this risk.
This project adds a QA safety net for AI/ML systems.

## Project Flow
1. Train a baseline ML model
2. Save training data as reference
3. Simulate daily production data
4. Detect data drift using Evidently AI
5. Generate an HTML QA report

## QA Perspective
This project helps QA teams detect silent failures in ML systems by monitoring
data drift, even when APIs and UI tests pass.

## How QA Can Use This
- Monitor daily production data
- Detect input data drift early
- Decide when re-validation or retraining is required

## Tools Used
- Python
- scikit-learn
- Evidently AI
- Pandas, NumPy

## How to Run
```bash
python train_model.py
python generate_daily_data.py
python drift_check.py

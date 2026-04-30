# Datathon 2026 - The Gridbreakers Submission

This repository contains the source code and final submission for the Datathon 2026 - The Gridbreakers competition.

## 📂 Directory Structure

```text
Datathon_Submission/
├── Data/
│   ├── sales.csv
│   ├── sample_submission.csv
│   ├── customers.csv
│   ├── promotions.csv
│   └── ...
├── main_modeling_pipeline.py          # End-to-end reproducible modeling pipeline
├── submission.csv                     # Final Kaggle submission file
└── README.md                          # This instruction file
```

The technical report is stored in `Documents/Report/Report_Datathon_2026.pdf`.

## 🚀 How to Reproduce Results

### 1. Prerequisites
Ensure you have Python 3.9+ installed along with the required libraries. You can install the dependencies using:
```bash
pip install pandas numpy scikit-learn xgboost catboost shap
```

### 2. Dataset Preparation
The pipeline expects the competition files to be available in `Datathon_Submission/Data/`.
The provided repository already includes the required CSV files, including `sales.csv`, `sample_submission.csv`, `customers.csv`, and `promotions.csv`.

### 3. Execution Flow
To reproduce the final `submission.csv`, run the main pipeline from the `Datathon_Submission` directory:

```bash
python main_modeling_pipeline.py
```

The script generates the final submission file and keeps the row order aligned with `sample_submission.csv`, as required by the competition rules.

## 🔍 Explainability (XAI) & Business Insights
The technical report documents the explainability requirement using business-facing discussion of the main drivers of revenue, including calendar effects, lagged revenue behavior, and seasonal patterns.

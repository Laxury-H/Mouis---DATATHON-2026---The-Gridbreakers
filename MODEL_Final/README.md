# Time-Decay Revenue Forecasting Model

This repository contains the full modeling pipeline to generate the time-decay revenue forecast submission.

## 📂 Directory Structure
- `data/`: Contains all required input datasets (sales, customers, promotions, base submission).
- `src/`: Contains the model components (Deep Learning Stack, Recursive Components, One-Shot Components, and Blending scripts).
- `pipeline.py`: The main execution script that orchestrates the entire modeling process.

## 🚀 Execution Guide
To reproduce the final submission file, open your terminal at the root directory of this project and execute the pipeline:

```bash
python pipeline.py
```

Upon successful completion, the pipeline will automatically clean up all intermediate files. The final result will be saved at the root directory as:
`final_submission.csv`

## 🛠 Dependencies
Ensure your environment has the following libraries installed:
- `pandas`
- `numpy`
- `scikit-learn`
- `xgboost`
- `lightgbm`
- `catboost`

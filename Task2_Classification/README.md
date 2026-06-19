# Task 2: Exoplanet Discovery Method Classification 🪐

## Goal
Build a basic classification model using a small dataset to predict a categorical outcome based on input features.

## Description
This project uses a Random Forest Classifier to predict the **discovery method** of an exoplanet (transit, radial velocity, microlensing, or imaging) based on its physical and orbital properties.

## Dataset
Exoplanets dataset (`exoplanets.csv`) containing physical characteristics of discovered exoplanets, including mass, radius, orbital period, and host star properties.

##issue
Initial model showed 98% accuracy but failed completely on minority classes due to class imbalance. After using median imputation (instead of dropping rows) and class_weight='balanced', accuracy dropped to 80% but became far more meaningful — all classes are now actually being learned, with the model showing a precision-recall tradeoff particularly visible in the microlensing class

## Key Features Used
- Radius (RJ)
- Period (days)
- Semi-major axis (AU)
- Host star mass (M☉)
- Host star temp. (K)

## Key Steps
1. **Data Loading & Exploration** — loaded CSV, checked structure, identified data types and missing values
2. **Class Filtering** — kept only the top 4 discovery methods with sufficient sample sizes (dropped extremely rare classes)
3. **Data Cleaning** — converted text-based numeric columns to proper numeric types
4. **Handling Missing Values** — used median imputation instead of dropping rows, to preserve minority class samples
5. **Train-Test Split** — 80/20 split with stratification to maintain class proportions
6. **Model Training** — Random Forest Classifier with `class_weight='balanced'` to address class imbalance
7. **Evaluation** — used accuracy, precision, recall, and F1-score (not just accuracy, due to class imbalance)

## Key Insight 💡
Initial model showed 98% accuracy but completely failed on minority classes (0% recall on `radial vel.`) due to severe class imbalance after improper handling of missing data. After switching to median imputation and balanced class weights, accuracy became a more honest 80% — with all classes now being meaningfully predicted, highlighting the classic **precision-recall tradeoff** in imbalanced classification problems.

## Results
| Metric | Score |
|--------|-------|
| Accuracy | 80.42% |
| Macro Avg F1 | 0.72 |
| Weighted Avg F1 | 0.85 |

## Key Skills Used
- Data handling & cleaning (pandas)
- Handling missing data (imputation)
- Train-test split
- Supervised learning (Random Forest)
- Model evaluation beyond accuracy (classification report)

## Tech Used
- Python 3
- pandas, numpy
- scikit-learn

## How to Run
```bash
python classification.py
```

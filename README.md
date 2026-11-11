# Student Pass Prediction — Machine Learning Project

## Project Overview
This project builds an end-to-end Machine Learning workflow to predict whether a student passes or fails based on learning-related features.

The project uses a synthetic student dataset and compares a baseline model with Logistic Regression and Random Forest classifiers.

## Dataset
- File: `student_learning.csv`
- Records: 280
- Features used:
  - `hours_studied`
  - `attendance`
  - `practice_tests`
  - `sleep_hours`
  - `study_method`
- Target: `passed` (0 = Fail, 1 = Pass)

**Note:** `final_score` was excluded from training to prevent target leakage.

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib
- Streamlit
- Jupyter Notebook

## Machine Learning Workflow
1. Data loading and exploration
2. Feature and target separation
3. Stratified train-test split (80/20)
4. Baseline model using DummyClassifier
5. Data preprocessing using ColumnTransformer and Pipeline
6. Model training:
   - Logistic Regression
   - Random Forest
7. Evaluation using accuracy, F1-score, and confusion matrices
8. Saving and reloading the best model
9. Predicting new student records
10. Building a Streamlit prediction interface

## Model Performance

| Model | Accuracy | F1-Score |
|---|---:|---:|
| Dummy Classifier | 55.36% | 0.00 |
| Logistic Regression | 75.00% | 0.72 |
| Random Forest | 75.00% | 0.7083 |

Logistic Regression was selected as the final model because it achieved the same accuracy as Random Forest with a slightly higher F1-score.

## How to Run the Project

### 1. Install dependencies
```bash
pip install pandas numpy scikit-learn matplotlib joblib streamlit jupyter
```

### 2. Run the Streamlit application
Make sure `app.py` and `best_student_model.pkl` are in the same directory.

```bash
python -m streamlit run app.py
```

### 3. Open the Jupyter Notebook
Open the project notebook to explore the complete training and evaluation workflow.

## Project Files
- `student_learning.csv` — Training dataset
- `new_student_records.csv` — New records for prediction
- `best_student_model.pkl` — Saved Logistic Regression pipeline
- `app.py` — Streamlit application
- `README.md` — Project documentation
- `model_card.md` — Model information and limitations
- `evaluation_summary.md` — Model evaluation results
- `.ipynb` — Jupyter Notebook

## Important Disclaimer
This project uses synthetic educational data for learning and demonstration purposes only. Its predictions must not be used to evaluate, penalize, or make real-world decisions about students.
# Model Card — Student Pass Prediction

## 1. Model Details
- **Project:** Student Pass Prediction
- **Model Type:** Binary Classification
- **Selected Model:** Logistic Regression
- **Framework:** Scikit-learn
- **Saved Model:** `best_student_model.pkl`

## 2. Intended Purpose
The model demonstrates how Machine Learning can use learning-related information to predict a binary outcome (Pass or Fail).

It is intended for educational and experimental purposes only.

## 3. Dataset Information
- Dataset: `student_learning.csv`
- Total records: 280
- Training records: 224
- Testing records: 56
- Target column: `passed`
- Class 0: Fail
- Class 1: Pass

## 4. Input Features
The model uses five input features:
1. Hours studied
2. Attendance
3. Practice tests
4. Sleep hours
5. Study method

The `final_score` column was excluded to avoid target leakage.

## 5. Preprocessing
The model uses a Scikit-learn Pipeline with:
- Median imputation for numerical features
- StandardScaler for numerical features
- Most-frequent imputation for categorical features
- OneHotEncoder for categorical features
- Logistic Regression classifier

## 6. Evaluation Results
- Accuracy: 75%
- F1-score: 0.72
- True Negatives: 24
- False Positives: 7
- False Negatives: 7
- True Positives: 18

## 7. Limitations
- The dataset is synthetic and relatively small.
- Results may not generalize to real student populations.
- The model may make incorrect predictions.
- The model has not been validated for real-world educational use.

## 8. Ethical Considerations
This model must not be used to make real academic, admission, grading, disciplinary, or other high-impact decisions about students.

It is strictly an educational Machine Learning demonstration.
# Model Evaluation Summary

## 1. Evaluation Setup
All models were evaluated using the same stratified 80/20 train-test split.

- Total records: 280
- Training records: 224
- Testing records: 56
- Random state: 42
- Target: `passed`

The evaluation used accuracy, F1-score, and confusion matrices.

## 2. Model Comparison

| Model | Accuracy | F1-Score |
|---|---:|---:|
| Dummy Classifier | 55.36% | 0.00 |
| Logistic Regression | 75.00% | 0.72 |
| Random Forest | 75.00% | 0.7083 |

## 3. Confusion Matrices

### Dummy Classifier
```text
[[31  0]
 [25  0]]
```

### Logistic Regression
```text
[[24  7]
 [ 7 18]]
```

### Random Forest
```text
[[25  6]
 [ 8 17]]
```

Confusion matrix format:

- True Negative (TN): Actual Fail, predicted Fail.
- False Positive (FP): Actual Fail, predicted Pass.
- False Negative (FN): Actual Pass, predicted Fail.
- True Positive (TP): Actual Pass, predicted Pass.

## 4. Results Analysis

### Dummy Classifier
The baseline achieved 55.36% accuracy but an F1-score of 0.00. It predicted every test record as Fail and failed to identify any students who passed.

### Logistic Regression
Logistic Regression achieved 75% accuracy and an F1-score of 0.72. It correctly classified 42 out of 56 records, with 7 false positives and 7 false negatives.

### Random Forest
Random Forest achieved 75% accuracy and an F1-score of approximately 0.7083. It correctly classified 42 out of 56 records, with 6 false positives and 8 false negatives.

## 5. Final Model Selection

Logistic Regression was selected as the final model because it achieved the same accuracy as Random Forest while producing a slightly higher F1-score.

Both candidate models performed substantially better than the baseline.

## 6. Conclusion
The project successfully demonstrates an end-to-end Machine Learning workflow, including preprocessing, model training, evaluation, saving, reloading, prediction, and deployment through Streamlit.

The results are limited to a small synthetic dataset and should not be interpreted as evidence of real-world student performance.
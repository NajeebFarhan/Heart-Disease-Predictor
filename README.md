# 🫀 Heart Disease Risk Prediction API

A simple machine learning API that estimates the risk of heart disease from basic clinical information.

This project is built as a learning exercise to explore:
- Proper ML pipelines for tabular data
- Safe handling of missing inputs
- Deploying ML models using FastAPI

> [Dataset](https://www.kaggle.com/datasets/neurocipher/heartdisease) used in this project

**⚠️ Disclaimer: This project is for educational purposes only and is not medical advice.**


## 📌 Overview

The API accepts patient health data and returns:
- A risk probability (0–1)
- A binary prediction based on a configurable threshold

The model uses:
- Logistic Regression
- Polynomial feature expansion (degree 2)
- Proper preprocessing for numeric and categorical features


# 🚀 API Usage
### Endpoint
```
POST /predict
```

### Example Request
```json
{
  "Age": 54,
  "Sex": 1,
  "Chest_pain_type": 2,
  "BP": 145,
  "Cholesterol": 260,
  "Exercise_angina": 1
}
```

### Example Response
```json
{
  "risk": 0.41,
  "prediction": 1
}
```

- risk → estimated probability of heart disease
- prediction → based on a configurable threshold (default: 0.3)

> Some clinical fields are optional. If omitted, the model safely imputes them.

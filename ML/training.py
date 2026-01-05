import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import (train_test_split, cross_val_score)
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, PolynomialFeatures
from sklearn.impute import SimpleImputer
import joblib


def train():
    df = pd.read_csv("ML/Heart_Disease_Prediction.csv")

    X = df.drop(columns=["Heart Disease"])
    y = df["Heart Disease"].map({
        "Absence": 0,
        "Presence": 1
    })

    cat_cols = ["Sex", "Chest pain type", "FBS over 120", "EKG results", "Exercise angina", "Thallium"]
    num_cols = ["Age", "BP", "Cholesterol", "Max HR", "ST depression", "Slope of ST", "Number of vessels fluro"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    num_pipeline = make_pipeline(
        SimpleImputer(strategy="median"),
        PolynomialFeatures(degree=2, include_bias=False),
        StandardScaler(),
    )

    cat_pipeline = make_pipeline(
        SimpleImputer(strategy="most_frequent"),
        OneHotEncoder(handle_unknown="ignore"),
    )

    preprocessor = ColumnTransformer([
        ("num", num_pipeline, num_cols),
        ("cat", cat_pipeline, cat_cols),
    ])

    model = make_pipeline(
        preprocessor,
        LogisticRegression(),
    )

    model.fit(X_train, y_train)

    joblib.dump(model, "ML/heart_disease_predictor.joblib")
    print("Mode has been saved as heart_disease_predictor.joblib")

if __name__ == "__main__":
    train()
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np

class RiskFeatureEngineer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()

        cat_cols = ["Sex", "Chest pain type", "FBS over 120", "EKG results", "Exercise angina", "Thallium"]
        num_cols = ["Age", "BP", "Cholesterol", "Max HR", "ST depression", "Slope of ST", "Number of vessels fluro"]
        X[num_cols] = X[num_cols].fillna(X[num_cols].median())
        X[cat_cols] = X[cat_cols].fillna(X[cat_cols].mode())

        X["AgeGroup"] = pd.cut(
            X["Age"],
            bins=[0, 40, 55, np.inf],
            labels=[0, 1, 2]
        ).astype(int)

        X["CholesterolCategory"] = pd.cut(
            X["Cholesterol"],
            bins=[0, 200, 240, 1000],
            labels=[0, 1, 2]
        ).astype(int)

        X["BPCategory"] = pd.cut(
            X["BP"],
            bins=[0, 120, 140, 300],
            labels=[0, 1, 2]
        ).astype(int)

        X["RiskScore"] = (
            (X["Age"] > 50).astype(int) +
            (X["Cholesterol"] > 240).astype(int) +
            (X["BP"] > 140).astype(int) +
            (X["Exercise angina"] == 1).astype(int)
        )

        # Interactive features
        X["ExerciseAngina x ST_depression"] = X["Exercise angina"] * X["ST depression"]
        X["Age x MaxHR"] = X["Age"] * X["Max HR"]

        return X

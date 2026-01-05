import pandas as pd
import joblib
from typing import Any

class HeartDiseasePredictor:
    def __init__(self, model_path: str = None, threshold: float = 0.3) -> None:
        self.model = joblib.load(model_path)
        self.threshold = threshold

    def predict(self, data: dict[str, Any] | pd.Series) -> tuple[float, int]:
        """
        Returns (risk_probability, prediction)
        """
        df = pd.DataFrame([data])
        risk_probability = float(self.model.predict_proba(df)[:, 1][0])
        prediction = int(risk_probability >= self.threshold)

        return risk_probability, prediction
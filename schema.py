from pydantic import BaseModel, Field
from typing import Optional


class HeartDiseaseData(BaseModel):
    # --- Required (low friction, high signal) ---
    Age: int = Field(..., description="Age in years")
    Sex: int = Field(..., description="0 = female, 1 = male")
    Chest_pain_type: int = Field(..., description="Chest pain type")
    BP: int = Field(..., description="Resting blood pressure")
    Cholesterol: int = Field(..., description="Serum cholesterol (mg/dl)")
    Exercise_angina: int = Field(..., description="1 = yes, 0 = no")

    # --- Optional (clinical / hard to know) ---
    FBS_over_120: Optional[int] = Field(
        None,
        description="Fasting blood sugar > 120 mg/dl (1 = true, 0 = false)"
    )
    EKG_results: Optional[int] = Field(
        None,
        description="ECG results (0–2)"
    )
    Max_HR: Optional[int] = Field(
        None,
        description="Maximum heart rate achieved"
    )
    ST_depression: Optional[float] = Field(
        None,
        description="ST depression induced by exercise"
    )
    Slope_of_ST: Optional[int] = Field(
        None,
        description="Slope of the peak exercise ST segment"
    )
    Number_of_vessels_fluro: Optional[int] = Field(
        None,
        description="Number of major vessels colored by fluoroscopy"
    )
    Thallium: Optional[int] = Field(
        None,
        description="Thallium stress test result"
    )

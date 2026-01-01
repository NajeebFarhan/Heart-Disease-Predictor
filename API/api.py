from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .schema import HeartDiseaseData
from ML.heart_disease_predictor import HeartDiseasePredictor

app = FastAPI()

predictor = HeartDiseasePredictor(model_path="ML/heart_disease_predictor.joblib")

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return {"message": "Hello World"}



COLUMN_MAP = {
    "Chest_pain_type": "Chest pain type",
    "Exercise_angina": "Exercise angina",
    "ST_depression": "ST depression",
    "Slope_of_ST": "Slope of ST",
    "Number_of_vessels_fluro": "Number of vessels fluro",
    "EKG_results": "EKG results",
    "FBS_over_120": "FBS over 120",
    "Max_HR": "Max HR",
}
@app.post("/predict")
async def predict(data: HeartDiseaseData):
    data = data.model_dump()

    data = {
        COLUMN_MAP.get(k, k): v
        for k, v in data.items()
    }

    risk_proba, prediction = predictor.predict(data)

    return {
        "risk_proba": risk_proba,
        "prediction": prediction
    }
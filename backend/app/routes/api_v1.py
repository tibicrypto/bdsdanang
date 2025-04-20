# backend/app/routes/api_v1.py
from fastapi import APIRouter, Depends
from fastapi_limiter.depends import RateLimiter
from app.core.ai.predictor import DanangPredictor

router = APIRouter()
predictor = DanangPredictor.load()

@router.post("/predict", dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def predict_property(data: PropertyData):
    """Dự đoán giá BĐS Đà Nẵng"""
    processed = preprocess_danang_data(data)
    prediction = predictor.predict(processed)
    return {
        "price": round(prediction, 2),
        "unit": "tỷ VND",
        "location": data.dict()['location']
    }

# backend/app/core/ai/predictor.py
import joblib
import pandas as pd

class DanangPredictor:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)
        self.features = [
            'area', 'district_code', 'distance_to_center',
            'flood_risk', 'tourism_index'
        ]
    
    @classmethod
    def load(cls):
        return cls("/app/models/danang_xgb_v1.3.pkl")
    
    def predict(self, data):
        df = pd.DataFrame([data], columns=self.features)
        return self.model.predict(df)[0]

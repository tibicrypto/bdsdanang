# backend/tests/test_api.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_endpoint():
    payload = {
        "area": 100,
        "district_code": 1,
        "distance_to_center": 2.5,
        "flood_risk": 0,
        "tourism_index": 1.2
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "price" in response.json()

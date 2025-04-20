# backend/scripts/train_danang.py
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
import joblib

def train_model():
    data = pd.read_csv('/data/danang_properties.csv')
    
    features = ['area', 'district_code', 'distance_to_center', 
               'flood_risk', 'tourism_index']
    target = 'price'
    
    X_train, X_test, y_train, y_test = train_test_split(
        data[features], data[target], test_size=0.2
    )
    
    model = xgb.XGBRegressor(objective='reg:squarederror')
    model.fit(X_train, y_train)
    
    joblib.dump(model, '/app/models/danang_xgb_v1.3.pkl')

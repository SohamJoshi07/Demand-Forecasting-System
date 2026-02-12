from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI(title='Retail Demand Forecast API')

model = joblib.load('walmart_forecast_model.pkl')
features = joblib.load('model_features.pkl')

@app.get('/')
def home():
    return{'message': 'Retail Forecasting API is running'}

@app.post('/predict')
def predict(data: dict):
    df = pd.DataFrame(data, index=[0])
    prediction = model.predict(df[features])
    return {'forcasted_sales': float(prediction[0])}
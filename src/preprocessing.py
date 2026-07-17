import pandas as pd
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = BASE_DIR / "models" / "scaler.pkl"

scaler = joblib.load(MODEL_PATH)


label_maps = {

    "gender": {
        "Female": 0,
        "Male": 1
    },

    "Partner": {
        "No": 0,
        "Yes": 1
    },

    "Dependents": {
        "No": 0,
        "Yes": 1
    },

    "PhoneService": {
        "No": 0,
        "Yes": 1
    },

    "MultipleLines": {
        "No": 0,
        "No phone service": 1,
        "Yes": 2
    },

    "InternetService": {
        "DSL": 0,
        "Fiber optic": 1,
        "No": 2
    },

    "OnlineSecurity": {
        "No": 0,
        "No internet service": 1,
        "Yes": 2
    },

    "OnlineBackup": {
        "No": 0,
        "No internet service": 1,
        "Yes": 2
    },

    "DeviceProtection": {
        "No": 0,
        "No internet service": 1,
        "Yes": 2
    },

    "TechSupport": {
        "No": 0,
        "No internet service": 1,
        "Yes": 2
    },

    "StreamingTV": {
        "No": 0,
        "No internet service": 1,
        "Yes": 2
    },

    "StreamingMovies": {
        "No": 0,
        "No internet service": 1,
        "Yes": 2
    },

    "Contract": {
        "Month-to-month": 0,
        "One year": 1,
        "Two year": 2
    },

    "PaperlessBilling": {
        "No": 0,
        "Yes": 1
    },

    "PaymentMethod": {
        "Bank transfer (automatic)": 0,
        "Credit card (automatic)": 1,
        "Electronic check": 2,
        "Mailed check": 3
    }

}


def preprocess_input(data):

    df = pd.DataFrame([data])

    for column, mapping in label_maps.items():
        df[column] = df[column].map(mapping)

    numerical_features = [
        "tenure",
        "MonthlyCharges",
        "TotalCharges"
    ]

    df[numerical_features] = scaler.transform(
        df[numerical_features]
    )

    return df
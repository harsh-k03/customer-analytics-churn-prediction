import joblib
from pathlib import Path
import pandas as pd

from src.preprocessing import preprocess_input

BASE_DIR = Path(__file__).resolve().parents[1]

MODEL_PATH = BASE_DIR / "models" / "best_random_forest.pkl"
FEATURE_PATH = BASE_DIR / "models" / "feature_columns.pkl"

model = joblib.load(MODEL_PATH)
feature_columns = joblib.load(FEATURE_PATH)


def predict_customer(customer_data):

    processed = preprocess_input(customer_data)

    processed = processed.reindex(
        columns=feature_columns,
        fill_value=0
    )

    prediction = model.predict(processed)[0]

    probability = model.predict_proba(processed)[0][1]

    return prediction, probability
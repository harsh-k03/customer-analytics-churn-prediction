import streamlit as st
from pathlib import Path
import sys

# Add project root to Python path
BASE_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(BASE_DIR))

from src.predictor import predict_customer

st.set_page_config(
    page_title="Churn Prediction",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Customer Churn Prediction")

st.markdown(
    "Enter the customer details below and click **Predict Churn**."
)

st.divider()

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    senior = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    partner = st.selectbox(
        "Partner",
        ["No", "Yes"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["No", "Yes"]
    )

    tenure = st.slider(
        "Tenure (Months)",
        0,
        72,
        12
    )

    phone = st.selectbox(
        "Phone Service",
        ["No", "Yes"]
    )

    multiple = st.selectbox(
        "Multiple Lines",
        [
            "No",
            "No phone service",
            "Yes"
        ]
    )

    internet = st.selectbox(
        "Internet Service",
        [
            "DSL",
            "Fiber optic",
            "No"
        ]
    )

    security = st.selectbox(
        "Online Security",
        [
            "No",
            "No internet service",
            "Yes"
        ]
    )

    backup = st.selectbox(
        "Online Backup",
        [
            "No",
            "No internet service",
            "Yes"
        ]
    )

with col2:

    protection = st.selectbox(
        "Device Protection",
        [
            "No",
            "No internet service",
            "Yes"
        ]
    )

    support = st.selectbox(
        "Tech Support",
        [
            "No",
            "No internet service",
            "Yes"
        ]
    )

    tv = st.selectbox(
        "Streaming TV",
        [
            "No",
            "No internet service",
            "Yes"
        ]
    )

    movies = st.selectbox(
        "Streaming Movies",
        [
            "No",
            "No internet service",
            "Yes"
        ]
    )

    contract = st.selectbox(
        "Contract",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )

    paperless = st.selectbox(
        "Paperless Billing",
        [
            "No",
            "Yes"
        ]
    )

    payment = st.selectbox(
        "Payment Method",
        [
            "Bank transfer (automatic)",
            "Credit card (automatic)",
            "Electronic check",
            "Mailed check"
        ]
    )

    monthly = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0,
        step=1.0
    )

    total = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=1000.0,
        step=10.0
    )

st.divider()

if st.button("Predict Churn", use_container_width=True):

    customer = {

        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone,
        "MultipleLines": multiple,
        "InternetService": internet,
        "OnlineSecurity": security,
        "OnlineBackup": backup,
        "DeviceProtection": protection,
        "TechSupport": support,
        "StreamingTV": tv,
        "StreamingMovies": movies,
        "Contract": contract,
        "PaperlessBilling": paperless,
        "PaymentMethod": payment,
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }

    prediction, probability = predict_customer(customer)

    probability = float(probability)

    st.subheader("Prediction Result")

    if prediction == 1:

        st.error("⚠️ High Risk of Churn")

    else:

        st.success("✅ Customer Likely to Stay")

    st.metric(
        "Churn Probability",
        f"{probability*100:.2f}%"
    )

    st.progress(probability)

    st.info(
        f"Model confidence: {probability*100:.2f}%"
    )
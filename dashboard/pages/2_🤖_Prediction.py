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

st.divider()

# ---------- Session State ----------
if "sample_loaded" not in st.session_state:
    st.session_state.sample_loaded = False

if st.button("📋 Load Sample Customer"):

    st.session_state.sample_loaded = True

    st.session_state.gender = "Female"
    st.session_state.senior = 0
    st.session_state.partner = "Yes"
    st.session_state.dependents = "No"
    st.session_state.tenure = 12
    st.session_state.phone = "Yes"
    st.session_state.multiple = "No"
    st.session_state.internet = "Fiber optic"
    st.session_state.security = "No"
    st.session_state.backup = "Yes"
    st.session_state.protection = "No"
    st.session_state.support = "No"
    st.session_state.tv = "Yes"
    st.session_state.movies = "Yes"
    st.session_state.contract = "Month-to-month"
    st.session_state.paperless = "Yes"
    st.session_state.payment = "Electronic check"
    st.session_state.monthly = 89.90
    st.session_state.total = 1120.50

    st.rerun()

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"],
        key="gender"
    )

    senior = st.selectbox(
        "Senior Citizen",
        [0, 1],
        key="senior"
    )

    partner = st.selectbox(
        "Partner",
        ["No", "Yes"],
        key="partner"
    )

    dependents = st.selectbox(
        "Dependents",
        ["No", "Yes"],
        key="dependents"
    )

    tenure = st.slider(
        "Tenure (Months)",
        0,
        72,
        key="tenure"
    )

    phone = st.selectbox(
        "Phone Service",
        ["No", "Yes"],
        key="phone"
    )

    multiple = st.selectbox(
        "Multiple Lines",
        [
            "No",
            "No phone service",
            "Yes"
        ],
        key="multiple"
    )

    internet = st.selectbox(
        "Internet Service",
        [
            "DSL",
            "Fiber optic",
            "No"
        ],
        key="internet"
    )

    security = st.selectbox(
        "Online Security",
        [
            "No",
            "No internet service",
            "Yes"
        ],
        key="security"
    )

    backup = st.selectbox(
        "Online Backup",
        [
            "No",
            "No internet service",
            "Yes"
        ],
        key="backup"
    )

with col2:

    protection = st.selectbox(
        "Device Protection",
        [
            "No",
            "No internet service",
            "Yes"
        ],
        key="protection"
    )

    support = st.selectbox(
        "Tech Support",
        [
            "No",
            "No internet service",
            "Yes"
        ],
        key="support"
    )

    tv = st.selectbox(
        "Streaming TV",
        [
            "No",
            "No internet service",
            "Yes"
        ],
        key="tv"
    )

    movies = st.selectbox(
        "Streaming Movies",
        [
            "No",
            "No internet service",
            "Yes"
        ],
        key="movies"
    )

    contract = st.selectbox(
        "Contract",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ],
        key="contract"
    )

    paperless = st.selectbox(
        "Paperless Billing",
        [
            "No",
            "Yes"
        ],
        key="paperless"
    )

    payment = st.selectbox(
        "Payment Method",
        [
            "Bank transfer (automatic)",
            "Credit card (automatic)",
            "Electronic check",
            "Mailed check"
        ],
        key="payment"
    )

    monthly = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        step=1.0,
        key="monthly"
    )

    total = st.number_input(
        "Total Charges",
        min_value=0.0,
        step=10.0,
        key="total"
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
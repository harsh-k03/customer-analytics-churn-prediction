import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import joblib
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)

st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Model Performance")

BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_DIR = BASE_DIR / "models"
DATA_DIR = BASE_DIR / "data" / "processed"

# Load data
X_test = pd.read_csv(DATA_DIR / "X_test.csv")
y_test = pd.read_csv(DATA_DIR / "y_test.csv").squeeze()

# Load models
models = {
    "Logistic Regression": joblib.load(MODEL_DIR / "logistic_regression.pkl"),
    "Decision Tree": joblib.load(MODEL_DIR / "decision_tree.pkl"),
    "Random Forest (Baseline)": joblib.load(MODEL_DIR / "random_forest.pkl"),
    "Random Forest (Optimized)": joblib.load(MODEL_DIR / "best_random_forest.pkl"),
}

results = []

for name, model in models.items():

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    results.append({
        "Model": name,
        "Accuracy": accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred),
        "Recall": recall_score(y_test, y_pred),
        "F1 Score": f1_score(y_test, y_pred),
        "ROC AUC": roc_auc_score(y_test, y_prob)
    })

results_df = pd.DataFrame(results)

st.subheader("Performance Comparison")

st.dataframe(
    results_df.style.format({
        "Accuracy": "{:.2%}",
        "Precision": "{:.3f}",
        "Recall": "{:.3f}",
        "F1 Score": "{:.3f}",
        "ROC AUC": "{:.3f}"
    }),
    use_container_width=True
)

st.info(
    """
**Deployment Note**

Although Logistic Regression achieved the highest baseline accuracy (79.30%),
the Optimized Random Forest (79.03%) was selected for deployment after
hyperparameter tuning using GridSearchCV. Its performance is comparable to the
best baseline model while demonstrating a complete model optimization workflow.
"""
)

st.divider()

metric = st.selectbox(
    "Select Metric",
    [
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
        "ROC AUC"
    ]
)

fig = px.bar(
    results_df,
    x="Model",
    y=metric,
    color="Model",
    text=metric,
    title=f"{metric} Comparison"
)

fig.update_traces(texttemplate="%{text:.3f}")

fig.update_layout(
    showlegend=False,
    yaxis_range=[0, 1]
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.success(
    """
### 🚀 Deployed Model

**Optimized Random Forest**

- Hyperparameter tuning using GridSearchCV
- Accuracy: **79.03%**
- ROC-AUC: **0.829**
- Selected for deployment due to its strong performance after optimization and its robust ensemble learning approach.
"""
)
import streamlit as st
import joblib
import json
import pandas as pd
from src.config import BEST_MODEL_PATH, FEATURES_PATH

# ======================================================
# Page Configuration
# ======================================================
st.set_page_config(
    page_title="E-Commerce Delivery Prediction",
    page_icon="📦",
    layout="wide"
)

# ======================================================
# Custom CSS (Dark + Yellow Theme)
# ======================================================
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0e0e0e;
        color: #f5f5f5;
        font-family: 'Segoe UI', sans-serif;
    }

    h1 {
        color: #f9c74f;
        font-size: 2.2rem;
        text-align: center;
        margin-bottom: 5px;
    }

    h2, h3 {
        color: #f9c74f;
    }

    .card {
        background-color: #1c1c1c;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 0px 20px rgba(249, 199, 79, 0.15);
        margin-bottom: 20px;
    }

    div.stButton > button {
        background-color: #f9c74f;
        color: #000000;
        font-weight: bold;
        border-radius: 12px;
        height: 3em;
        width: 100%;
        border: none;
    }

    div.stButton > button:hover {
        background-color: #ffd166;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ======================================================
# Load Model & Feature Schema
# ======================================================
@st.cache_resource
def load_artifacts():
    if not BEST_MODEL_PATH.exists():
        st.error("❌ Trained model not found. Please train the model first.")
        st.stop()

    if not FEATURES_PATH.exists():
        st.error("❌ feature_list.json not found. Please run training.")
        st.stop()

    model = joblib.load(BEST_MODEL_PATH)
    with open(FEATURES_PATH, "r") as f:
        features = json.load(f)

    return model, features


model, feature_cols = load_artifacts()

# ======================================================
# App Header
# ======================================================
st.title("📦 E-Commerce Delivery Predictor")
st.markdown(
    "<center style='font-size:16px; color:#d6d6d6;'>"
    "AI-powered insights to predict on-time vs delayed deliveries"
    "</center>",
    unsafe_allow_html=True
)

# ======================================================
# Sidebar – User Inputs
# ======================================================
st.sidebar.header("📝 Enter Shipment Details")

warehouse = st.sidebar.selectbox("Warehouse Block", ["A", "B", "C", "D", "E"])
mode = st.sidebar.selectbox("Mode of Shipment", ["Ship", "Flight", "Road"])
importance = st.sidebar.selectbox("Product Importance", ["low", "medium", "high"])
gender = st.sidebar.selectbox("Customer Gender", ["M", "F"])

calls = st.sidebar.number_input("Customer Care Calls", 0, 10, 3)
rating = st.sidebar.slider("Customer Rating", 1, 5, 4)
prior = st.sidebar.number_input("Prior Purchases", 0, value=2)
cost = st.sidebar.number_input("Product Cost", 1, value=250)
discount = st.sidebar.number_input("Discount Offered", 0, value=10)
weight = st.sidebar.number_input("Product Weight (gms)", 1, value=1200)

if discount > cost:
    st.sidebar.warning("⚠️ Discount is greater than product cost.")

# ======================================================
# Main Panel – Prediction Card
# ======================================================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("📊 Delivery Prediction Result")

input_df = pd.DataFrame(
    [{
        "Warehouse_block": warehouse,
        "Mode_of_Shipment": mode,
        "Customer_care_calls": calls,
        "Customer_rating": rating,
        "Cost_of_the_Product": cost,
        "Prior_purchases": prior,
        "Product_importance": importance,
        "Gender": gender,
        "Discount_offered": discount,
        "Weight_in_gms": weight
    }],
    columns=feature_cols
)

# ======================================================
# Prediction Logic (REALISTIC & FIXED)
# ======================================================
if st.button("🚀 Predict Delivery Status"):

    if not hasattr(model, "predict_proba"):
        st.error("❌ This model does not support probability prediction.")
        st.stop()

    prediction_proba = model.predict_proba(input_df)[0][1]

    # -----------------------------
    # FINAL CONFIDENCE LOGIC
    # -----------------------------
    if prediction_proba >= 0.45:
        st.success("✅ **Likely ON-TIME delivery**")
    elif prediction_proba >= 0.35:
        st.warning("⚠️ **Uncertain delivery (Monitor closely)**")
    else:
        st.error("❌ **High risk of DELIVERY DELAY**")

    st.markdown("### 📈 Prediction Confidence")
    st.progress(int(prediction_proba * 100))
    st.write(f"Confidence Score: **{prediction_proba * 100:.2f}%**")

    with st.expander("ℹ️ How to interpret this result"):
        st.write(
            """
            - **Likely ON-TIME**: Delivery can be planned confidently.
            - **Uncertain**: Monitor shipment closely.
            - **High risk**: Delay mitigation may be required.
            """
        )

st.markdown("</div>", unsafe_allow_html=True)

# ======================================================
# Footer
# ======================================================
st.markdown(
    "<hr><center style='color:gray;'>Powered by Machine Learning · Optimizing E-Commerce Delivery Decisions 🚀</center>",
    unsafe_allow_html=True
)

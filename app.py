import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the model and scaler
model = joblib.load('models/ctr_model.pkl')
scaler = joblib.load('models/scaler.pkl')

st.title("Click Through Rate (CTR) Prediction")

st.write("Enter user details to predict if they will click on the ad.")

# Input fields
age = st.number_input("Age", min_value=1, max_value=100, value=25)
daily_time_spent = st.number_input("Daily Time Spent (minutes)", min_value=0.0, value=60.0)
area_income = st.number_input("Area Income", min_value=0.0, value=50000.0)

if st.button("Predict CTR"):
    # Prepare input
    input_data = np.array([[age, daily_time_spent, area_income]])
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    st.write(f"Predicted CTR Probability: {probability:.2%}")
    if prediction == 1:
        st.success("Likely to CLICK the ad")
    else:
        st.error("Likely to NOT click the ad")

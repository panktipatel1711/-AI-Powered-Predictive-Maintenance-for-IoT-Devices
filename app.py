import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Page Title
st.set_page_config(page_title="AI Maintenance Dashboard")
st.title("🛠️ Maintenance Dashboard")
st.write("Live Sensor Analytics")

# Load Model
model = joblib.load('models/pdm_model.pkl')

# Sidebar for Input
st.sidebar.header("Sensor Input Data")
temp = st.sidebar.number_input("Temperature (°C)", value=20.0)
vib = st.sidebar.number_input("Vibration (mm/s)", value=2.0)
curr = st.sidebar.number_input("Current (mA)", value=500.0)

# Main Dashboard Graph
data = pd.DataFrame({
    'Current': [curr] * 20,
    'Temperature': [temp] * 20,
    'Vibration': [vib] * 20
})
st.line_chart(data)

# Prediction Button
if st.button("Predict Machine Status"):
    # Match the column names used during training
    features = pd.DataFrame([[temp, vib, curr]], 
                         columns=['temperature', 'vibration', 'current'])
    
    prediction = model.predict(features)[0]
    
    st.subheader("Diagnosis Result:")
    if prediction == 1:
        st.error("🚨 ALERT: High Risk of Machine Failure!")
    else:
        st.success("✅ Machine Status: Normal")
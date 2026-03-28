import streamlit as st
import pandas as pd
import joblib
import numpy as np
st.title("Engine Predictive Maintenance")
@st.cache_resource
def load_artifacts():
    return joblib.load("best_xgboost_model.joblib")
model = load_artifacts()
st.write("Enter the engine sensor readings below to predict condition:")
rpm = st.number_input("Engine RPM", value=800.0)
lub_pres = st.number_input("Lub Oil Pressure", value=3.0)
fuel_pres = st.number_input("Fuel Pressure", value=6.0)
cool_pres = st.number_input("Coolant Pressure", value=2.0)
lub_temp = st.number_input("Lub Oil Temp", value=77.0)
cool_temp = st.number_input("Coolant Temp", value=78.0)
if st.button("Predict"):
    input_data = pd.DataFrame([[rpm, lub_pres, fuel_pres, cool_pres, lub_temp, cool_temp]], 
                              columns=['Engine rpm', 'Lub oil pressure', 'Fuel pressure', 'Coolant pressure', 'lub oil temp', 'Coolant temp'])
    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0]
    if prediction == 1: st.error(f"Maintenance Required (Probability: {prob[1]:.2f})")
    else: st.success(f"Engine Healthy (Probability: {prob[0]:.2f})")
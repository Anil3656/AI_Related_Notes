import streamlit as st
import joblib

model = joblib.load("model.pkl")

st.title("ML Prediction App")

input_value = st.number_input("Enter value")

if st.button("Predict"):
    result = model.predict([[input_value]])
    st.success(f"Prediction: {result[0].round(2)}")

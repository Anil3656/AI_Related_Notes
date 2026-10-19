import streamlit as st
import pickle
import numpy as np

# Load the saved model
model = pickle.load(open(r'C:\Users\aneel.kumar\NARESH_IT\Machine Learning\house_price_model.pkl', 'rb'))

st.title("🏠 House Price Prediction Web App")

st.write("Enter the property details below to estimate the house price:")

# --------------------------
# Input Fields (based on your dataset features)
# --------------------------
bedrooms = st.number_input("Number of Bedrooms", min_value=0, max_value=20, value=3, step=1)
bathrooms = st.number_input("Number of Bathrooms", min_value=0, max_value=20, value=2, step=1)
living_area = st.number_input("Living Area (sq ft)", min_value=100, max_value=20000, value=1500, step=50)
lot_area = st.number_input("Lot Area (sq ft)", min_value=500, max_value=100000, value=4000, step=100)
floors = st.number_input("Number of Floors", min_value=1, max_value=5, value=2, step=1)

waterfront = st.radio("Waterfront Present", ["Yes", "No"])
views = st.number_input("Number of Views", min_value=0, max_value=10, value=0, step=1)
condition = st.slider("Condition of the House (1–5)", 1, 5, 3)
grade = st.slider("Grade of the House (1–13)", 1, 13, 7)

house_area_excl_basement = st.number_input("Area of the House (Excluding Basement)", min_value=100, max_value=20000, value=1200, step=50)
basement_area = st.number_input("Area of the Basement (sq ft)", min_value=0, max_value=5000, value=500, step=50)

built_year = st.number_input("Built Year", min_value=1800, max_value=2025, value=2000, step=1)
renovation_year = st.number_input("Renovation Year", min_value=0, max_value=2025, value=0, step=1)

postal_code = st.number_input("Postal Code", min_value=10000, max_value=99999, value=12345, step=1)
latitude = st.number_input("Latitude", format="%.6f", value=47.5112)
longitude = st.number_input("Longitude", format="%.6f", value=-122.257)

living_area_renov = st.number_input("Living Area after Renovation (sq ft)", min_value=0, max_value=20000, value=1500, step=50)
lot_area_renov = st.number_input("Lot Area after Renovation (sq ft)", min_value=0, max_value=100000, value=4000, step=100)

schools_nearby = st.number_input("Number of Schools Nearby", min_value=0, max_value=50, value=3, step=1)
airport_distance = st.number_input("Distance from Airport (km)", min_value=0, max_value=200, value=10, step=1)

# --------------------------
# Preprocessing
# --------------------------
waterfront_val = 1 if waterfront == "Yes" else 0

# Arrange features in correct order
input_features = [
    bedrooms, bathrooms, living_area, lot_area, floors,
    waterfront_val, views, condition, grade,
    house_area_excl_basement, basement_area,
    built_year, renovation_year, postal_code,
    latitude, longitude,
    living_area_renov, lot_area_renov,
    schools_nearby, airport_distance
]

# Convert to numpy array
input_array = np.array(input_features).reshape(1, -1)

# --------------------------
# Prediction
# --------------------------
if st.button("🔍 Predict Price"):
    try:
        price = model.predict(input_array)[0]
        st.success(f"💰 Estimated House Price: ₹ {price:,.2f}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")

st.caption("⚠️ Note: Ensure your model was trained with exactly these 20 features in the same order.")
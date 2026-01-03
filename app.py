import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("house_price_model.pkl")

st.title("🏠 House Price Prediction App")

st.write("Enter house details to predict price")

# --- User Inputs ---
bath = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)
size = st.number_input("Size (BHK)", min_value=1, max_value=10, value=2)
total_sqft = st.number_input("Total Square Feet", min_value=300, max_value=10000, value=1000)
balcony = st.number_input("Balcony", min_value=0, max_value=5, value=1)

location = st.text_input("Location", value="Bangalore")
availability = st.selectbox("Availability", ["Ready To Move", "Under Construction"])
area_type = st.selectbox("Area Type", ["Super built-up Area", "Built-up Area", "Plot Area"])
society = st.text_input("Society", value="Unknown")

# --- Create Input DataFrame ---
input_df = pd.DataFrame([{
    "bath": bath,
    "size": size,
    "total_sqft": total_sqft,
    "balcony": balcony,
    "location": location,
    "availability": availability,
    "area_type": area_type,
    "society": society
}])

# --- Prediction ---
if st.button("Predict Price"):
    price = model.predict(input_df)[0]
    st.success(f"Estimated House Price: ₹ {round(price, 2)}")

# app.py
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64

# ===============================
# Background Image with Black Overlay
# ===============================
def add_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:image/{"png"};base64,{encoded});
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            position: relative;
        }}
        .stApp::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.55); /* black overlay with 55% opacity */
            z-index: 0;
        }}
        .stApp > * {{
            position: relative;
            z-index: 1;
        }}
        /* Floating card effect for inputs */
        .stSidebar, .block-container {{
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(6px);
            border-radius: 15px;
            padding: 15px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call background function
add_bg_from_local("Car BG.png")  # Replace with your background image file

# ===============================
# Load Model
# ===============================
pipe = pickle.load(open("LinearRegressionModelv2.pkl", "rb"))

# Load dataset (for dropdown values)
df = pd.read_csv("cars_24_combined.csv", index_col=0)

# ===============================
# App Title
# ===============================
st.title("Car Price Prediction App")
st.write("Enter car details below to get an estimated resale price.")

# ===============================
# Inputs
# ===============================
car_names = sorted(df['Car Name'].dropna().astype(str).unique())
locations = sorted(df['Location'].dropna().astype(str).unique())
fuel_types = sorted(df['Fuel'].dropna().astype(str).unique())
drive_types = sorted(df['Drive'].dropna().astype(str).unique())
car_types = sorted(df['Type'].dropna().astype(str).unique())

car_name = st.selectbox("Car Name", car_names)
location = st.selectbox("Location", locations)
fuel = st.selectbox("Fuel Type", fuel_types)
drive = st.selectbox("Drive Type", drive_types)
car_type = st.selectbox("Car Type", car_types)
year = st.number_input("Year of Manufacture", min_value=1990, max_value=2025, value=2018)
distance = st.number_input("Distance Driven (km)", min_value=0, max_value=300000, value=50000)
owner = st.selectbox("Owner Type", [1, 2, 3, 4])

# Convert input into DataFrame
input_data = pd.DataFrame({
    "Car Name": [car_name],
    "Location": [location],
    "Fuel": [fuel],
    "Drive": [drive],
    "Type": [car_type],
    "Year": [year],
    "Distance": [distance],
    "Owner": [owner]
})

# ===============================
# Prediction
# ===============================
if st.button("🔮 Predict Price"):
    prediction = pipe.predict(input_data)[0]
    st.success(f"💰 Estimated Car Price: ₹ {np.round(prediction, 2):,}")

import pickle
import streamlit as st

# Load the model
with open('pickle1.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to predict crop yield
def predict_crop(N, P, K, temperature, humidity, pH, rainfall):
    features = [[N, P, K, temperature, humidity, pH, rainfall]]  # Prepare features for prediction
    prediction = model.predict(features)  # Make prediction
    return prediction[0]  # Return the first prediction

# Define the app function
def app():
    st.title("Crop Yield Prediction")
    st.write("Enter the features for crop yield prediction:")

    # Input fields for features
    N = st.number_input("Nitrogen (N)", min_value=0.0, step=0.1)
    P = st.number_input("Phosphorus (P)", min_value=0.0, step=0.1)
    K = st.number_input("Potassium (K)", min_value=0.0, step=0.1)
    temperature = st.number_input("Temperature (°C)", min_value=0.0, step=0.1)
    humidity = st.number_input("Humidity (%)", min_value=0.0, step=0.1)
    pH = st.number_input("Soil pH", min_value=0.0, step=0.1)
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0, step=0.1)

    # Button to make prediction
    if st.button("Predict"):
        prediction = predict_crop(N, P, K, temperature, humidity, pH, rainfall)
        st.write(f"Predicted Crop Yield: {prediction}")

# No need for the __main__ block in this module

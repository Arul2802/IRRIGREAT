import streamlit as st
import pickle
import numpy as np
import pandas as pd
import altair as alt

# Load the trained model from the uploaded file
file_path = "model1.pkl"

# Define the main app function
def app():
    # Title of the app
    st.title("Price Prediction App")

    # Function to load the pickle file (assuming it contains the model)
    def load_model(file):
        with open(file, 'rb') as f:
            model = pickle.load(f)
        return model

    # Try to load the model
    try:
        model = load_model(file_path)
        st.success("Model loaded successfully!")

        # Display how many features the model expects
        expected_features = model.coef_.shape[0]  # Number of features model expects
        st.write(f"Model expects {expected_features} features.")
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        st.stop()

    # Collect user inputs for the features
    st.header("Enter the details:")

    # Vegetable (Text input)
    vegetable = st.selectbox("Vegetable", ("Tomato", "Potato", "Onion", "Carrot"))

    # Season (Dropdown selection)
    season = st.selectbox("Season", ("Summer", "Winter", "Spring", "Autumn"))

    # Month (Dropdown for selecting month)
    month = st.selectbox("Month", list(range(1, 13)))

    # Temp (Numeric input for temperature)
    temp = st.number_input("Temperature (°C)", min_value=-50.0, max_value=50.0, value=25.0)

    # Humidity (Numeric input for humidity)
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=50.0)  # New feature

    # Disaster Happen in last 3 months (Yes/No Checkbox)
    disaster = st.checkbox("Disaster Happen in last 3 months?")

    # Combine features into a numerical representation (reduce features to 6)
    # For simplicity, assign numbers to categories
    vegetable_dict = {"Tomato": 1, "Potato": 2, "Onion": 3, "Carrot": 4}
    season_dict = {"Summer": 1, "Winter": 2, "Spring": 3, "Autumn": 4}
    disaster_encoded = 1 if disaster else 0

    # Prepare the final input features based on 6 features expected by the model
    input_data = np.array([vegetable_dict[vegetable], season_dict[season], month, temp, humidity, disaster_encoded])

    # Reshape to ensure it matches the expected input shape (1 row, n features)
    input_data = input_data.reshape(1, -1)

    # Display the number of features in input_data
    st.write(f"Input data shape: {input_data.shape[1]} features provided.")

    # Button for prediction
    if st.button("Predict Price"):
        # Check if input feature length matches expected length
        if input_data.shape[1] != expected_features:
            st.error(f"Model expects {expected_features} features but received {input_data.shape[1]} features.")
        else:
            # Predict the price
            try:
                prediction = model.predict(input_data)
                st.write(f"The predicted price for {vegetable} is: ${prediction[0]:.2f}")
            except Exception as e:
                st.error(f"Error during prediction: {e}")

    # Visualization of average prices for different vegetables by selected month
    st.subheader(f"Average Price of Vegetables in Month {month}")

    # Sample data for visualization
    vegetable_data = pd.DataFrame({
        'Vegetable': ['Tomato', 'Potato', 'Onion', 'Carrot'] * 12,
        'Month': sum([[m] * 4 for m in range(1, 13)], []),
        'Average Price': [
            2.5, 1.8, 3.0, 2.2,  # January
            2.6, 1.9, 3.1, 2.3,  # February
            2.7, 2.0, 3.2, 2.4,  # March
            2.8, 2.1, 3.3, 2.5,  # April
            2.6, 1.9, 3.0, 2.2,  # May
            2.5, 1.8, 3.1, 2.3,  # June
            2.7, 1.9, 3.3, 2.4,  # July
            2.8, 2.0, 3.2, 2.5,  # August
            2.9, 2.1, 3.4, 2.6,  # September
            2.7, 2.0, 3.1, 2.3,  # October
            2.8, 1.9, 3.2, 2.4,  # November
            2.9, 2.2, 3.5, 2.7   # December
        ]  # Replace with real average prices if available
    })

    # Filter data based on the selected month
    monthly_data = vegetable_data[vegetable_data['Month'] == month]

    # Create a bar chart for the selected month using Altair
    chart = alt.Chart(monthly_data).mark_bar().encode(
        x=alt.X('Vegetable', title='Vegetable'),
        y=alt.Y('Average Price', title='Average Price ($)'),
        color='Vegetable'
    ).properties(
        width=600,
        height=400
    )

    # Display the chart in Streamlit
    st.altair_chart(chart, use_container_width=True)

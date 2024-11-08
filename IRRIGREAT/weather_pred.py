import streamlit as st
import requests

def app():
    st.title("Weather Forecast")

    API_KEY = "ced9f1c80ff3325c9a782e2683e8bb91"

    # Function to fetch weather data
    def get_weather(city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            st.error("Could not fetch data. Check the city name or try again.")
            return None

    # Input city name
    city = st.text_input("Enter a city name")

    # Display weather data
    if city:
        data = get_weather(city)
        if data:
            st.write(f"### Weather in {city.title()}")
            st.write(f"**Temperature**: {data['main']['temp']}°C")
            st.write(f"**Weather**: {data['weather'][0]['description'].capitalize()}")
            st.write(f"**Humidity**: {data['main']['humidity']}%")
            st.write(f"**Wind Speed**: {data['wind']['speed']} m/s")

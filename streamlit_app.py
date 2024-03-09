import streamlit as st
import requests

# Function to get weather data
def get_weather_data(city_name):
    api_key = "b5fb90812d2e71ecfedeee7880d05e40"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        return weather_description, temperature, humidity, wind_speed
    else:
        return None

# Streamlit app
st.title("City Data Viewer")

city_name = st.text_input("Enter the city name:")
if city_name:
    weather_data = get_weather_data(city_name)
    if weather_data:
        st.write(f"Weather in {city_name}: {weather_data[0]}")
        st.write(f"Temperature: {weather_data[1]}°C")
        st.write(f"Humidity: {weather_data[2]}%")
        st.write(f"Wind Speed: {weather_data[3]} m/s")
    else:
        st.write("City not found. Please enter a valid city name.")

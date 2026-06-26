from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/weather')
def weather():

    # --------------------------------------------------
    # Call the Open-Meteo API (no API key needed)
    # Latitude and Longitude for Chennai, India
    # --------------------------------------------------
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude":   13.08,
        "longitude":  80.27,
        "current":    "temperature_2m,wind_speed_10m",
        "timezone":   "Asia/Kolkata"
    }

    # Send GET request to the external API
    response = requests.get(url, params=params)

    # Convert the response to a Python dictionary
    data = response.json()

    # Pick out the values we need
    current     = data["current"]
    temperature = current["temperature_2m"]
    wind_speed  = current["wind_speed_10m"]

    print("Weather data received from API:")
    print("  Temperature :", temperature, "°C")
    print("  Wind Speed  :", wind_speed, "km/h")

    weather_info = {
        "city":        "Chennai",
        "temperature": temperature,
        "wind_speed":  wind_speed
    }

    return render_template('weather.html', weather=weather_info)


if __name__ == '__main__':
    app.run(debug=True)

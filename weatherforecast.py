import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_desc = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        return f"Weather: {weather_desc}\nTemperature: {temp}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s"
    else:
        return "Failed to retrieve weather data."

def get_weather_forecast(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        forecast_data = ""
        for forecast in data['list']:
            forecast_data += f"Date: {forecast['dt_txt']}\nWeather: {forecast['weather'][0]['description']}\nTemperature: {forecast['main']['temp']}°C\nHumidity: {forecast['main']['humidity']}%\nWind Speed: {forecast['wind']['speed']} m/s\n\n"
        return forecast_data
    else:
        return "Failed to retrieve forecast data."

def show_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Warning", "Please enter a city name.")
        return
    weather_info = get_weather(api_key, city)
    weather_label.config(text=weather_info)

def show_forecast():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Warning", "Please enter a city name.")
        return
    forecast_info = get_weather_forecast(api_key, city)
    forecast_label.config(text=forecast_info)

api_key = "3850c7d467deceb8a191902c84501a14"

root = tk.Tk()
root.title("Weather Forecast")

city_label = tk.Label(root, text="Enter city name:")
city_label.grid(row=0, column=0, padx=10, pady=10)

city_entry = tk.Entry(root)
city_entry.grid(row=0, column=1, padx=10, pady=10)

get_weather_button = tk.Button(root, text="Get Weather", command=show_weather)
get_weather_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="we")

weather_label = tk.Label(root, text="")
weather_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

get_forecast_button = tk.Button(root, text="Get Forecast", command=show_forecast)
get_forecast_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="we")

forecast_label = tk.Label(root, text="")
forecast_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
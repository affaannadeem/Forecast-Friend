import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
import io

# Function to fetch weather data
def get_weather():
    city = city_entry.get().strip()  # Remove any leading/trailing whitespace
    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return

    api_key = "your_weather_api_key"  # Replace with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        display_weather(weather_data)
    else:
        error_message = response.json().get("message", "City not found!")
        messagebox.showerror("Error", error_message)

# Function to display weather data
def display_weather(data):
    city_name = data['name']
    temperature = data['main']['temp']
    weather_desc = data['weather'][0]['description']
    
    weather_info = f"City: {city_name}\nTemperature: {temperature}°C\nDescription: {weather_desc.capitalize()}"
    weather_label.config(text=weather_info)

# Create the main window
root = tk.Tk()
root.title("Weather Forecast App")
root.geometry("400x300")
root.configure(bg='#87CEEB')  # Light blue color for the background

# Create and place widgets
city_label = tk.Label(root, text="Enter City:", bg='#87CEEB', font=("Arial", 14, "bold"), fg="white")
city_label.pack(pady=10)

city_entry = tk.Entry(root, width=30, font=("Arial", 14))
city_entry.pack(pady=10)

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather, bg='white', font=("Arial", 12, "bold"))
get_weather_button.pack(pady=10)

weather_label = tk.Label(root, text="", bg='#87CEEB', font=("Arial", 14), fg="white")
weather_label.pack(pady=20)

# Run the application
root.mainloop()
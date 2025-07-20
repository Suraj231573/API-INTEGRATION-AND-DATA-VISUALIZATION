import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

API_KEY = '144bc6db18df4a958188a8233b3b8802'
CITY = 'Ballari'
URL = (
    f'http://api.openweathermap.org/data/2.5/forecast'
    f'?q={CITY}&appid={API_KEY}&units=metric'
)

def fetch_weather_data():
    response = requests.get(URL)
    data = response.json()
    if response.status_code != 200:
        print("Failed to fetch data:", data.get("message", "Unknown error"))
        return []
    return data['list']

def prepare_data(raw_data):
    dates = [datetime.fromtimestamp(entry['dt']) for entry in raw_data]
    temps = [entry['main']['temp'] for entry in raw_data]
    humidity = [entry['main']['humidity'] for entry in raw_data]
    return dates, temps, humidity

def plot_weather(dates, temps, humidity):
    sns.set(style='whitegrid')
    plt.figure(figsize=(14, 6))

    plt.plot(dates, temps, label='Temperature (°C)', marker='o')
    plt.plot(dates, humidity, label='Humidity (%)', marker='x')

    plt.title(f"5‑Day Weather Forecast for {CITY}")
    plt.xlabel("Date & Time")
    plt.ylabel("Value")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    raw_data = fetch_weather_data()
    if raw_data:
        dates, temps, humidity = prepare_data(raw_data)
        plot_weather(dates, temps, humidity)

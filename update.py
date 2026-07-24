import requests
from datetime import datetime

url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=11.94"
    "&longitude=108.44"
    "&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
)

data = requests.get(url, timeout=10).json()

current = data["current"]

temperature = current["temperature_2m"]
humidity = current["relative_humidity_2m"]
wind = current["wind_speed_10m"]

time = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

text = f"""# Weather Report

## Da Lat

🌡 Temperature: {temperature} °C

💧 Humidity: {humidity} %

🌬 Wind: {wind} km/h

---

Updated

{time}

Generated automatically by GitHub Actions.
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(text)

print("README updated")

import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
CITY = "Warsaw"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"


def extract_weather():
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        print(f"✅ Data pulled for {CITY}")
        return data
    else:
        print(f"❌ Failed to fetch data: {response.status_code}")
        return None

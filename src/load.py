import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    return conn


def load_weather(data):
    if data is None:
        print("❌ No data to load")
        return

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO weather (city, country, temperature, feels_like, humidity, weather, wind_speed, recorded_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        data["city"],
        data["country"],
        data["temperature"],
        data["feels_like"],
        data["humidity"],
        data["weather"],
        data["wind_speed"],
        data["recorded_at"]
    ))

    conn.commit()
    cursor.close()
    conn.close()
    print(f"✅ Loaded into database: {data['city']} at {data['recorded_at']}")

from datetime import datetime


def transform_weather(raw_data):
    if raw_data is None:
        print("❌ No data to transform")
        return None

    transformed = {
        "city": raw_data["name"],
        "country": raw_data["sys"]["country"],
        "temperature": raw_data["main"]["temp"],
        "feels_like": raw_data["main"]["feels_like"],
        "humidity": raw_data["main"]["humidity"],
        "weather": raw_data["weather"][0]["description"],
        "wind_speed": raw_data["wind"]["speed"],
        "recorded_at": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    }

    print(
        f"✅ Transformed: {transformed['city']} | {transformed['temperature']}°C | {transformed['weather']}")
    return transformed

import time
import logging
import os
from extract import extract_weather
from transform import transform_weather
from load import load_weather


os.makedirs("../logs", exist_ok=True)
logging.basicConfig(
    filename="../logs/etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def run_pipeline():
    print("\n🚀 Starting ETL pipeline...")
    logging.info("Pipeline started")

    raw_data = extract_weather()

    clean_data = transform_weather(raw_data)

    load_weather(clean_data)

    print("✅ Pipeline complete\n")
    logging.info("Pipeline complete")


if __name__ == "__main__":
    while True:
        run_pipeline()
        print("⏳ Waiting 1 hour for next run...")
        time.sleep(3600)

# ETL Orchestration Agent

A Python-based ETL pipeline that extracts weather data, transforms it, and loads it into PostgreSQL automatically every hour.

## What it does
- Extracts live weather data from OpenWeatherMap API
- Transforms raw JSON into clean structured data
- Loads it into a PostgreSQL database
- Runs automatically every hour
- Logs every run to logs/etl.log

## Tech Stack
- Python 3.14
- PostgreSQL 18.3
- requests, psycopg2, python-dotenv

## Project Structure
etl-agent/
├── src/
│   ├── extract.py     
│   ├── transform.py   
│   ├── load.py        
│   └── main.py        
├── logs/              
├── .env               
└── README.md          

## Setup
1. Clone the repo
2. Create virtual environment: python -m venv venv
3. Activate: venv\Scripts\activate
4. Install dependencies: pip install -r requirements.txt
5. Add your credentials to .env
6. Run: cd src && python main.py

## Environment Variables
WEATHER_API_KEY=your_key
DB_HOST=localhost
DB_NAME=etl_agent
DB_USER=postgres
DB_PASSWORD=your_password
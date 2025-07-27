import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_by_city(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt-br"
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            "cidade": data["name"],
            "temperatura": data["main"]["temp"],
            "descricao": data["weather"][0]["description"],
            "umidade": data["main"]["humidity"],
            "sensacao_termica": data["main"]["feels_like"],
            "vento_kmh": round(data["wind"]["speed"] * 3.6, 2)
        }
    else:
        return {"erro": "Cidade não encontrada ou erro na API."}
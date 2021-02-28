import requests
import json
import datetime
from datetime import datetime

def forecast():
    read_config = open("config.json", "r")
    config = json.load(read_config)
    get_weather = requests.get(
    f'http://api.weatherapi.com/v1/current.json?key={config["api_key"]}&q={config["city"]}')
    weather = json.loads(get_weather.text)
    print(weather["location"]["name"] + " | " + datetime.strptime(weather["location"]["localtime"], "%Y-%m-%d %H:%M").strftime("%I:%M%p | %m/%d/%Y"))
    print(
        f'Current Temp: {weather["current"]["temp_f"]}°f | Feels like: {weather["current"]["feelslike_f"]}°f'
    )
    print(f'Condition: {weather["current"]["condition"]["text"]}')
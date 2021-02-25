#!/usr/bin/python3
import requests
from startup import startup
startup()
import config
import json

get_weather = requests.get(
    f'http://api.weatherapi.com/v1/current.json?key={config.api_key}&q=Los%20Angeles'
)

weather = json.loads(get_weather.text)
print(weather["location"]["localtime"])
print(
    f'Current Temp: {weather["current"]["temp_f"]}°f | Feels like: {weather["current"]["feelslike_f"]}°f'
)
print(f'Condition: {weather["current"]["condition"]["text"]}')
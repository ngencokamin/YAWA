import os
from os import path
import pyinputplus as pyip


def startup():
    if not path.isfile("config.py"):
        config = open("config.py", "w")
        api_key = input("Please enter your api key here: ")
        config.write(f"api_key = '{api_key}' \n")
        default_forecast = pyip.inputNum(
            min=1, max=7, prompt="How many days forecast by default? (1-7): ")
        config.write(f"default_forecast = {default_forecast} \n")
        result = pyip.inputMenu(
            ['Minimal', 'Aesthetic'],
            numbered=True,
            prompt="Do you prefer minimalism or ASCII art?: \n")
        config.write(f"view = '{result}' \n")

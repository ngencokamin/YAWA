import os
from os import path
import pyinputplus as pyip
import geocoder
import json


def get_location(set_type):
    if set_type=="Automatic":
        city = geocoder.ip("me").city + ", "+ geocoder.ip("me").state
        confirm_city = pyip.inputYesNo(f"Does '{city}' look right? [y/n] ")
        if confirm_city == "no":
            print("Sorry about that, let's try entering your city manually.")
            set_type = "Manual"
            get_location(set_type)
    else:
        city = input("Please enter your city: ").capitalize() + ", "
        city += input("Please enter your state: ").capitalize()
        confirm_city = pyip.inputYesNo(f"Does '{city}' look right? [y/n] ")
        if confirm_city == "no":
            print("Let's try that again.")
            get_location(set_type)
    return city



def startup():
    if not path.isfile("config.json"):
        settings = {
            "api_key": "",
            "default_forecast": 7,
            "view": "",
            "city": ""
        }

        api_key = input("Please enter your api key here: ")
        default_forecast = pyip.inputNum(
            min=1, max=7, prompt="How many days forecast by default? (1-7): ")
        # config.write(f"default_forecast = {default_forecast} \n")
        view = pyip.inputMenu(
            ['Minimal', 'Aesthetic'],
            numbered=True,
            prompt="Do you prefer minimalism or ASCII art?: \n")
        # config.write(f"view = '{result}' \n")
        locset = pyip.inputMenu(
            ['Automatic', 'Manual'],
            numbered=True,
            prompt="Would you prefer to have your city set automatically or manually?: \n")
        city = get_location(locset)
        settings["api_key"] = api_key
        settings["city"] = city
        settings["view"] = view
        settings["default_forecast"] = default_forecast
        settings_json = json.dumps(settings)
        config = open("config.json", "w")
        config.write(settings_json)        





import json
import requests


class Weather:
    def __init__(self):
        __API_TOKEN = json.load(open('keys.json'))['API']
        self.params = {'q': 'Москва', 'appid': __API_TOKEN, "main": "main.temp"}

    def get_temp(self):
        KELVIN = 273.15
        response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=self.params)
        temp_in_kelvin = response.json()["main"]["temp"]
        temp_in_celsius = float(temp_in_kelvin) - KELVIN
        return int(round(temp_in_celsius, 0))


weather = Weather()
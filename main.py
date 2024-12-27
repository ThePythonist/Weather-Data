import requests
from datetime import datetime
from queries import save_weather_data


def normalizer(data):
    temp = data['main']['temp'] - 273.15
    dt = str(datetime.fromtimestamp(data['dt']))
    # return name, date, temp, humidity, wind_speed
    return {"name": data['name'], "date": dt, "temp": temp, "humidity": data['main']['humidity'],
            "wind_speed": data['wind']['speed']}


def get_weather_data(city):
    api_key = "ce28524cced047e5c594dabe55a408be"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    data = response.json()
    data = normalizer(data)
    save_weather_data(data)
    print(data)


get_weather_data(city=input("Enter a city name : "))

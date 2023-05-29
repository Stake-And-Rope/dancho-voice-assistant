import requests


def retrieve_data_about_the_weather_forecast():
    """
    This function retrieves data from the internet and returns a string about the current weather
     in the city of Sofia.
    Raw information has the following example contents:
    {'coord': {'lon': 23.3242, 'lat': 42.6975},
    'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}],
    'base': 'stations', 'main': {'temp': 294.41, 'feels_like': 293.92, 'temp_min': 294.41,
    'temp_max': 294.98, 'pressure': 1018, 'humidity': 51},
    'visibility': 10000, 'wind': {'speed': 3.09, 'deg': 90}, 'clouds': {'all': 75},
    'dt': 1684938048,
    'sys': {'type': 2, 'id': 2033225, 'country': 'BG', 'sunrise': 1684897012, 'sunset': 1684950627},
    'timezone': 10800, 'id': 727011, 'name': 'Sofia', 'cod': 200}

    """
    weather_forecast_text = ''

    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = "Sofia"

    url = base_url + "q=" + city + "&appid=" + "f4e5b648421e4d481828851a5763cbf1"
    response = requests.get(url).json()
    weather_type = response['weather'][0]['main']
    weather_type_further_description = response['weather'][0]['description']
    current_temperature_in_celsius = response['main']['temp'] - 273.15
    feels_like_in_celsius = response['main']['feels_like'] - 273.15
    temperature_min_celsius = response['main']['temp_min'] - 273.15
    temperature_max_celsius = response['main']['temp_max'] - 273.15

    weather_forecast_text = f'Today will be {weather_type} with {weather_type_further_description}. The current temperature is {current_temperature_in_celsius:.1f} degrees celsius and will feel like {feels_like_in_celsius:.1f} degrees celsius. The minimal temperature will be {temperature_min_celsius:.1f} degrees celsius. The maximal temperature will be {temperature_max_celsius:.1f} degrees celsius. '
    print(weather_forecast_text)
    return weather_forecast_text


# retrieve_data_about_the_weather_forecast()
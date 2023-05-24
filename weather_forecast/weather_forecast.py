import datetime
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

    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    CITY = "Sofia"

    url = BASE_URL + "q=" + CITY + "&appid=" + "f4e5b648421e4d481828851a5763cbf1"
    response = requests.get(url).json()
    day = datetime.datetime.today().now()
    day = (str(day).split(" "))[0].split("-")[2]
    weather_type = response['weather'][0]['main']
    weather_type_further_description = response['weather'][0]['description']
    current_temperature_in_celsius = response['main']['temp'] - 273.15
    feels_like_in_celsius = response['main']['feels_like'] - 273.15
    temperature_min_celsius = response['main']['temp_min'] - 273.15
    temperature_max_celsius = response['main']['temp_max'] - 273.15
    pressure_hpa = response['main']['pressure']
    relative_air_humidity_in_percent = response['main']['humidity']
    wind_degrees = response['wind']['deg']
    wind_speed = response['wind']['speed']

    wind_compass_rose = {
        'North': range(0, 12),
        'North by East': range(12, 22),
        'North-Northeast': range(22, 33),
        'Northeast by North': range(33, 45),
        'Northeast': range(45, 56),
        'Northeast by East': range(56, 67),
        'East-Northeast': range(67, 78),
        'East': range(78, 90),
        'East by South': range(90, 101),
        'East-Southeast': range(101, 112),
        'Southeast by East': range(112, 123),
        'Southeast': range(123, 135),
        'Southeast by South': range(135, 146),
        'South-Southeast': range(146, 157),
        'South by East': range(157, 168),
        'South': range(168, 180),
        'South by West': range(180, 191),
        'South-Southwest': range(191, 202),
        'Southwest by South': range(202, 213),
        'Southwest': range(213, 225),
        'Southwest by West': range(225, 236),
        'West-Southwest': range(236, 247),
        'West by South': range(247, 258),
        'West': range(258, 270),
        'West by North': range(270, 281),
        'West-Northwest': range(281, 292),
        'Northwest by West': range(292, 303),
        'Northwest': range(303, 315),
        'Northwest by North': range(315, 326),
        'North-Northwest': range(326, 337),
        'North by West': range(337, 361)
        }

    wind_direction = [direction for direction, degrees in wind_compass_rose.items() if wind_degrees in degrees]

    weather_forecast_text = f'Today will be {weather_type} with {weather_type_further_description}.' \
                            f'The current temperature is {current_temperature_in_celsius:.1f} degrees celsius ' \
                            f'and will feel like {feels_like_in_celsius:.1f} degrees celsius. ' \
                            f'The minimal temperature will be {temperature_min_celsius:.1f} degrees celsius. ' \
                            f'The maximal temperature will be {temperature_max_celsius:.1f} degrees celsius. ' \
                            f'Atmospheric pressure will be {pressure_hpa} hpa.' \
                            f'Humidity will be {relative_air_humidity_in_percent} percent.' \
                            f'The wind will be {wind_direction[0]} with a speed of {wind_speed:.1f} kilometers' \
                            f' per hour.'
    print(weather_forecast_text)
    return weather_forecast_text

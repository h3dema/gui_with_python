"""
    obtem informacoes de tempo da internet

"""
import urllib.parse
import datetime
import requests


def get_weather(lat: float, lon: float,
                day: datetime.datetime = datetime.datetime.now(),
                ) -> dict:
    """
    ref. https://open-meteo.com/en/docs

    {'latitude': -12.875, 'longitude': -38.5, 'generationtime_ms': 8.585929870605469, 'utc_offset_seconds': -10800,
     'timezone': 'America/Sao_Paulo', 'timezone_abbreviation': '-03',
     'elevation': 0.0,
     'daily_units': {'time': 'iso8601',
                     'weathercode': 'wmo code',
                     'temperature_2m_max': '°C',
                     'temperature_2m_min': '°C',
                     'sunrise': 'iso8601',
                     'sunset': 'iso8601',
                     'precipitation_sum': 'mm',
                     'rain_sum': 'mm',
                     'showers_sum': 'mm',
                     'snowfall_sum': 'cm',
                     'precipitation_hours': 'h',
                     'winddirection_10m_dominant': '°'},
     'daily': {'time': ['2022-10-23'],
               'weathercode': [3],
               'temperature_2m_max': [29.0],
               'temperature_2m_min': [23.9],
               'sunrise': ['2022-10-23T05:03'],
               'sunset': ['2022-10-23T17:33'],
               'precipitation_sum': [1.1],
               'rain_sum': [0.0],
               'showers_sum': [1.1],
               'snowfall_sum': [0.0],
               'precipitation_hours': [6.0],
               'winddirection_10m_dominant': [88]
               }
    }
    """
    today = day.strftime("%Y-%m-%d")
    timezone = urllib.parse.quote("America/Sao_Paulo")
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=weathercode,temperature_2m_max,temperature_2m_min,sunrise,sunset,precipitation_sum,rain_sum,showers_sum,snowfall_sum,precipitation_hours,winddirection_10m_dominant&timezone={timezone}&start_date={today}&end_date={today}"
    # call the API
    resp = requests.get(url)
    # if sucess, return the response
    if 200 <= resp.status_code < 300:
        return resp.json()
    else:
        return {}


if __name__ == "__main__":
    weather_info = get_weather(lat=-13.01009515567156, lon=-38.532752829369244)  # Farol da Barra, Salvador/BA
    if len(weather_info) > 0:
        print("Weather info:")
        for k, v in zip(weather_info["daily_units"], weather_info["daily"]):
            print(
                f"{k.replace('_', ' '):>30s}: {weather_info['daily'][v][0]}{weather_info['daily_units'][k]}")
    else:
        print("No weather info:")

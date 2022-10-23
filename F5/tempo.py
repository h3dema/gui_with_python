"""
    tela com as informações sobre o tempo

"""
import os
import datetime
import PySimpleGUI as sg

from weathercrawler import get_weather


_map = {'precipitation_sum': 'Precipitação',
        'rain_sum': 'Chuva',
        'precipitation_hours': 'Previsão de chuva',
        }

path_imgs = os.path.join(os.path.dirname(__file__), "imgs")

imgs = {
    "clear_sky": os.path.join(path_imgs, "clear_sky.png"),
    "drizzle": os.path.join(path_imgs, "drizzle.png"),
    "fog": os.path.join(path_imgs, "fog.png"),
    "grains": os.path.join(path_imgs, "grains.png"),
    "mainly_clear": os.path.join(path_imgs, "mainly_clear.png"),
    "rain": os.path.join(path_imgs, "rain.png"),
    "snow": os.path.join(path_imgs, "snow.png"),
    "thunder": os.path.join(path_imgs, "thunder.png"),
    "no": os.path.join(path_imgs, "no.png"),  # don't know
}

def img_type_map(code):
    if code == 0:
        return "clear_sky"
    elif code in [1, 2, 3]:
        return "mainly_clear"
    elif code in [45, 48]:
        return "fog"
    elif code in [51, 53, 55]:
        return "drizzle"
    elif code in [61, 63, 65, 80, 81, 82]:
        return "rain"
    elif code in [71, 73, 75]:
        return "snow"
    elif code in [95, 96, 99]:
        return "thunder"
    elif code == 77:
        return "grains"
    else:
        return "no"


def format_day(day: str) -> str:
    # YYYY-MM-DD --> DD/MM/YYYY
    d = datetime.datetime.strptime(day, "%Y-%m-%d").strftime("%d/%m/%Y")
    return d


def format_hour(dt: str) -> str:
    # '2022-10-23T05:03 --> HH:MM
    d = dt.split("T")[1]
    return d


if __name__ == '__main__':
    # localização
    local = "Farol da Barra, Salvador/BA"
    lat = -13.01009515567156
    lon = -38.532752829369244
    # weather_info = get_weather(lat=lat, lon=lon)
    weather_info = {'latitude': -12.875, 'longitude': -38.5, 'generationtime_ms': 0.43189525604248047, 'utc_offset_seconds': -10800, 'timezone': 'America/Sao_Paulo', 'timezone_abbreviation': '-03', 'elevation': 0.0, 'daily_units': {'time': 'iso8601', 'weathercode': 'wmo code', 'temperature_2m_max': '°C', 'temperature_2m_min': '°C', 'sunrise': 'iso8601', 'sunset': 'iso8601', 'precipitation_sum': 'mm', 'rain_sum': 'mm', 'showers_sum': 'mm',
                                                                                                                                                                                                                                        'snowfall_sum': 'cm', 'precipitation_hours': 'h', 'winddirection_10m_dominant': '°'}, 'daily': {'time': ['2022-10-23'], 'weathercode': [3], 'temperature_2m_max': [29.2], 'temperature_2m_min': [23.9], 'sunrise': ['2022-10-23T05:03'], 'sunset': ['2022-10-23T17:33'], 'precipitation_sum': [0.8], 'rain_sum': [0.0], 'showers_sum': [0.8], 'snowfall_sum': [0.0], 'precipitation_hours': [6.0], 'winddirection_10m_dominant': [85]}}

    img_type = img_type_map(weather_info["daily"]["weathercode"][0])
    weather_img = imgs[img_type]

    # Add your new theme colors and settings
    # see more at https://www.pysimplegui.org/en/latest/cookbook/#making-changes-to-themes-adding-your-own-themes
    # select color at https://www.w3schools.com/colors/colors_picker.asp
    my_new_theme = {'BACKGROUND': '#ffffff',
                    'TEXT': '#000000',
                    'INPUT': '#c7e78b',
                    'TEXT_INPUT': '#000000',
                    'SCROLL': '#c7e78b',
                    'BUTTON': ('white', '#709053'),
                    'PROGRESS': ('#01826B', '#D0D0D0'),
                    'BORDER': 1,
                    'SLIDER_DEPTH': 0,
                    'PROGRESS_DEPTH': 0}

    # Add your dictionary to the PySimpleGUI themes
    sg.theme_add_new('MyNewTheme', my_new_theme)
    sg.theme('My New Theme')

    infos = [[sg.Text(v, key=f"lab-{k}-"),
              sg.Text(weather_info["daily"][k][0]),
              sg.Text(weather_info["daily_units"][k], key=f"met-{k}")] for k, v in _map.items()]

    layout_local = [sg.Column([[sg.Text(f"{local}", font=["bold", 16])],
                               [sg.Text(f"Latitude: {lat:.2f} Longitude: {lon:.2f}")],
                               [sg.Push(),
                                sg.Text(format_day(weather_info["daily"]["time"][0]), font=["bold", 10]),
                                sg.Push(),
                                ],
                               ]),
                    sg.Image(weather_img, key="-type-"),
                    ]

    layout_temp_rain = [sg.Image(os.path.join(path_imgs, "temp.png"), key="-type-"),
                   sg.Column([[sg.Text("Mínima: {}{}".format(weather_info["daily"]["temperature_2m_max"][0], weather_info["daily_units"]["temperature_2m_max"])), ],
                              [sg.Text("Máxima: {}{}".format(weather_info["daily"]["temperature_2m_min"][0], weather_info["daily_units"]["temperature_2m_min"]))],
                              ]),
                   sg.Frame("", [[sg.Column(infos)]], border_width=1, vertical_alignment="top")
                   ]

    layout_sun = [sg.Image(os.path.join(path_imgs, "sun_rise.png")),
                  sg.Text(format_hour(weather_info["daily"]["sunrise"][0])),
                  sg.Image(os.path.join(path_imgs, "sun_set.png")),
                  sg.Text(format_hour(weather_info["daily"]["sunset"][0])),
                  ]

    layout = [
        [sg.VPush()],
        layout_local,
        layout_temp_rain,
        layout_sun,
        # infos,
        [sg.Text("Direção do vento predominante: {}{}".format(
            weather_info["daily"]["winddirection_10m_dominant"][0],
            weather_info["daily_units"]["winddirection_10m_dominant"]
            ))],
        [sg.VPush()],
    ]

    #Create the Window
    window = sg.Window('Cobertura do Tempo', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '-close-':  # if user closes window or clicks cancel
            break
    window.close()

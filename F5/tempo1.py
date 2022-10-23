"""
    tela com as informações sobre o tempo

"""
import os
import PySimpleGUI as sg

from weathercrawler import get_weather


_map = {'time': 'dia',
        'temperature_2m_max': 'Temperatura (máx)',
        'temperature_2m_min': 'Temperatura (min)',
        'sunrise': 'Nascer do sol',
        'sunset': 'Por do sol',
        'precipitation_sum': 'Precipitação',
        'rain_sum': 'Chuva',
        'precipitation_hours': 'Previsão de chuva',
        'winddirection_10m_dominant' : 'Direção do vento predominante',
        }

path = os.path.dirname(__file__)
imgs = {
    "clear_sky": os.path.join(path, "imgs", "clear_sky.png"),
    "drizzle": os.path.join(path, "imgs", "drizzle.png"),
    "fog": os.path.join(path, "imgs", "fog.png"),
    "grains": os.path.join(path, "imgs", "grains.png"),
    "mainly_clear": os.path.join(path, "imgs", "mainly_clear.png"),
    "rain": os.path.join(path, "imgs", "rain.png"),
    "snow": os.path.join(path, "imgs", "snow.png"),
    "thunder": os.path.join(path, "imgs", "thunder.png"),
    "no": os.path.join(path, "imgs", "no.png"),  # don't know
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


if __name__ == '__main__':
    # localização
    local = "Farol da Barra, Salvador/BA"
    lat = -13.01009515567156
    lon = -38.532752829369244
    weather_info = get_weather(lat=lat, lon=lon)

    img_type = img_type_map(weather_info["daily"]["weathercode"][0])
    weather_img = imgs[img_type]
    print(weather_img)

    infos = [[sg.Text(v, key=f"lab-{k}-", background_color="white", text_color="black"),
              sg.Text(weather_info["daily"][k][0], key=k, background_color="white", text_color="black"),
              sg.Text(weather_info["daily_units"][k], key=f"met-{k}", background_color="white", text_color="black")] for k, v in _map.items()]

    layout = [
        [sg.VPush(background_color="white")],
        [sg.Text(f"{local} - Latitude: {lat:.2f} Longitude: {lon:.2f}", background_color="white", text_color="black")],
        infos,
        [sg.Image(weather_img, key="-type-")],
        [sg.VPush(background_color="white")],
    ]

    #Create the Window
    window = sg.Window('Cobertura do Tempo', layout, background_color="white")
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '-close-':  # if user closes window or clicks cancel
            break
    window.close()

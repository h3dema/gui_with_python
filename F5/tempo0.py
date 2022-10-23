"""
    tela com as informações sobre o tempo

"""

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


if __name__ == '__main__':
    # localização
    local = "Farol da Barra, Salvador/BA"
    lat = -13.01009515567156
    lon = -38.532752829369244
    weather_info = get_weather(lat=lat, lon=lon)

    infos = [[sg.Text(v, key=f"lab-{k}-"),
              sg.Text(weather_info["daily"][k][0], key=k),
              sg.Text(weather_info["daily_units"][k], key=f"met-{k}")] for k, v in _map.items()]

    layout = [
        [sg.VPush()],
        [sg.Text(f"Local: {local} - Latitude: {lat:.2f} Longitude: {lon:.2f}")],
        infos,
        [sg.VPush()],
    ]

    #Create the Window
    window = sg.Window('Cobertura do Tempo', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '-close-':  # if user closes window or clicks cancel
            break
    window.close()

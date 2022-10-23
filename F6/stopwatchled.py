import os
import PySimpleGUI as sg

from stopwatch import time_convert
from stopwatch import CountTime

PATH = os.path.dirname(__file__)

imgs = {"0": os.path.join(PATH, "imgs/0.png"),
        "1": os.path.join(PATH, "imgs/1.png"),
        "2": os.path.join(PATH, "imgs/2.png"),
        "3": os.path.join(PATH, "imgs/3.png"),
        "4": os.path.join(PATH, "imgs/4.png"),
        "5": os.path.join(PATH, "imgs/5.png"),
        "6": os.path.join(PATH, "imgs/6.png"),
        "7": os.path.join(PATH, "imgs/7.png"),
        "8": os.path.join(PATH, "imgs/8.png"),
        "9": os.path.join(PATH, "imgs/9.png"),
        ":": os.path.join(PATH, "imgs/sep1.png"),
        ".": os.path.join(PATH, "imgs/sep2.png"),
        }


if __name__ == '__main__':
    button_size = (12, 3)

    layout_clock = [sg.Push(background_color="white"),
                    sg.Image(imgs["0"], key="-H1-"),
                    sg.Image(imgs["0"], key="-H2-"),
                    sg.Image(imgs[":"], key="-sep1-"),
                    sg.Image(imgs[":"], key="-sep1-"),
                    sg.Image(imgs["0"], key="-M1-"),
                    sg.Image(imgs["0"], key="-M2-"),
                    sg.Image(imgs[":"], key="-sep2-"),
                    sg.Image(imgs["0"], key="-S1-"),
                    sg.Image(imgs["0"], key="-S2-"),
                    sg.Image(imgs["."], key="-sep3-"),
                    sg.Image(imgs["0"], key="-D1-"),
                    sg.Push(background_color="white")
                    ]

    layout = [[sg.VPush(background_color="white")],
              layout_clock,
              [sg.Push(background_color="white"),
               sg.Button("Start", key="-start-", size=button_size),
               sg.Button("Stop", key="-stop-",
                         size=button_size, disabled=True),
               sg.Button("Reset", key="-reset-",
                         size=button_size, disabled=True),
               sg.Button("Cancel", key="-close-", size=button_size),
               sg.Push(background_color="white"),
               ],
              [sg.VPush(background_color="white")],
              ]

    #Create the Window
    window = sg.Window('Cronometro LED', layout, background_color="white")

    def update_clock(time_lapsed):
        value = "{:02d}{:02d}{:02d}{:01d}".format(
            *time_convert(time_lapsed))
        for v, k in zip(value, ["-H1-", "-H2-", "-M1-", "-M2-", "-S1-", "-S2-", "-D1-"]):
            window[k].update(filename=imgs[v])

    # Event Loop to process "events" and get the "values" of the inputs
    crono = None
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '-close-':  # if user closes window or clicks cancel
            break
        elif event == "-start-":
            window["-start-"].update(disabled=True)
            window["-stop-"].update(disabled=False)
            if crono is None:
                crono = CountTime(update_clock)
                crono.start()
            else:
                crono.restart()
        elif event == "-stop-":
            window["-start-"].update(disabled=False)
            window["-stop-"].update(disabled=True)
            crono.stop()
        elif event == "-reset-":
            crono.reset()

        window["-reset-"].update(disabled=crono is None)
    window.close()

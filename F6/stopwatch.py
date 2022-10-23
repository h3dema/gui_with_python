import time
import PySimpleGUI as sg

from repeattimer import RepeatTimer


def time_convert(dt: float):
    """ convert time in seconds to hh:mm:ss.d

    Args:
        sec (int): _description_

    Returns:
        _type_: _description_
    """

    sec = int(dt)
    dsec = int((dt - sec) * 10)  # tenths of seconds

    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60

    return int(hours), int(mins), sec, dsec


class CountTime(object):

    def __init__(self, fupdate):
        """ guardar funcao de atualizacao e inicializar variaveis """
        self.update = fupdate
        self.time_lapsed = 0

    def _create_start_thread(self):
        """ Timer não permite restart.
            Tem que ser criado toda a vez depois de timer.cancel()
        """
        self.thread = RepeatTimer(0.1, self.count)
        self.thread.start()

    def reset(self):
        """ zera o timer e atualiza o valor na tela """
        self.time_lapsed = 0  # zero the counting timer
        self.start_time = time.time()  # reset the initial time
        self.update(self.time_lapsed)

    def start(self):
        """ inicia a contagem do timer na tela """
        # get initial time
        self.start_time = time.time()
        # start count
        self._create_start_thread()

    def count(self):
        """ atualiza a contagem na tela """
        end_time = time.time()
        time_lapsed = end_time - self.start_time
        self.update(self.time_lapsed + time_lapsed)
        return time_lapsed

    def stop(self):
        """ para o cronometro, mas nao zera (assim pode reiniciar) """
        time_lapsed = self.count()
        self.time_lapsed += time_lapsed
        self.thread.cancel()  # para reiniciar o timer, precisa criar de novo a thread

    def restart(self):
        """ reinicia a contagem se estiver parado """
        if not self.thread.is_alive():
            self.start_time = time.time()  # restart interval
            self._create_start_thread()


if __name__ == '__main__':
    button_size = 7

    layout = [[sg.VPush()],
              [sg.Push(),
               sg.Text("00:00:00.0", key="-clock-", font=["Arial Bold", 40]),
               sg.Push()
               ],
              [sg.Push(),
               sg.Button("Start", key="-start-", size=button_size),
               sg.Button("Stop", key="-stop-", size=button_size, disabled=True),
               sg.Button("Reset", key="-reset-", size=button_size, disabled=True),
               sg.Button("Cancel", key="-close-", size=button_size),
               sg.Push(),
               ],
              [sg.VPush()],
              ]

    #Create the Window
    window = sg.Window('Cronometro', layout)

    def update_clock(time_lapsed):
        value = "{:02d}:{:02d}:{:02d}.{:01d}".format(*time_convert(time_lapsed))
        window["-clock-"].update(value=value)

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

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


class CountTime(object):

    def __init__(self, fupdate):
        """ guardar funcao de atualizacao e inicializar variaveis """

    def reset(self):
        """ zera o timer e atualiza o valor na tela """

    def start(self):
        """ inicia a contagem do timer na tela """

    def count(self):
        """ atualiza a contagem na tela """

    def stop(self):
        """ para o cronometro, mas nao zera (assim pode reiniciar) """

    def restart(self):
        """ reinicia a contagem se estiver parado """


if __name__ == '__main__':
    button_size = 7

    layout = [[# linha com o timer
              ],
              [# linha com os botoes de controle: start, stop, reset, exit
              ],
              ]

    #Create the Window
    window = sg.Window('Cronometro', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    crono = None
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '-close-':  # if user closes window or clicks cancel
            break
        elif event == "-start-":
            """ inicia o cronometro """
        elif event == "-stop-":
            """ para a contagem """
        elif event == "-reset-":
            """ zera cronometro """

    window.close()

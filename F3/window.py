"""
  Configurando o objeto Windows

"""
import PySimpleGUI as sg

layout = [[]]

# sg.theme("SystemDefault")
win = sg.Window("First simple window",
                layout=[layout],
                margins=[10, 10],  # Esta é a margem interna dentro da janela
                resizable=True,
                )

win.read()

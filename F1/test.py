"""
Passos para utilizar:
====================

1- instalar tkinter (no ubuntu)

    sudo apt install python3-tk

2- (opcional) criar ambiente virtual para python e ativa-lo

    python3 -m venv .venv
    source .venv/bin/activate

3- instalar PySimpleGUI

    pip3 install pysimplegui

"""

import PySimpleGUI as sg

sg.theme("DarkAmber")
sg.Window("First simple window",
          layout=[[]],
          margins=[100, 100],  # Esta é a margem interna dentro da janela
          ).read()

# comente a linha #25 acima e rode o programa para ver o que acontece.
# -- a janela fica minúscula!

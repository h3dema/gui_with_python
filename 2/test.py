"""
Passos para utilizar:
====================

1- (opcional) criar ambiente virtual para python e ativa-lo no powershell

    python -m venv .venv
    .\venv\bin\activate.ps1

2- instalar PySimpleGUI

    pip install pysimplegui

"""

import PySimpleGUI as sg

sg.theme("DarkAmber")
sg.Window("First simple window",
          layout=[[]],
          margins=[100, 100],
          resizable=True,
          ).read()


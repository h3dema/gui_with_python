"""
  Configurando o objeto Windows

"""
import typing
import PySimpleGUI as sg


def campo(texts: list,
          inputs: list,
          sizes: typing.Optional[list] = None,
          ):
    assert len(texts) == len(
        inputs), "Inputs e títulos devem ter o mesmo tamanho"
    _elements = [sg.Column([[sg.Text(_text)], [sg.Input(key=_input)]])
                 for _text, _input in zip(texts, inputs)]
    return sg.Frame("", [_elements], border_width=1)


button_size = 10
title_font = ["Arial Bold", 20]

# define os botoes na parte inferior da tela
layout_botoes = [sg.Push(),
                 sg.Button("Salvar", key="-save-", size=button_size),
                 sg.Button("Cancelar", key="-canc-", size=button_size),
                 sg.Button("Fechar", key="-fechar-", size=button_size),
                 sg.Push()]

#
# layout initial
#
# linha 1 - titulo
# linha 2 - grupo para o conteúdo dos dados da empresa
# linha 3 - grupo para os dados de faturamento
# linha 4 - botoes
#
layout = [[sg.Push(), sg.Text("Ficha de Cliente", font=title_font), sg.Push()],
          # empresa
          [sg.Frame("Empresa", [[]])],
          # faturamento
          [sg.Frame("Faturamento", [[]])],
          layout_botoes,
          ]

# sg.theme("SystemDefault")
win = sg.Window("Cadastro Simples",
                layout=[layout],
                margins=[10, 10],  # Esta é a margem interna dentro da janela
                resizable=True,
                )

while True:
    event, values = win.read()
    if event == sg.WIN_CLOSED or event == "-fechar-":
        break

"""
    1 - Configurando o objeto Windows
    2 - Adicionando os campos

"""
# %%
import typing
import PySimpleGUI as sg

def campo(text: str,
          in_key: str,
          in_def: str = "",
          size: int = None,  # largura em caracteres
          ):
    # um por linha
    if size is None:
        # para autodimensionar, deve passar tupla com 2 valores (largura, em caracteres, e altura, em linha)
        size = [None, None]
    _campo = sg.Frame("", [
        [sg.Column([[sg.Text(text, size=size)],  # primeira linha
                    [sg.Input(in_def, key=in_key, size=size)]  # segunda linha
                    ])
         ]
        ]
    )
    return _campo


button_size = 10
title_font = ["Arial Bold", 20]
# %%

layout_razao = campo("Razão Social", "-razao-")


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
          [sg.Push(), sg.Frame("Empresa", [[layout_razao]]), sg.Push(), ],
          # faturamento
          [sg.Push(), sg.Frame("Faturamento", [[]]), sg.Push(), ],
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

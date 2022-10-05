"""
  Configurando o objeto Windows

"""
import random
import PySimpleGUI as sg


def label(name, NAME_SIZE=20):
    dots = NAME_SIZE - len(name) - 2
    return sg.Text(f"{name} {'•'*dots}",
                   size=(NAME_SIZE, 1),
                   justification='r',
                   # pad=(0, 0),
                   # font='Courier 10'
                   )


texto_surpresa = sg.Text("Texto surpresa!",
                         text_color="white",
                         background_color="blue",
                         justification="right",  # Valid choices = left, right, center
                         visible=random.random() > 0.5,
                         size=100,
                         )

nome_produto = "PySimpleGui"

bt_extra = sg.Button("Extra", size=10, disabled=True)
botoes = [[sg.Button('Ok', size=10, bind_return_key=True), sg.Button('Cancelar', size=10), bt_extra]]

inputs = [[label("Nome original:"), sg.Text(nome_produto)],
          [label("Nome alterado:"), sg.Input(nome_produto)],
          ]

layout = [[sg.VPush()],
          [sg.Stretch(), sg.Text("Renomear o produto", font=["Arial Bold", 15]), sg.Stretch(), ],
          [sg.Push(), sg.Column(inputs), sg.Push(), ],
          [sg.VPush()],
          [sg.Stretch(), sg.Column(botoes, element_justification="right"), sg.Stretch(), ],
          # [sg.Ok(), sg.Cancel("Cancelar")],
          [texto_surpresa],
          [sg.VPush()],
          ]

# sg.theme("SystemDefault")
win = sg.Window("First simple window",
                layout=[layout],
                margins=[10, 10],  # Esta é a margem interna dentro da janela
                resizable=True,
                size=[600, 200],  # Este é o tamanho da janela
                location=[2000, 200],
                font=["Calibri", 12],  # afeta o texto
                icon="icon.ico",
                )
while True:
    event, values = win.read()

    if event in ["Ok", "Cancelar"]:
        bt_extra.update(disabled=False)
    elif event == sg.WIN_CLOSED or event == "Extra":
        break

"""
    1 - Configurando o objeto Windows
    2 - Adicionando os campos

"""
# %%
import typing
import PySimpleGUI as sg

DEFAULT_SIZE = [None, None]

def campos(texts: list,
          in_keys: list,
          in_defs: list = [],
          sizes: list = []
          ):
    # verifica tamanhos
    assert len(texts) == len(in_keys), "Labels e inputs devem ter o mesmo numero"
    if len(in_defs) == 0 or len(in_defs) != len(in_keys):
        in_defs = ["" for _ in in_keys]

    if len(sizes) == 0 or len(in_defs) != len(in_keys):
        sizes = [DEFAULT_SIZE for _ in in_keys]
    for i in range(len(sizes)):
        if sizes[i] is None:
            sizes[i] = DEFAULT_SIZE

    # coloca o label em uma linha e o input na linha de baixo
    _columns = [sg.Column([[sg.Text(_text,
                                    size=_size,
                                    pad=[[0, 0], [0, 0]])],
                           [sg.Input(_def,
                                     key=_key,
                                     size=_size,
                                     pad=[[0, 0], [0, 0]])],
                           ])
                for _text, _def, _key, _size in zip(texts, in_defs, in_keys, sizes)]

    # monta bloco: cada par (label, input) é uma coluna dentro do frame
    _campos = sg.Frame("",
                       [[sg.Column([_columns])
         ]
         ],
        border_width= 0
    )
    return _campos


button_size = 10
title_font = ["Arial Bold", 20]
# %%

#
# cadastro principal da empresa
#
layout_razao = campos(["Razão Social"], ["-razao-"], sizes=[60])
layout_cad = campos(["CNPJ", "Inscrição"], ["-cnpj-", "-inscr-"], sizes=[25, 25])
layout_log = campos(["Rua"], ["-log-"], sizes=[60])
layout_end = campos(["Cidade", "Estado", "CEP", "Fone"],
                    ["-cid-", "-est-", "-cep-", "-fone-"],
                    sizes=[30, 7, 10, 10])

layout_emp = [[layout_razao],
              [layout_cad],
              [layout_log],
              [layout_end]
              ]

#
# cadastro dos dados de faturamento da empresa
#
layout_fat_cad = campos(["CNPJ", "Inscrição"], [
                    "-fat-cnpj-", "-fat-inscr-"], sizes=[25, 25])
layout_fat_log = campos(["Rua"], ["-fat-log-"], sizes=[60])
layout_fat_end = campos(["Cidade", "Estado", "CEP", "Fone"],
                        ["-fat-cid-", "-fat-est-", "-fat-cep-", "-fat-fone-"],
                        sizes=[30, 7, 10, 10])

layout_fat = [[layout_fat_cad],
              [layout_fat_log],
              [layout_fat_end],
              ]

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
layout = [[sg.VPush()],
          [sg.Push(), sg.Text("Ficha de Cliente", font=title_font), sg.Push()],
          # empresa
          [sg.Push(), sg.Frame("Empresa", [[sg.Column(layout_emp)]]), sg.Push(), ],
          # faturamento
          [sg.Push(),
           sg.Frame("Faturamento", [[sg.Column(layout_fat)]],),
           sg.Push(), ],
          [sg.VPush()],
          layout_botoes,
          [sg.VPush()],
          ]

# sg.theme("SystemDefault")
win = sg.Window("Cadastro Simples",
                layout=[layout],
                margins=[5, 5],  # Esta é a margem interna dentro da janela
                resizable=True,
                )

while True:
    event, values = win.read()
    if event == sg.WIN_CLOSED or event == "-fechar-":
        break

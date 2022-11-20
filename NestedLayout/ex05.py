import PySimpleGUI as sg

if __name__ == '__main__':

    layout = [[sg.Button(button_color="red", size=(15, 10)),
               sg.Column([[sg.Button(button_color="blue", size=(10, 5))],
                          [sg.Button(button_color="red", size=(10, 5))]
                          ])
               ],
              [sg.Column([[sg.Button(button_color="blue", size=(10, 5))],
                          [sg.Button(button_color="red", size=(10, 5))]
                          ]),
               sg.Button(button_color="red", size=(15, 10))]
              ]

    window = sg.Window('Nested Layout', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '-close-':  # if user closes window or clicks cancel
            break
    window.close()

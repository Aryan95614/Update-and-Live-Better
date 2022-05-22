
import PySimpleGUI as sg


def a(dat):
    sg.theme('DarkGreen3')
    layout = [[sg.Text("Information for you")],
              ([sg.Text(dat[i])] for i in range(len(dat) // 2)),
              ([sg.Text(dat[i])] for i in range(len(dat) // 2, len(dat))),
              [sg.Button("OK")]]

    window = sg.Window("Demo", layout, size = (1600, 500))

    while True:
        event, values = window.read()

        if event == "OK" or event == sg.WIN_CLOSED:
            break

    window.close()
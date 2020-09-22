import random
import string
import PySimpleGUI as sg
import clipboard


def id_generator(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


generated_result = id_generator(25)
clipboard.copy(generated_result)

sg.theme('DarkAmber')
layout = [[sg.Text('Generated Password')],
          [sg.InputText(generated_result, key='-OUTPUT-')],
          [sg.Button('Generate')]]

window = sg.Window('Password Generation Gadget', layout, icon="app.ico")

load = False
while True:
    event, values = window.read()
    if event is None:
        break
    if event == sg.WIN_CLOSED or event == 'Generate':
        generated_result = id_generator(25)
        clipboard.copy(generated_result)
        window['-OUTPUT-'].update(generated_result)

window.close()

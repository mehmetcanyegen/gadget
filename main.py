import random
import string
import PySimpleGUI as sg
import clipboard


def id_generator(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

number_size = 12
generated_result = id_generator(number_size)
clipboard.copy(generated_result)

# sg.theme('DarkAmber')
layout = [[sg.Text('Generated Password', size=(31,1)), sg.Text('Character Size') ],
          [
              sg.InputText(generated_result, key='-OUTPUT-', size=(30, 1)),
              sg.Button("-5", size=(2, 1), key='_BUTTON_DEC_5_'),
              sg.Button("-1", size=(2, 1), key='_BUTTON_DEC_'),
              sg.Text(number_size, key='-NUMBER_SIZE-', size=(5, 1)),
              sg.Button("+1", size=(2, 1), key='_BUTTON_INC_'),
              sg.Button("+5", size=(2, 1), key='_BUTTON_INC_5_')
          ],
          [
            sg.Radio(text='Brutal', group_id=1, key="_LEVEL_0_"),
           sg.Radio(text='Hard', group_id=1, key="_LEVEL_1_", default=True),
           sg.Radio(text='Moderate', group_id=1, key="_LEVEL_2_"),
           sg.Radio(text='Simple',group_id=1, key="_LEVEL_3_"),
           ],
          [sg.Button('Generate', size=(22, 1))]]

window = sg.Window('Password Generation Gadget', layout, icon="app.ico")

load = False
while True:
    event, values = window.read()

    if event is None:
        break
    if event == sg.WIN_CLOSED or event == 'Generate':
        chars = None
        if values["_LEVEL_0_"]:
            chars = string.ascii_letters + string.digits + string.punctuation
        if values["_LEVEL_1_"]:
            chars = string.ascii_letters + string.digits
        if values["_LEVEL_2_"]:
            chars = string.ascii_lowercase
        if values["_LEVEL_3_"]:
            chars = string.digits
        generated_result = id_generator(size=number_size, chars=chars)
        clipboard.copy(generated_result)
        window['-OUTPUT-'].update(generated_result)

    if event == '_BUTTON_DEC_':
        number_size = int(number_size) - 1
        if number_size < 1:
            number_size = 1
        window['-NUMBER_SIZE-'].update(number_size)

    if event == '_BUTTON_DEC_5_':
        number_size = int(number_size) - 5
        if number_size < 1:
            number_size = 1
        window['-NUMBER_SIZE-'].update(number_size)

    if event == '_BUTTON_INC_':
        number_size = int(number_size) + 1
        window['-NUMBER_SIZE-'].update(number_size)

    if event == '_BUTTON_INC_5_':
        number_size = int(number_size) + 5
        window['-NUMBER_SIZE-'].update(number_size)


window.close()

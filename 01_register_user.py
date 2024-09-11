from PySimpleGUI import as sg
#layout
sg.theme('Reddit')
layout = [
    [sg.text('User'),sg.input(key='user',size=(20,1))],
    [sg.text('password'),sg.input(key='password',password_char='*',size=(20,1))],
    [sg.checkbox('save login?')],
    [sg.button('to enter')]
]
#window
window = sg.window('login screen', layout)
#action
while true:
    actions, values = window.read()
    if actions == sg.WINDOW_CLOSED:
        break
    if actions == 'to enter':
        if values['user'] == 'name' and values['password'] == '123456':
                print('Welcome')

#OR_THE_NEXT_CODE

import PySimpleGUI as sg

# layout
sg.theme('Reddit')
layout = [
    [sg.Text('User'), sg.Input(key='user', size=(20, 1))],
    [sg.Text('Password'), sg.Input(key='password', password_char='*', size=(20, 1))],
    [sg.Checkbox('Save login?')],
    [sg.Button('To Enter')]
]

# window
window = sg.Window('Login Screen', layout)

# action
while True:
    events, values = window.read()
    if events == sg.WIN_CLOSED:
        break
    if events == 'To Enter':
        if values['user'] == 'name' and values['password'] == '123456':
            print('Welcome')

window.close()

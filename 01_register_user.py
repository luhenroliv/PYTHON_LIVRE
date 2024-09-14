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

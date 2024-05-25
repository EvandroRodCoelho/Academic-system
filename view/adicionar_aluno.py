import PySimpleGUI as sg

def tela_adicionar_aluno():
    layout = [
        [sg.Text('Nome:', size=(15, 1))],
        [sg.InputText(key='nome')],
        [sg.Text('Endereço:', size=(15, 1))],
        [sg.InputText(key='endereco')],
        [sg.Button('Cadastrar'), sg.Button('Cancelar')]
    ]

    window = sg.Window('Cadastro de Aluno', layout)
    return window

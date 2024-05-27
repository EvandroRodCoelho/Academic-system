import PySimpleGUI as sg

def tela_adicionar_aluno():
    layout = [
        [sg.Text('Nome:', font=("Helvetica",14))],
        [sg.InputText(key='nome')],
        [sg.Text('Endereço:', font=("Helvetica",14))],
        [sg.InputText(key='endereco',font=("Helvetica",14))],
        [sg.Button('Cadastrar',font=("Helvetica",14)), sg.Button('Cancelar',font=("Helvetica",14))]
    ]

    window = sg.Window('Cadastro de Aluno', layout)
    return window

import PySimpleGUI as sg

def tela_principal():
    layout = [
        [sg.Button('Cadastrar Aluno', font=("Helvetica",14)), sg.Button('Visualizar Alunos', font=("Helvetica",14))],
        [sg.Button('Sair', font=("Helvetica",16))]
    ]
    return sg.Window('Sistema de Alunos', layout, finalize=True)

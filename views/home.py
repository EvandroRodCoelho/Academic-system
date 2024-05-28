import PySimpleGUI as sg

class HomeView:
    def __init__(self):
        button_size = (20, 2)
        self.layout = [
            [sg.Button('Alunos', size=button_size, pad=(5, 5)), sg.Button('Professores', size=button_size, pad=(5, 5))],
            [sg.Button('Disciplinas', size=button_size, pad=(5, 5)), sg.Button('Turmas', size=button_size, pad=(5, 5))],
            [sg.Button('Salas de Aulas', size=button_size, pad=(5, 5)), sg.Button('Aulas', size=button_size, pad=(5, 5))],
            [sg.Button('Horários', size=button_size, pad=(5, 5)), sg.Button('Sair', size=button_size, pad=(5, 5))],
        ]
        self.window = sg.Window('Sistema de Gerenciamento Escolar', self.layout, finalize=True)

    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()

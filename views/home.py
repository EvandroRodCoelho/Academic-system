import PySimpleGUI as sg

class HomeView:
    def __init__(self):
        self.layout = [
            [sg.Button('Alunos'), sg.Button('Professores')],
            [sg.Button('Disciplinas'),sg.Button('Turmas')],
            [sg.Button('Salas de Aulas'),sg.Button('Aulas'),sg.Button('Horários')],
            [sg.Button('Sair')]
        ]
        self.window = sg.Window('Sistema de Gerenciamento Escolar', self.layout, finalize=True)

    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()

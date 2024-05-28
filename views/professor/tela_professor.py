import PySimpleGUI as sg
class TelaProfessor: 
    def __init__(self):
        self.layout = [
            [sg.Button('Adicionar professor', key='Adicionar'), sg.Button('Visualizar Alunos', key='Visualizar')]
        ]
        self.window = sg.Window('Gerenciamento de Alunos', self.layout)

    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()
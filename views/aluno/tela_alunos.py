import PySimpleGUI as sg
class TelaAlunos:
    def __init__(self):
        self.layout = [
            [sg.Button('Adicionar Aluno', key='Adicionar'), sg.Button('Visualizar Alunos', key='Visualizar')]
        ]
        self.window = sg.Window('Gerenciamento de Alunos', self.layout)

    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()
        


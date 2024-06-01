import PySimpleGUI as sg

class TelaAdicionarDisciplina:
    def __init__(self, professores):
        self.professores = professores
        self.professor_nomes = [prof[1] for prof in professores]
        self.layout = [
            [sg.Text('Nome da Disciplina:', font=("Helvetica", 14))],
            [sg.InputText(key='nome')],
            [sg.Text('Professor:', font=("Helvetica", 14))],
            [sg.Combo(self.professor_nomes, key='professor', readonly=True,size=(30,1))],
            [sg.Text('Especialidade:', font=("Helvetica", 14))],
            [sg.InputText(key='especialidade')],
            [sg.Button('Cadastrar', font=("Helvetica", 14)), sg.Button('Cancelar', font=("Helvetica", 14), key='cancelar')]
        ]
        self.window = sg.Window('Cadastro de Disciplina', self.layout, finalize=True)

    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()

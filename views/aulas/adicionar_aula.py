import PySimpleGUI as sg

class TelaAdicionarAula:
    def __init__(self, professores,disciplina):
        print (disciplina)
        self.professor_nomes = [prof[1] for prof in professores]
        self.disciplina_nome = [disc[1] for disc in disciplina]
        self.layout = [
            [sg.Text('Professor:', font=("Helvetica", 14))],
            [sg.Combo(self.professor_nomes, key='professor', readonly=True,size=(30,1))],
            [sg.Text('Disciplina:', font=("Helvetica", 14))],
            [sg.Combo(self.disciplina_nome, key='professor', readonly=True, size=(30,1))],
            [sg.Button('Cadastrar', font=("Helvetica", 14)), sg.Button('Cancelar', font=("Helvetica", 14), key='cancelar')]
        ]
        self.window = sg.Window('Cadastro de Disciplina', self.layout, finalize=True)

    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()

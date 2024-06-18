import PySimpleGUI as sg


class TelaAdicionarAula:
    def __init__(self, professores, disciplina):
        self.professor_nomes = [prof[1] for prof in professores]
        self.disciplina_nome = [disc[1] for disc in disciplina]
        self.layout = [
            [sg.Text('Professor:', font=("Helvetica", 16))],
            [sg.Combo(self.professor_nomes, key='professor', readonly=True, size=(30, 1), font=("Helvetica", 14))],
            [sg.Text('Disciplina:', font=("Helvetica", 16))],
            [sg.Combo(self.disciplina_nome, key='disciplina', readonly=True, size=(30, 1), font=("Helvetica", 14))],
            [sg.Text('Data:', font=("Helvetica", 16))],
            [sg.Input(key='data', size=(10, 1), font=("Helvetica", 14)),
                sg.CalendarButton("Escolha a data", font=("Helvetica", 12), target='data', format='%d/%m/%Y')],
            [sg.Button('Cadastrar', font=("Helvetica", 16)),
             sg.Button('Cancelar', font=("Helvetica", 16), key='cancelar')]
        ]
        self.window = sg.Window('Cadastro de Aula', self.layout, finalize=True)

    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()

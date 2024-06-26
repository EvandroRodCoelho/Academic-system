import PySimpleGUI as sg


class TelaEditarDisciplina:
    def __init__(self, professores, disciplina):
        self.professores = professores
        self.disciplina = disciplina
        self.professor_nomes = [prof[1] for prof in professores]
        self.layout = [
            [sg.Text('Nome da Disciplina:', font=("Helvetica", 16))],
            [sg.InputText(key='nome', default_text=self.disciplina['nome'], font=("Helvetica", 14))],
            [sg.Text('Professor:', font=("Helvetica", 16))],
            [sg.Combo(self.professor_nomes, key='professor', readonly=True, size=(30, 1),
                      default_value=self.disciplina['id_professor'], font=("Helvetica", 14))],
            [sg.Text('Especialidade:', font=("Helvetica", 16))],
            [sg.InputText(key='especialidade', default_text=self.disciplina['especialidade'], font=("Helvetica", 14))],
            [sg.Button('Salvar', font=("Helvetica", 16)), sg.Button('Cancelar', font=("Helvetica", 16), key='cancelar')]
        ]
        self.window = sg.Window('Editar de Disciplina', self.layout, finalize=True)

    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()

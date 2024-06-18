import PySimpleGUI as sg


class TelaEditarSalaDeAula:
    def __init__(self, sala_de_aula, professores, disciplinas):
        self.sala_de_aula = sala_de_aula
        self.professores = professores
        self.disciplinas = disciplinas
        self.professor_nome = [prof[1] for prof in professores]
        self.disciplina_nome = [disc[1] for disc in disciplinas]
        self.layout = [
            [sg.Text('Professor:', font=("Helvetica", 16))],
            [sg.Combo(self.professor_nome, key='professor', readonly=True, size=(30, 1),
                      default_value=self.sala_de_aula['id_professor'], font=("Helvetica", 14))],
            [sg.Text('Disciplina:', font=("Helvetica", 16))],
            [sg.Combo(self.disciplina_nome, key='disciplina', readonly=True, size=(30, 1),
                      default_value=self.sala_de_aula['id_disciplina'], font=("Helvetica", 14))],
            [sg.Text('Data:', font=("Helvetica", 16))],
            [sg.Input(key='data', size=(10, 1), font=("Helvetica", 14), default_text=self.sala_de_aula['data']),
                sg.CalendarButton("Escolha a data", font=("Helvetica", 12), target='data', format='%d/%m/%Y')],
            [sg.Button('Salvar', font=("Helvetica", 14)),
             sg.Button('Cancelar', font=("Helvetica", 14), key='cancelar')]
        ]
        self.window = sg.Window('Editar Aula', self.layout, finalize=True)

    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()

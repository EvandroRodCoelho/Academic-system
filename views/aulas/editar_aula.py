import PySimpleGUI as sg

class TelaEditarAula:
    def __init__(self,aula, professores,disciplina):
        self.aula = aula
        self.professor_nomes = [prof[1] for prof in professores]
        self.disciplina_nome = [disc[1] for disc in disciplina]

        self.layout = [
            [sg.Text('Professor:', font=("Helvetica", 14))],
            [sg.Combo(self.professor_nomes, key='professor', readonly=True,size=(30,1), default_value=self.aula['professor'])],
            [sg.Text('Disciplina:', font=("Helvetica", 14))],
            [sg.Combo(self.disciplina_nome, key='disciplina', readonly=True, size=(30,1), default_value=self.aula['disciplina'])],
            [sg.Text('Horário:', font=("Helvetica", 14))],
            [sg.Input(key='horario', size=(10, 1), default_text=self.aula['horario'])],
            [sg.Button('Salvar', font=("Helvetica", 14)), sg.Button('Cancelar', font=("Helvetica", 14), key='cancelar')]
        ]
        self.window = sg.Window('Editar Aula', self.layout, finalize=True)

    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()
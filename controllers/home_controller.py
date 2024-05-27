import PySimpleGUI as sG


class HomeController:
    def __init__(self):
        self.layout = [
            [sG.Button('Alunos')],
            [sG.Button('Professores')],
            [sG.Button('Disciplinas')],
            [sG.Button('Turmas')],
            [sG.Button('Salas de Aulas')],
            [sG.Button('Horários')],
            [sG.Button('Aulas')]
        ]
        self.window = None

    def retorno(self):
        self.window = sG.Window('Sistema Acadêmico', self.layout)

        while True:
            event, values = self.window.read()

            if event == self.window.is_closed():
                break

        self.window.close()

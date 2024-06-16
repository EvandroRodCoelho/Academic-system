import PySimpleGUI as sg


class HomeView:
    def __init__(self):
        button_size = (14, 2)
        self.layout = [
            [
                sg.Button('Alunos', font=('Helvetica', 14), size=button_size, pad=(5, 5)),
                sg.Button('Professores',font=('Helvetica', 14), size=button_size, pad=(5, 5))
            ],
            [
                sg.Button('Disciplinas',font=('Helvetica', 14), size=button_size, pad=(5, 5)), 
                sg.Button('Salas de Aulas',font=('Helvetica', 14), size=button_size, pad=(5, 5))
            ],
            [ 
                sg.Button('Histórico',key='Historico',font=('Helvetica', 14), size=button_size, pad=(5, 5)),
                sg.Button('Sair', font=('Helvetica', 14),size=button_size, pad=(5, 5))
            ],
        ]
        self.window = sg.Window('Sistema de Gerenciamento Escolar', self.layout, finalize=True)

    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()

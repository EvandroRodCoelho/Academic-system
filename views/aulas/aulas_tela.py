import PySimpleGUI as sg

class TelaAulas:
    def __init__(self,aulas):
        self.layout = [
            [sg.Text('Lista de aulas', font=('Helvetica', 16)),
             sg.Button('Adicionar', font=('Helvetica', 16), key='Adicionar'),
             sg.Button('Editar', font=('Helvetica', 16)),
             sg.Button('Excluir', font=('Helvetica', 16))],
            [sg.Button('Voltar', key='voltar', font=('Helvetica', 16))]
        ]
        self.window = sg.Window('Aulas', self.layout)

    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()

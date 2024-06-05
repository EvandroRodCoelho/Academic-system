import PySimpleGUI as sg

class TelaTurmas:
    def __init__(self):
        self.layout = [
            [sg.Text('Lista de turmas', font=('Helvetica', 16)),
             sg.Push(),
             sg.Button('Adicionar', font=('Helvetica', 16), key='Adicionar'),
             sg.Button('Editar', font=('Helvetica', 16)),
             sg.Button('Excluir', font=('Helvetica', 16))],
            [sg.Button('Voltar', key='voltar', font=('Helvetica', 16))]
        ]
        self.window = sg.Window('Turmas', self.layout)

    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()

import PySimpleGUI as sg

class TelaHorarios:
    def __init__(self,horarios):
        self.layout = [
            [sg.Text('Lista de horários', font=('Helvetica', 16)),
             sg.Button('Adicionar', font=('Helvetica', 16), key='Adicionar'),
             sg.Button('Editar', font=('Helvetica', 16)),
             sg.Button('Excluir', font=('Helvetica', 16))],
            [sg.Button('Voltar', key='voltar', font=('Helvetica', 16))]
        ]
        self.window = sg.Window('Horários', self.layout)

    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()

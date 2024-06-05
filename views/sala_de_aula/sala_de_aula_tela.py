
import PySimpleGUI as sg

class TelaSalaDeAula:
    def __init__(self,aulas):
        self.layout = [
            [sg.Text('Lista de salas de aula', font=('Helvetica', 16)),
             sg.Button('Adicionar', font=('Helvetica', 16), key='Adicionar'),
             sg.Button('Editar', font=('Helvetica', 16)),
             sg.Button('Excluir', font=('Helvetica', 16))],
            [sg.Button('Voltar', key='voltar', font=('Helvetica', 16))]
        ]
        self.window = sg.Window('Salas de Aula', self.layout)

    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()

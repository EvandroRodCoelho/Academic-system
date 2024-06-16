import PySimpleGUI as sg

class TelaAtribuirNotaFalta:
    def __init__(self):
        self.layout = [
            [sg.Text('Digite a nota:', font=("Helvetica", 14)),sg.Push() ,sg.InputText(key='nota',size=(10, 1) ,font=("Helvetica", 14))],
            [sg.Text('Digite a quantidade de faltas:' ,font=("Helvetica", 14)), sg.InputText(key='faltas',size=(10, 1) ,font=("Helvetica", 14))],
            [sg.Button('Confirmar', size=(10, 1),font=("Helvetica", 14), key=('confirmar')),
              sg.Button('Cancelar',size=(10, 1), font=("Helvetica", 14))]
        ]
        self.window = sg.Window('Atribuir Nota e Faltas', self.layout)

    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()
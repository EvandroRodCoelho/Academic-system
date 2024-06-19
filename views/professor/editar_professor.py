import PySimpleGUI as sg


class TelaEditarProfessor:
    def __init__(self, professor):
        self.professor = professor
        self.layout = [
            [sg.Text('Nome:', font=("Helvetica", 16))],
            [sg.InputText(default_text=professor['nome'], key='nome', font=("Helvetica", 14))],
            [sg.Button('Salvar', font=("Helvetica", 16)), sg.Button('Cancelar', font=("Helvetica", 16), key="cancelar")]
        ]
        self.window = sg.Window('Editar Professor', self.layout, finalize=True)
    
    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()
import PySimpleGUI as sg
class TelaAdicionarAluno:
    def __init__(self):
        self.layout = [
            [sg.Text('Nome:', font=("Helvetica", 16))],
            [sg.InputText(key='nome', font=("Helvetica", 14))],
            [sg.Text('Endereço:', font=("Helvetica", 16))],
            [sg.InputText(key='endereco', font=("Helvetica", 14))],
            [sg.Button('Cadastrar', font=("Helvetica", 16)),
             sg.Button('Cancelar', font=("Helvetica", 16), key="cancelar")]
        ]
        self.window = sg.Window('Cadastro de Aluno', self.layout, finalize=True)

    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()
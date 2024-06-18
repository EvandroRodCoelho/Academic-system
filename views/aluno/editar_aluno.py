import PySimpleGUI as sg


class TelaEditarAluno:
    def __init__(self, aluno):
        self.aluno = aluno
        self.layout = [
            [sg.Text('Nome:', font=("Helvetica", 16))],
            [sg.InputText(default_text=aluno['nome'], key='nome', font=("Helvetica", 14))],
            [sg.Text('Endereço:', font=("Helvetica", 16))],
            [sg.InputText(default_text=aluno['endereco'], key='endereco', font=("Helvetica", 14))],
            [sg.Button('Salvar', font=("Helvetica", 16)),
             sg.Button('Cancelar', font=("Helvetica", 16), key="cancelar")]
        ]
        self.window = sg.Window('Editar Aluno', self.layout, finalize=True)

    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()

import PySimpleGUI as sg


class AdicionarAlunosSalaDeAula:
    def __init__(self, alunos, sala_de_aula):
        self.aluno_nome = [aluno[1] for aluno in alunos]
        self.sala_de_aula = [sala[1] for sala in sala_de_aula]

        self.layout = [
            [sg.Text('Aluno:', font=("Helvetica", 16))],
            [sg.Combo(self.aluno_nome, key='aluno', readonly=True, size=(30, 1), font=("Helvetica", 14))],
            [sg.Text('Sala de Aula:', font=("Helvetica", 16))],
            [sg.Combo(self.sala_de_aula, key='sala_de_aula', readonly=True, size=(30, 1), font=("Helvetica", 14))],
            [sg.Button('Cadastrar', font=("Helvetica", 16)),
             sg.Button('Cancelar', font=("Helvetica", 16), key='cancelar')]
        ]
        self.window = sg.Window('Cadastro de Aluno para Sala de Aula', self.layout, finalize=True)

    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()

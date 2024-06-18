import PySimpleGUI as sg


class TelaAlunosSalaDeAula:
    def __init__(self, alunos_sala_de_aulas):
        cabecalhos = ['ID', 'Aluno', 'Sala de Aula']
        self.layout = [
            [sg.Text('Lista de alunos adicionados as salas de aulas', font=('Helvetica', 16)),
             sg.Button('Adicionar', font=('Helvetica', 16)),
             sg.Button('Excluir', font=('Helvetica', 16))],
            [sg.Table(values=alunos_sala_de_aulas,
                      headings=cabecalhos,
                      display_row_numbers=False,
                      font=('Helvetica', 14),
                      auto_size_columns=False,
                      num_rows=min(25, len(alunos_sala_de_aulas)),
                      key='-TABLE-',
                      enable_events=True,
                      justification='left',
                      col_widths=[10, 25, 25])],
            [sg.Button('Voltar', key='voltar', font=('Helvetica', 16))]
        ]
        self.window = sg.Window('Alunos da Sala de Aula', self.layout)

    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()

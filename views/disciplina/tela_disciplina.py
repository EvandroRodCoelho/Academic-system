import PySimpleGUI as sg


class TelaDisciplina:
    def __init__(self, disciplinas=None):
        cabecalho = ['ID', 'Nome', 'Professor', 'Especialidade']
        if disciplinas is None or len(disciplinas) == 0:
            disciplinas = [('', "Nenhuma disciplina encontrada", '', '')]

        self.layout = [
            [sg.Text('Lista de disciplinas', font=('Helvetica', 16)),
             sg.Push(),
             sg.Button('Adicionar', font=('Helvetica', 16), key='Adicionar'),
             sg.Button('Editar', font=('Helvetica', 16)),
             sg.Button('Excluir', font=('Helvetica', 16))],
            [sg.Table(
                values=disciplinas,
                key='-TABLE-',
                headings=cabecalho,
                col_widths=[10, 30, 15, 30],
                display_row_numbers=False,
                auto_size_columns=False,
                justification='left',
                num_rows=min(25, len(disciplinas)),
                font=('Helvetica', 14),
                enable_events=True
            )],
            [sg.Button('Voltar', key='voltar', font=('Helvetica', 16))]
        ]

        self.window = sg.Window('Gerenciamento de disciplina', self.layout)

    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()

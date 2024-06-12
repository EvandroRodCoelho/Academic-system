import PySimpleGUI as sg
class TelaAulas:
    def __init__(self, aulas):
        cabecalho = ['ID', 'Horário', 'Professor', 'Disciplina', 'Especialidade']
        self.layout = [
            [sg.Text('Lista de aulas', font=('Helvetica', 16)),
             sg.Push(),
             sg.Button('Adicionar', font=('Helvetica', 16), key='Adicionar'),
             sg.Button('Editar', font=('Helvetica', 16)),
             sg.Button('Excluir', font=('Helvetica', 16))],
            [sg.Table(
                values=aulas,
                key='-TABLE-',
                headings=cabecalho,
                col_widths=[10, 20, 15, 15, 15],
                display_row_numbers=False,
                auto_size_columns=False,
                justification='left',
                num_rows=min(25, len(aulas)),
                font=('Helvetica', 14),
                enable_events=True
            )],
            [sg.Button('Voltar', key='voltar', font=('Helvetica', 16))]
        ]
        self.window = sg.Window('Aulas', self.layout)

    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()
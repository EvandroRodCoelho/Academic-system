import PySimpleGUI as sg


class TelaSalaDeAula:
    def __init__(self, salas_de_aulas):
        cabecalhos = ['ID', 'Professor', 'Disciplina', 'Data']
        self.layout = [
            [sg.Text('Lista de salas de aula', font=('Helvetica', 16)),
             sg.Button('Adicionar', font=('Helvetica', 16)),
             sg.Button('Editar', font=('Helvetica', 16)),
             sg.Button('Excluir', font=('Helvetica', 16)),
             sg.Button('Adicionar Alunos', font=('Helvetica', 16))],
            [sg.Table(values=salas_de_aulas,
                      headings=cabecalhos,
                      display_row_numbers=False,
                      font=('Helvetica', 14),
                      auto_size_columns=False,
                      num_rows=min(25, len(salas_de_aulas)),
                      key='-TABLE-',
                      enable_events=True,
                      justification='left',
                      col_widths=[10, 25, 25, 10])],
            [sg.Button('Voltar', key='voltar', font=('Helvetica', 16))]
        ]
        self.window = sg.Window('Salas de Aula', self.layout)

    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()

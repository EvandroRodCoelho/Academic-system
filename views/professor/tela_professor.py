import PySimpleGUI as sg
class TelaProfessor: 
    def __init__(self, professor:None):
        if professor is None or len(professor) == 0:
            professor = [('',"Nenhum professor encontrado")]
        self.layout =  [[sg.Text('Lista de professores', font=('Helvetica', 16)), sg.Button('Adicionar', font=('Helvetica', 16), key='Adicionar'), sg.Button('Editar', font=('Helvetica', 16)), sg.Button('Excluir', font=('Helvetica', 16))],
            [sg.Table(
                values=professor,
                key='-TABLE-',
                headings=['ID', 'Nome'],
                col_widths=[10, 30],
                display_row_numbers=False,
                auto_size_columns=False,
                justification='left',
                num_rows=min(25, len(professor)),
                font=('Helvetica', 14),
                enable_events=True
            )],
            [sg.Button('Voltar', key='voltar', font=('Helvetica', 16))]]
        self.window = sg.Window('Gerenciamento de professor', self.layout)

    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()
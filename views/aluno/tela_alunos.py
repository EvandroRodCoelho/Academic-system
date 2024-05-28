import PySimpleGUI as sg
class TelaAlunos:
    def __init__(self,alunos):
            self.layout =  [[sg.Text('Lista de Alunos', font=('Helvetica', 16)), sg.Button('Adicionar', font=('Helvetica', 16))],
            [sg.Table(
                values=alunos,
                key='-TABLE-',
                headings=['ID', 'Nome', 'Endereço'],
                col_widths=[10, 30, 50],
                display_row_numbers=False,
                auto_size_columns=False,
                justification='left',
                num_rows=min(25, len(alunos)),
                font=('Helvetica', 14),
                enable_events=True
            )],
            [sg.Button('Voltar', key='voltar', font=('Helvetica', 16))]]
            self.window = sg.Window('Gerenciamento de Alunos', self.layout)

    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()
        


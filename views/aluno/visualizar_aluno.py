import PySimpleGUI as sg
class VisualizarAlunoView: 
    def __init__(self,alunos):
        layout = [
            [sg.Text('Lista de Alunos', font=('Helvetica', 16))],
            [sg.Table(
                values=alunos,
                headings=['ID', 'Nome', 'Endereço'],
                col_widths=[10, 30, 50],
                display_row_numbers=False,
                auto_size_columns=False,
                justification='left',
                num_rows=min(25, len(alunos)),
                font=('Helvetica', 14),
                key='-TABLE-'
            )],
            [sg.Button('Fechar')]
        ]
        self.window = sg.Window('Visualizar Alunos', layout, finalize=True)
    
    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()

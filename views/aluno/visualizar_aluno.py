import PySimpleGUI as sg

def tela_visualizar_alunos(alunos):
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
    window = sg.Window('Visualizar Alunos', layout, finalize=True)
    return window

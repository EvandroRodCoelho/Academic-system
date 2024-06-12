import PySimpleGUI as sg

class TelaHorarios:
    def __init__(self, horarios):
        dados_tabela = [list(linha) for linha in horarios]
        cabecalhos = ['ID', 'Professor', 'Disciplina', 'Horário']
        self.layout = [
            [sg.Text('Lista de horários', font=('Helvetica', 16))],
            [sg.Table(values=dados_tabela, col_widths=[10, 30, 15, 30], font=('Helvetica', 14), headings=cabecalhos, display_row_numbers=False, auto_size_columns=True, num_rows=min(25, len(horarios)))],
            [sg.Button('Voltar', key='voltar', font=('Helvetica', 16))]
        ]
        self.window = sg.Window('Horários', self.layout)

    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()
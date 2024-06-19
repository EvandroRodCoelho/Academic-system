import PySimpleGUI as sg


class TelaHistorico:
    def __init__(self, aulas, alunos):
        self.alunos = alunos
        self.aulas = aulas
        print(self.alunos)
        self.layout = [
            [sg.Text('Aluno:', font=('Helvetica', 16)), sg.Push(), sg.Combo([f"{aluno[0]} - {aluno[1]}" for aluno in alunos], key='aluno',
                                                    size=(30, 1), enable_events=True, font=("Helvetica", 14))],
            [sg.Text('Sala:', font=('Helvetica', 16)), sg.Push(), sg.Combo(aulas, key='sala',size=(30, 1),
                                                   font=("Helvetica", 14), enable_events=True)],
            [sg.Button('Buscar',font=('Helvetica', 16) ,size=(10, 1))],
            [sg.Table(values=[], headings=['ID', 'Aluno', 'Notas', 'Faltas', 'Situação'], key='tabela',font=('Helvetica', 14),
                      display_row_numbers=False, auto_size_columns=False,col_widths=[5,20,5,5,10], num_rows=10)],
            [sg.Button('Atribuir Falta', key='att-falta',font=('Helvetica', 16), size=(15, 1)),
             sg.Button('Atribuir Nota', key='att-nota',font=('Helvetica', 16), size=(15, 1)),
             sg.Button('Atribuir Nota e Falta',font=('Helvetica', 16), key='att-nota-falta', size=(20, 1))],
            [sg.Button('Voltar',font=('Helvetica', 16), key='voltar', size=(10, 1))]
        ]

        self.window = sg.Window('Histórico', self.layout)

    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()
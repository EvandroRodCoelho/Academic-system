import PySimpleGUI as sg

class TelaSalaDeAula:
    def __init__(self, aulas):
        cabecalhos = ['ID', 'Professor', 'Disciplina', 'Horário']
        self.layout = [
            [sg.Text('Lista de salas de aula', font=('Helvetica', 16)),
              sg.Button('Adicionar')], 
            [sg.Table(values=aulas, headings=cabecalhos, 
                    display_row_numbers=False, font=('Helvetica', 14),
                    auto_size_columns=True, num_rows=min(25, len(aulas)),
                    key='-TABELA-AULAS-', enable_events=True, 
                    justification='left')],
            [sg.Button('Voltar', key='voltar', font=('Helvetica', 16))]
        ]
        self.window = sg.Window('Salas de Aula', self.layout)

    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()
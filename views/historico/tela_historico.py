import PySimpleGUI as sg
class TelaHistorico: 
    def __init__(self, aulas, alunos):
        self.alunos = alunos
        self.aulas = aulas
        self.todos_alunos = [f"{aluno[0]} {aluno[1]}"  for aluno in alunos]
        self.layout = [
            [sg.Text('Aluno:'),sg.Push() ,sg.Combo(values=self.todos_alunos, key='aluno', size=(30, 1),enable_events=True, font=("Helvetica", 14))],
            [sg.Text('Sala:'),sg.Push() , sg.Combo(aulas, key='sala', size=(30, 1), font=("Helvetica", 14), enable_events=True)],
            [sg.Button('Buscar',font=("Helvetica", 14), size=(10, 1)), sg.Button('Atribuir falta' , key="att-falta",font=("Helvetica", 14))],
            [sg.Table(values=[], headings=['ID', 'Aluno', 'Notas', 'Faltas', 'Aprovado'],col_widths=[5,15,5,5,10] ,key='tabela', display_row_numbers=False,
                auto_size_columns=False, font=("Helvetica", 14))],
            [sg.Button('Voltar', font=("Helvetica", 14), size=(10, 1))]
        ]


        self.window = sg.Window('Histórico', self.layout)
    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()
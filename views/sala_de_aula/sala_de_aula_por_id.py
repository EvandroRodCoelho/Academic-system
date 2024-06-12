import PySimpleGUI as sg

class TelaSalaDeAulaPorId:
    def __init__(self, aula, alunos):
        cabecalhos = ['ID', 'Nome', 'Endereço', 'Notas', 'Faltas']
        self.layout = [
            [sg.Text(f'Aula: {aula["aula"]} - Professor: {aula["professor"]} - Horário: {aula["horario"]}', font=('Helvetica', 16))],
            [sg.Text("Alunos:")],
            [sg.Table(values=alunos, col_widths=[5,20,40,5,5], font=('Helvetica', 14), headings=cabecalhos, 
                      display_row_numbers=False, auto_size_columns=False, 
                      num_rows=min(25, len(alunos)), key='-TABELA-ALUNOS-', 
                      enable_events=True, justification='left')],
            [sg.Button('Voltar', size=(10, 1), font=('Helvetica', 16))]
        ]
        self.window = sg.Window('Salas de Aula', self.layout, finalize=True)

    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()
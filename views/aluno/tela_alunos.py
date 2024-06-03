import PySimpleGUI as sg


class TelaAlunos:
    def __init__(self, alunos=None):
        if alunos is None or len(alunos) == 0:
            alunos = [('', "Nenhum aluno encontrado", "")]

        self.layout = [[sg.Text('Lista de Alunos', font=('Helvetica', 16)),
                        sg.Push(),
                        sg.Button('Adicionar', font=('Helvetica', 16)),
                        sg.Button('Editar', font=('Helvetica', 16)),
                        sg.Button('Excluir', font=('Helvetica', 16))],
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
        self.alunos = alunos

    def mostrar(self):
        return self.window.read()

    def fechar(self):
        self.window.close()

    def adicionar_aluno(self, nome, endereco):
        id = max(aluno["ID"] for aluno in self.alunos) + 1
        novo_aluno = {"ID": id, "Nome": nome, "Endereço": endereco}
        self.alunos.append(novo_aluno)
        self.atualizar_tabela()

    def editar_aluno(self, id, nome, endereco):
        for aluno in self.alunos:
            if aluno["ID"] == id:
                aluno["Nome"] = nome
                aluno["Endereço"] = endereco
                self.atualizar_tabela()
                break

    def atualizar_tabela(self):
        self.window["-TABLE-"].update(values=self.alunos)

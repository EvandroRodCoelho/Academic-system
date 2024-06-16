from model.aluno_model import AlunoModel
from service.page_service import NavegacaoService
from views.aluno.tela_alunos import TelaAlunos
import PySimpleGUI as sG


class AlunoController:

    def __init__(self):
        self.window = None
        self.alunoModel = AlunoModel()
        self.alunos = self.alunoModel.consultar_alunos()
        self.navegacaoService = NavegacaoService()
        self.aluno_selecionado = None

    def mostrar_tela(self):
        self.window = TelaAlunos(self.alunos).window
        self.retorno()

    def retorno(self):
        while True:
            event, values = self.window.read()
            if event == 'Adicionar':
                self.window.close()
                self.navegacaoService.navegar_para_adicionar_alunos()
                break
            if event == 'Editar':
                if self.aluno_selecionado:
                    self.window.close()
                    self.navegacaoService.navegar_para_editar_alunos(self.aluno_selecionado)
            if event == 'Excluir':
                if self.aluno_selecionado:
                    self.alunoModel.excluir(self.aluno_selecionado['id'])
                    self.alunos = self.alunoModel.consultar_alunos()
                    self.window['-TABLE-'].update(values=self.alunos)
                    self.aluno_selecionado = None

            if event == '-TABLE-':
                selected_row_index = values['-TABLE-'][0] if values['-TABLE-'] else None

                if selected_row_index is not None:
                    linha_selecionada = self.alunos[selected_row_index]
                    self.aluno_selecionado = {'id': linha_selecionada[0], 'nome': linha_selecionada[1],
                                              'endereco': linha_selecionada[2]}

            if event == sG.WIN_CLOSED or event == 'voltar':
                self.window.close()
                self.navegacaoService.navegar_para_home()
                break

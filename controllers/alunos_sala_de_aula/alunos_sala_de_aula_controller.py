from model.alunos_sala_de_aula_model import AlunosSalaDeAulaModel
from service.page_service import NavegacaoService
from views.alunos_sala_de_aula.tela_alunos_sala_de_aula import TelaAlunosSalaDeAula
import PySimpleGUI as sG


class AlunosSalaDeAulaController:
    def __init__(self):
        self.window = None
        self.navegacaoService = NavegacaoService()
        self.alunosSalasDeAulaModel = AlunosSalaDeAulaModel()
        self.alunos_sala_de_aulas = self.alunosSalasDeAulaModel.consultar_alunos_sala_de_aula()
        self.aluno_sala_de_aula_selecionada = None

        if self.alunos_sala_de_aulas is None:
            self.alunos_sala_de_aulas = []

    def mostrar_tela(self):
        self.window = TelaAlunosSalaDeAula(self.alunos_sala_de_aulas).window
        self.retorno()

    def retorno(self):
        while True:
            event, values = self.window.read()
            if event == sG.WIN_CLOSED or event == 'voltar':
                self.window.close()
                self.navegacaoService.navegar_para_home()
                break
            if event == "Adicionar":
                self.window.close()
                self.navegacaoService.navegar_para_adicionar_alunos_sala_de_aula()
            if event == 'Excluir':
                if self.aluno_sala_de_aula_selecionada:
                    self.alunosSalasDeAulaModel.excluir_alunos_sala_de_aula(self.aluno_sala_de_aula_selecionada['id'])
                    self.alunos_sala_de_aulas = self.alunosSalasDeAulaModel.consultar_alunos_sala_de_aula()
                    self.window['-TABLE-'].update(values=self.alunos_sala_de_aulas)
                    self.aluno_sala_de_aula_selecionada = None
            if event == '-TABLE-':
                selected_row_index = values['-TABLE-'][0] if values['-TABLE-'] else None
                if selected_row_index is not None:
                    linha_selecionada = self.alunos_sala_de_aulas[selected_row_index]
                    self.aluno_sala_de_aula_selecionada = {'id': linha_selecionada[0],
                                                           'id_aluno': linha_selecionada[1],
                                                           'id_sala_de_aula': linha_selecionada[2]}

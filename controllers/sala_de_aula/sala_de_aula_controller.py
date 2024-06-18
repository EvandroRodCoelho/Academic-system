from model.sala_de_aula_model import SalaDeAulaModel
from service.page_service import NavegacaoService
from views.sala_de_aula.tela_sala_de_aula import TelaSalaDeAula
import PySimpleGUI as sG


class SalaDeAulaController:
    def __init__(self):
        self.window = None
        self.navegacaoService = NavegacaoService()
        self.salasDeAulaModel = SalaDeAulaModel()
        self.salas_de_aulas = self.salasDeAulaModel.consultar_salas_de_aulas()
        self.sala_de_aula_selecionada = None

    def mostrar_tela(self):
        self.window = TelaSalaDeAula(self.salas_de_aulas).window
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
                self.navegacaoService.navegar_para_adicionar_sala_de_aula()
            if event == 'Excluir':
                if self.sala_de_aula_selecionada:
                    self.salasDeAulaModel.excluir_sala_de_aula(self.sala_de_aula_selecionada['id'])
                    self.salas_de_aulas = self.salasDeAulaModel.consultar_salas_de_aulas()
                    self.window['-TABLE-'].update(values=self.salas_de_aulas)
                    self.sala_de_aula_selecionada = None
            if event == 'Editar':
                if self.sala_de_aula_selecionada:
                    self.window.close()
                    self.navegacaoService.navegar_para_editar_sala_de_aula(self.sala_de_aula_selecionada)
            if event == 'Adicionar Alunos':
                self.window.close()
                self.navegacaoService.navegar_para_alunos_sala_de_aula()
            if event == '-TABLE-':
                selected_row_index = values['-TABLE-'][0] if values['-TABLE-'] else None
                if selected_row_index is not None:
                    linha_selecionada = self.salas_de_aulas[selected_row_index]
                    self.sala_de_aula_selecionada = {'id': linha_selecionada[0],
                                                     'id_professor': linha_selecionada[1],
                                                     'id_disciplina': linha_selecionada[2],
                                                     'data': linha_selecionada[3]}

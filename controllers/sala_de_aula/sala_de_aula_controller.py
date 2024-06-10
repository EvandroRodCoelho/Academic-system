from model.sala_de_aula_model import SalaDeAulaModel
from service.page_service import NavegacaoService
from views.sala_de_aula.sala_de_aula_tela import TelaSalaDeAula
import PySimpleGUI as sG

class SalaDeAulaController:
    def __init__(self):
        self.window = None
        self.navegaçãoService = NavegacaoService()
        self.salasDeAulaModel = SalaDeAulaModel()
        self.salas_de_aula = self.salasDeAulaModel.consultar_salas_aulas()
        self.sala_selecionada = None
    def mostrar_tela(self):
        self.window = TelaSalaDeAula(self.salas_de_aula).window
        self.retorno()

    def retorno(self):
        while True:
            event, values = self.window.read()
            if event == sG.WIN_CLOSED or event == 'voltar':
                self.window.close()
                self.navegaçãoService.navegar_para_home()
                break
            if event == '-TABELA-AULAS-': 
                selected_row_index = values['-TABELA-AULAS-'][0] if values['-TABELA-AULAS-'] else None
                if selected_row_index is not None:
                    linha_selecionada = self.salas_de_aula[selected_row_index]
                    self.sala_selecionada = { 'id': linha_selecionada[0],
                                               'aula': linha_selecionada[2], 
                                               'professor': linha_selecionada[1], 
                                                'horario': linha_selecionada[3],
                                            'id_disciplina': linha_selecionada[4], }
                    self.window.close()
                    self.navegaçãoService.navegar_para_salas_de_aula_alunos(self.sala_selecionada)
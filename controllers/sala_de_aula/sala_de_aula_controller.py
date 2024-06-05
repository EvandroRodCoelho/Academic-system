from model.sala_de_aula_model import SalaDeAulaModel
from service.page_service import NavegacaoService
from views.sala_de_aula.sala_de_aula_tela import TelaSalaDeAula
import PySimpleGUI as sG

class SalaDeAulaController:
    salas_de_aula = []
    navegaçãoService = NavegacaoService()
    selected_sala_de_aula = None

    def __init__(self):
        self.window = None
        self.homeService = NavegacaoService()
        self.salasDeAulaModel = SalaDeAulaModel()
        #self.salas_de_aula = self.salasDeAulaModel.consultar_salas_de_aula()

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

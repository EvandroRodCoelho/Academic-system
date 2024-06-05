from service.page_service import NavegacaoService
from model.aulas_model import AulaModel
from views.aulas.aulas_tela import TelaAulas
import PySimpleGUI as sG
class AulasController:
    aulas = []
    navegaçãoService = NavegacaoService()
    selected_aula = None

    def __init__(self):
        self.window = None
        self.homeService = NavegacaoService()
        self.aulasModel = AulaModel()
#        self.aulas = self.aulasModel.consultar_aulas()

    def mostrar_tela(self):
        self.window = TelaAulas(self.aulas).window
        self.retorno()

    def retorno(self):
        while True:
            event, values = self.window.read()
            if event == sG.WIN_CLOSED or event == 'voltar':
                self.window.close()
                self.navegaçãoService.navegar_para_home()
                break

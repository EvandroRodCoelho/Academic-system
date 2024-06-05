from service.page_service import NavegacaoService
from model.aulas_model import AulasModel
from views.aulas.aulas_tela import TelaAulas
import PySimpleGUI as sG
class AulasController:
    aulas = []
    selected_aula = None

    def __init__(self):
        self.window = None
        self.navegaçãoService = NavegacaoService()
        self.aulasModel = AulasModel()
        self.aulas = self.aulasModel.consultar_aulas()

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
            if event == 'Adicionar':
                self.window.close()
                self.navegaçãoService.navegar_para_adicionar_aula()
                break

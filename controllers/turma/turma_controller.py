from model.turmas_model import TurmasModel
from service.page_service import NavegacaoService
from views.turma.tela_turma import TelaTurmas
import PySimpleGUI as sG

class TurmasController:
    turmas = []
    navegaçãoService = NavegacaoService()
    selected_turma = None

    def __init__(self):
        self.window = None
        self.homeService = NavegacaoService()
        self.turmasModel = TurmasModel()
       # self.turmas = self.turmasModel.consultar_turmas()

    def mostrar_tela(self):
        self.window = TelaTurmas().window
        self.retorno()

    def retorno(self):
        while True:
            event, values = self.window.read()
            if event == sG.WIN_CLOSED or event == 'voltar':
                self.window.close()
                self.navegaçãoService.navegar_para_home()
                break

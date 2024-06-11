from model.horarios_model import HorariosModel
from service.page_service import NavegacaoService
from views.horarios.tela_horarios import TelaHorarios
import PySimpleGUI as sG

class HorariosController:
    def __init__(self):
        self.window = None
        self.navegaçãoService = NavegacaoService()
        self.horariosModel = HorariosModel()
        self.horarios = self.horariosModel.consultar_horarios()
        self.horario_selecionado = None

    def mostrar_tela(self):
        self.window = TelaHorarios(self.horarios).window
        self.retorno()

    def retorno(self):
        while True:
            event, values = self.window.read()
            if event == sG.WIN_CLOSED or event == 'voltar':
                self.window.close()
                self.navegaçãoService.navegar_para_home()
                break

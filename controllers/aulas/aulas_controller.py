from service.page_service import NavegacaoService
from model.aulas_model import AulasModel
from views.aulas.aulas_tela import TelaAulas
import PySimpleGUI as sG
class AulasController:
    def __init__(self):
        self.window = None
        self.navegaçãoService = NavegacaoService()
        self.aulasModel = AulasModel()
        self.aulas = self.aulasModel.consultar_aulas()
        self.aulaSelecionada = None

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
            if event == 'Editar':
                if self.aulaSelecionada:
                    self.window.close()
                    self.navegaçãoService.navegar_para_editar_aula(self.aulaSelecionada)
                    break
            if event == '-TABLE-':
                selected_row_index = values['-TABLE-'][0] if values['-TABLE-'] else None
                if selected_row_index is not None:
                    linha_selecionada = self.aulas[selected_row_index]
                    self.aulaSelecionada = {
                        'id': linha_selecionada[0],
                        'horario': linha_selecionada[1],
                        'professor': linha_selecionada[2],
                        'disciplina': linha_selecionada[3]
                    }
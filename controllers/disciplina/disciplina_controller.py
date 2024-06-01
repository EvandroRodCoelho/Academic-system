from views.disciplina.tela_disciplina import TelaDisciplina
from model.disciplina_model import DisciplinaModel
from service.page_service import NavegacaoService
import PySimpleGUI as sg

class DisciplinaController:
    disciplinas = []
    navegacaoService = NavegacaoService()
    selected_disciplina = None

    def __init__(self):
        self.window = None
        self.homeService = NavegacaoService()
        self.disciplinaModel = DisciplinaModel()
        self.disciplinas = self.disciplinaModel.consultar_disciplinas()

    def mostrar_tela(self):
        self.window = TelaDisciplina(self.disciplinas).window
        self.retorno()

    def retorno(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'voltar':
                self.window.close()
                self.navegacaoService.navegar_para_home()
                break
            if event == 'Adicionar':
                self.window.close()
                self.homeService.navegar_para_adicionar_disciplina()
                break
            if event == 'Excluir':
                if self.selected_disciplina:
                    self.disciplinaModel.excluir_disciplina(self.selected_disciplina['id'])
                    self.disciplinas = self.disciplinaModel.consultar_disciplinas()
                    self.window['-TABLE-'].update(values=self.disciplinas)
                    self.selected_disciplina = None
            if event == 'Editar':
                if self.selected_disciplina:
                    self.window.close()
                    self.navegacaoService.navegar_para_editar_disciplina(self.selected_disciplina)
                    break
            if event == '-TABLE-':
                selected_row_index = values['-TABLE-'][0] if values['-TABLE-'] else None
                if selected_row_index is not None:
                    linha_selecionada = self.disciplinas[selected_row_index]
                    self.selected_disciplina = {
                        'id': linha_selecionada[0],
                        'nome': linha_selecionada[1],
                        'id_professor': linha_selecionada[2],
                        'especialidade': linha_selecionada[3]
                    }

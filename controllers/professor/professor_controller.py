from views.professor.tela_professor import TelaProfessor
from model.professor_model import ProfessorModel
from service.page_service import NavegacaoService
import PySimpleGUI as sg


class ProfessorController:

    def __init__(self):
        self.window = None
        self.navegacaoService = NavegacaoService()
        self.professoresModel = ProfessorModel()
        self.professores = self.professoresModel.consultar_professores();
        self.professor_selecionado = None

    def mostrar_tela(self):
        self.window = TelaProfessor(self.professores).window
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
                self.navegacaoService.navegar_para_adicionar_professor()
                break
            if event == 'Excluir':
                if self.professor_selecionado:
                    self.professoresModel.excluir_professor(self.professor_selecionado['id'])
                    self.professores = self.professoresModel.consultar_professores()
                    self.window['-TABLE-'].update(values=self.professores)
                    self.professor_selecionado = None
            if event == 'Editar':
                if self.professor_selecionado:
                    self.window.close()
                    self.navegacaoService.navegar_para_editar_professor(self.professor_selecionado)
            if event == '-TABLE-':
                selected_row_index = values['-TABLE-'][0] if values['-TABLE-'] else None
                if selected_row_index is not None:
                    linha_selecionada = self.professores[selected_row_index]
                    self.professor_selecionado = {'id': linha_selecionada[0], 'nome': linha_selecionada[1]}

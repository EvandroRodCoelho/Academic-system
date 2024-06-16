from views.disciplina.tela_disciplina import TelaDisciplina
from model.disciplina_model import DisciplinaModel
from service.page_service import NavegacaoService
import PySimpleGUI as sg


class DisciplinaController:

    def __init__(self):
        self.window = None
        self.navegacaoService = NavegacaoService()
        self.disciplinaModel = DisciplinaModel()
        self.disciplinas = self.disciplinaModel.consultar_disciplinas()
        self.disciplina_selecionada = None

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
                self.navegacaoService.navegar_para_adicionar_disciplina()
                break
            if event == 'Excluir':
                if self.disciplina_selecionada:
                    self.disciplinaModel.excluir_disciplina(self.disciplina_selecionada['id'])
                    self.disciplinas = self.disciplinaModel.consultar_disciplinas()
                    self.window['-TABLE-'].update(values=self.disciplinas)
                    self.disciplina_selecionada = None
            if event == 'Editar':
                if self.disciplina_selecionada:
                    self.window.close()
                    self.navegacaoService.navegar_para_editar_disciplina(self.disciplina_selecionada)
                    break
            if event == '-TABLE-':
                selected_row_index = values['-TABLE-'][0] if values['-TABLE-'] else None
                if selected_row_index is not None:
                    linha_selecionada = self.disciplinas[selected_row_index]
                    self.disciplina_selecionada = {
                        'id': linha_selecionada[0],
                        'nome': linha_selecionada[1],
                        'id_professor': linha_selecionada[2],
                        'especialidade': linha_selecionada[3]
                    }

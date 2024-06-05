from model.disciplina_model import DisciplinaModel
from model.professor_model import ProfessorModel
from service.page_service import NavegacaoService
from model.aulas_model import AulasModel
from views.aulas.adicionar_aula import TelaAdicionarAula

import PySimpleGUI as sg

class AdicionarAulaController:

    def __init__(self):
        self.window = None
        self.disciplinaModel = DisciplinaModel()
        self.professorModel = ProfessorModel()
        self.aulasModel = AulasModel()
        self.navegacaoService = NavegacaoService()
        self.professores = self.obter_professores()
        self.disciplina = self.obter_disciplina()

    def obter_disciplina(self): 
        disciplina = self.disciplinaModel.consultar_disciplinas()
        return [(dip[0], dip[1]) for dip in disciplina]
    
    def obter_professores(self):
        professores = self.professorModel.consultar_professores()
        return [(prof[0], prof[1]) for prof in professores]

    def mostrar_tela(self):
        self.window = TelaAdicionarAula(self.professores, self.disciplina).window
        self.retorno()

    def retorno(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED or event == 'cancelar':
                self.window.close()
                self.navegacaoService.navegar_para_aulas()
                break

                


from model.disciplina_model import DisciplinaModel
from model.professor_model import ProfessorModel
from model.sala_de_aula_model import SalaDeAulaModel
from service.page_service import NavegacaoService
from views.sala_de_aula.editar_sala_de_aula import TelaEditarSalaDeAula
import PySimpleGUI as sg


class EditarSalaDeAulaController:

    def __init__(self, sala_de_aula):
        self.window = None
        self.sala_de_aula = sala_de_aula
        self.disciplinaModel = DisciplinaModel()
        self.professorModel = ProfessorModel()
        self.SalaDeAulaModel = SalaDeAulaModel()
        self.navegacaoService = NavegacaoService()
        self.professor = self.obter_professores()
        self.disciplina = self.obter_disciplina()

    def obter_disciplina(self):
        disciplina = self.disciplinaModel.consultar_disciplinas()
        return [(dip[0], dip[1]) for dip in disciplina]

    def obter_professores(self):
        professor = self.professorModel.consultar_professores()
        return [(prof[0], prof[1]) for prof in professor]

    def mostrar_tela(self):
        self.window = TelaEditarSalaDeAula(self.sala_de_aula, self.professor, self.disciplina).window
        self.retorno()

    def retorno(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED or event == 'cancelar':
                self.window.close()
                self.navegacaoService.navegar_para_salas_de_aula()
                break
            elif event == 'Salvar':
                try:
                    professor = values['professor']
                    disciplina = values['disciplina']
                    data = values['data']

                    id_disciplina = next(dis[0] for dis in self.disciplina if dis[1] == disciplina)
                    id_professor = next(prof[0] for prof in self.professor if prof[1] == professor)

                    self.SalaDeAulaModel.atualizar_sala_de_aula(id_disciplina, id_professor,
                                                                data, self.sala_de_aula['id'])

                    sg.popup('Sala de Aula atualizada com sucesso!', title='Sucesso')
                except Exception as e:
                    sg.popup_error(f"Erro ao editar sala de aula: {e}", title='Erro')
                    print(e)

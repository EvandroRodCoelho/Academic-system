from model.aluno_model import AlunoModel
from model.alunos_sala_de_aula_model import AlunosSalaDeAulaModel
from model.disciplina_model import DisciplinaModel
from model.professor_model import ProfessorModel
from model.sala_de_aula_model import SalaDeAulaModel
from service.page_service import NavegacaoService
from views.alunos_sala_de_aula.adicionar_alunos_sala_de_aula import AdicionarAlunosSalaDeAula
from views.sala_de_aula.adicionar_sala_de_aula import TelaAdicionarAula
import PySimpleGUI as sg


class AdicionarAlunosSalaDeAulaController:

    def __init__(self):
        self.window = None
        self.disciplinaModel = DisciplinaModel()
        self.professorModel = ProfessorModel()
        self.alunoModel = AlunoModel()
        self.salaDeAulaModel = SalaDeAulaModel()

        self.alunosSalaDeAulaModel = AlunosSalaDeAulaModel()
        self.navegacaoService = NavegacaoService()

        self.alunos = self.obter_alunos()
        self.professores = self.obter_professores()
        self.disciplinas = self.obter_disciplina()
        self.salas_de_aulas = self.obter_sala_de_aula()

    def obter_disciplina(self):
        disciplinas = self.disciplinaModel.consultar_disciplinas()
        return [(dip[0], dip[1]) for dip in disciplinas]

    def obter_professores(self):
        professores = self.professorModel.consultar_professores()
        return [(prof[0], prof[1]) for prof in professores]

    def obter_alunos(self):
        alunos = self.alunoModel.consultar_alunos()
        return [(aluno[0], aluno[1]) for aluno in alunos]

    def obter_sala_de_aula(self):
        salas_de_aulas = self.alunosSalaDeAulaModel.consultar_salas_de_aulas()
        return [(sal[0], sal[1]) for sal in salas_de_aulas]

    def mostrar_tela(self):
        self.window = AdicionarAlunosSalaDeAula(self.alunos, self.professores,
                                                self.disciplinas, self.salas_de_aulas).window
        self.retorno()

    def retorno(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED or event == 'cancelar':
                self.window.close()
                self.navegacaoService.navegar_para_alunos_sala_de_aula()
                break
            elif event == 'Cadastrar':
                try:
                    aluno = values['aluno']

                    id_aluno = next(dis[0] for dis in self.alunos if dis[1] == aluno)
                    id_sala_de_aula = next(dis[0] for dis in self.alunos if dis[1] == aluno)

                    self.alunosSalaDeAulaModel.adicionar_alunos_sala_de_aula(id_sala_de_aula, id_aluno)
                    sg.popup('Aluno cadastrado na sala de aula, com sucesso!', title='Sucesso')
                except Exception as e:
                    sg.popup_error(f"Erro ao cadastrar aula: {e}", title='Erro')
                    print(e)

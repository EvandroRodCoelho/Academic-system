from pyswip import Prolog
from model.aluno_model import AlunoModel
from model.professor_model import ProfessorModel
from service.page_service import NavegacaoService


class main:
    @staticmethod
    def inserir_dados_prolog():
        prolog = Prolog()
        professor_model = ProfessorModel()
        aluno_model = AlunoModel()

        prolog.consult("alunos_professor_mock.pl")

        for aluno in prolog.query("adicionar_aluno(Nome, Endereco)"):
            aluno_model.adicionar_aluno(str(aluno['Nome'].decode('utf-8')),
                                        str(aluno['Endereco'].decode('utf-8')))

        for professor in prolog.query("adicionar_professor(Nome)"):
            professor_model.adicionar_professor(str(professor['Nome'].decode('utf-8')))

    if __name__ == "__main__":
        home_controller = NavegacaoService()
        home_controller.navegar_para_home()

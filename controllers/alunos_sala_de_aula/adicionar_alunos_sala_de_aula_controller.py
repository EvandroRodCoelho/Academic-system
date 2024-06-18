from model.alunos_sala_de_aula_model import AlunosSalaDeAulaModel
from service.page_service import NavegacaoService
from views.sala_de_aula.adicionar_sala_de_aula import TelaAdicionarAula
import PySimpleGUI as sg


class AdicionarAlunosSalaDeAulaController:

    def __init__(self):
        self.window = None
        self.alunosSalaDeAulaModel = AlunosSalaDeAulaModel()
        self.navegacaoService = NavegacaoService()
        self.alunos = self.obter_alunos()

    def obter_alunos(self):
        alunos = self.alunosSalaDeAulaModel.consultar_alunos_sala_de_aula()
        return [(aluno[0], aluno[1]) for aluno in alunos]

    def mostrar_tela(self):
        self.window = TelaAdicionarAula(self.alunos).window
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

                    self.alunosSalaDeAulaModel.adicionar_alunos_sala_de_aula(id_aluno)
                    sg.popup('Aula cadastrada com sucesso!', title='Sucesso')
                except Exception as e:
                    sg.popup_error(f"Erro ao cadastrar aula: {e}", title='Erro')
                    print(e)

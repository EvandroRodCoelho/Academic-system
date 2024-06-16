from model.sala_de_aula_model import SalaDeAulaModel
from service.page_service import NavegacaoService
from views.sala_de_aula.sala_de_aula_por_id import TelaSalaDeAulaPorId
import PySimpleGUI as sG


class SalaDeAulaPorIdController:
    def __init__(self, aula):
        self.window = None
        self.aula = aula
        self.navegacaoService = NavegacaoService()
        self.salasDeAulaModel = SalaDeAulaModel()
        self.alunos = self.salasDeAulaModel.consultar_alunos_aula(self.aula['id'])
        self.alunos_com_notas = []
        for aluno in self.alunos:
            nota = self.salasDeAulaModel.pegar_alunos(self.aula['id_disciplina'], aluno[0])
            self.alunos_com_notas.append({'id': aluno[0], 'nome': aluno[1], 'endereco': aluno[2],
                                          'nota': nota[0][0] if nota else 0, 'faltas': nota[0][1]})

        self.values = [(aluno['id'], aluno['nome'], aluno['endereco'], aluno['nota'], aluno['faltas']) for aluno in
                       self.alunos_com_notas]

    def mostrar_tela(self):
        self.window = TelaSalaDeAulaPorId(self.aula, self.values).window
        self.retorno()

    def retorno(self):
        while True:
            event, values = self.window.read()
            if event == sG.WIN_CLOSED or event == 'Voltar':
                self.window.close()
                self.navegacaoService.navegar_para_home()
                break

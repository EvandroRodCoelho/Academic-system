from pyswip import Prolog

from model.aluno_model import AlunoModel
from service.page_service import NavegacaoService
from views.aluno.editar_aluno import TelaEditarAluno
import PySimpleGUI as sG


class EditarAlunoController:

    def __init__(self, aluno):
        self.window = None
        self.navegacaoService = NavegacaoService()
        self.aluno = aluno
        self.alunoModel = AlunoModel()
        self.prolog = Prolog()
        self.prolog.assertz("tamanho_campo_valido(X) :- string_length(X, Length), Length =< 100")

    def mostrar_tela(self):
        self.window = TelaEditarAluno(self.aluno).window
        self.retorno()

    def retorno(self):
        while True:
            event, values = self.window.read()

            if event == 'Salvar':
                nome = values['nome']
                endereco = values['endereco']

                if nome and endereco:
                    tamanho_nome_valido = list(self.prolog.query(f"tamanho_campo_valido('{nome}')"))
                    tamanho_endereco_valido = list(self.prolog.query(f"tamanho_campo_valido('{endereco}')"))

                    if not tamanho_nome_valido or not tamanho_endereco_valido:
                        sG.popup('Os campos tem uma tamanho máximo de 100 caracteres')
                    else:
                        self.alunoModel.atualizar_aluno(nome, endereco, self.aluno['id'])
                        self.navegacaoService.navegar_para_alunos()

                else:
                    sG.popup('Por favor, preencha todos os campos.')

            if event == sG.WIN_CLOSED or event == 'cancelar':
                self.window.close()
                self.navegacaoService.navegar_para_alunos()
                break

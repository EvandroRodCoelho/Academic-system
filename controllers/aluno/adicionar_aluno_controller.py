from pyswip import Prolog

from service.page_service import NavegacaoService
from views.aluno.adicionar_aluno import TelaAdicionarAluno
from model.aluno_model import AlunoModel
import PySimpleGUI as sG


class AdicionarAlunoController:
    def __init__(self):
        self.window = None
        self.alunoModel = AlunoModel()
        self.prolog = Prolog()

        self.prolog.assertz("tamanho_campo_valido(X) :- string_length(X, Length), Length =< 100")

    def mostrar_tela(self):
        self.window = TelaAdicionarAluno().window
        self.retorno()

    def retorno(self):
        while True:
            event, values = self.window.read()

            if event == 'Cadastrar':
                nome = values['nome']
                endereco = values['endereco']

                if nome and endereco:
                    tamanho_nome_valido = list(self.prolog.query(f"tamanho_campo_valido({nome})"))
                    tamanho_endereco_valido = list(self.prolog.query(f"tamanho_campo_valido({endereco})"))

                    if not tamanho_nome_valido or not tamanho_endereco_valido:
                        sG.popup('Os campos tem uma tamanho máximo de 100 caracteres')
                    else:
                        self.alunoModel.adicionar_aluno(nome, endereco)
                        sG.popup('Cadastro realizado com sucesso!', f'Nome: {nome}\nEndereço: {endereco}')
                else:
                    sG.popup('Por favor, preencha todos os campos.')

            if event == sG.WIN_CLOSED or event == 'cancelar':
                self.window.close()
                paginaService = NavegacaoService()
                paginaService.navegar_para_alunos()
                break

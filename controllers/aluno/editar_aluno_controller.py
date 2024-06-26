from pyswip import Prolog

from model.aluno_model import AlunoModel
from service.page_service import NavegacaoService
from validations.validators import validar_tamanho_campo, validar_caracteres_especiais, validar_caracteres_numericos
from views.aluno.editar_aluno import TelaEditarAluno
import PySimpleGUI as sG


class EditarAlunoController:

    def __init__(self, aluno):
        self.window = None
        self.navegacaoService = NavegacaoService()
        self.aluno = aluno
        self.alunoModel = AlunoModel()

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
                    tamanho_nome_valido = validar_tamanho_campo(nome)
                    caracteres_numericos_nome = validar_caracteres_numericos(nome)
                    caracteres_especiais_nome = validar_caracteres_especiais(nome)
                    tamanho_endereco_valido = validar_tamanho_campo(endereco)

                    if not tamanho_nome_valido or not tamanho_endereco_valido:
                        sG.popup('Os campos devem ter um tamanho mínimo de 3 caracteres e máximo de 100 caracteres')
                    elif not caracteres_numericos_nome or not caracteres_especiais_nome:
                        sG.popup('O campo de Nome não pode conter caracteres numéricos ou especiais (exceto espaços)')
                    else:
                        self.alunoModel.atualizar_aluno(nome, endereco, self.aluno['id'])
                        self.navegacaoService.navegar_para_alunos()
                else:
                    sG.popup('Por favor, preencha todos os campos.')

            if event == sG.WIN_CLOSED or event == 'cancelar':
                self.window.close()
                self.navegacaoService.navegar_para_alunos()
                break

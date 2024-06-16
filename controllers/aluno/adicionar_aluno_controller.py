from service.page_service import NavegacaoService
from validations.validators import validar_tamanho_campo, validar_caracteres_numericos, validar_caracteres_especiais
from views.aluno.adicionar_aluno import TelaAdicionarAluno
from model.aluno_model import AlunoModel
import PySimpleGUI as sG


class AdicionarAlunoController:
    def __init__(self):
        self.window = None
        self.alunoModel = AlunoModel()

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
                    tamanho_nome_valido = validar_tamanho_campo(nome)
                    caracteres_numericos_nome = validar_caracteres_numericos(nome)
                    caracteres_especiais_nome = validar_caracteres_especiais(nome)
                    tamanho_endereco_valido = validar_tamanho_campo(endereco)

                    if not tamanho_nome_valido or not tamanho_endereco_valido:
                        sG.popup('Os campos devem ter um tamanho mínimo de 3 caracteres e máximo de 100 caracteres')
                    elif not caracteres_numericos_nome or not caracteres_especiais_nome:
                        sG.popup('O campo de Nome não pode conter caracteres numéricos ou especiais (exceto espaços)')
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

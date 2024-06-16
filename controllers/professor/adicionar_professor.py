from model.professor_model import ProfessorModel
from service.page_service import NavegacaoService
from validations.validators import validar_tamanho_campo, validar_caracteres_numericos, validar_caracteres_especiais
from views.professor.adicionar_professor import TelaAdicionarProfessor
import PySimpleGUI as sg


class AdicionarProfessorController:

    def __init__(self):
        self.window = None
        self.professorModel = ProfessorModel()
        self.navegacaoService = NavegacaoService()

    def mostrar_tela(self):
        self.window = TelaAdicionarProfessor().window
        self.retorno()

    def retorno(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED or event == 'cancelar':
                self.window.close()
                self.navegacaoService.navegar_para_professores()
                break

            if event == 'Cadastrar':

                nome = values['nome']

                if nome:
                    tamanho_nome_valido = validar_tamanho_campo(nome)
                    caracteres_numericos_nome = validar_caracteres_numericos(nome)
                    caracteres_especiais_nome = validar_caracteres_especiais(nome)

                    if not tamanho_nome_valido:
                        sg.popup('Os campos devem ter um tamanho mínimo de 3 caracteres e máximo de 100 caracteres')
                    elif not caracteres_numericos_nome or not caracteres_especiais_nome:
                        sg.popup('O campo de Nome não pode conter caracteres numéricos ou especiais (exceto espaços)')
                    else:
                        self.professorModel.adicionar_professor(nome)
                        sg.popup('Cadastro realizado com sucesso!', f'Nome: {nome}')
                else:
                    sg.popup('Por favor, preencha todos os campos.')

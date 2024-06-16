from model.professor_model import ProfessorModel
from service.page_service import NavegacaoService
from model.disciplina_model import DisciplinaModel
from validations.validators import validar_tamanho_campo, validar_caracteres_numericos, validar_caracteres_especiais
from views.disciplina.editar_disciplina import TelaEditarDisciplina
import PySimpleGUI as sg


class EditarDisciplinaController:
    def __init__(self, disciplina):
        self.window = None
        self.disciplina = disciplina
        self.navegacaoService = NavegacaoService()
        self.disciplinaModel = DisciplinaModel()
        self.professorModel = ProfessorModel()
        self.professores = self.obter_professores()

    def obter_professores(self):
        professores = self.professorModel.consultar_professores()
        return [(prof[0], prof[1]) for prof in professores]

    def mostrar_tela(self):
        self.window = TelaEditarDisciplina(self.professores, self.disciplina).window
        self.retorno()

    def retorno(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'cancelar':
                self.window.close();
                self.navegacaoService.navegar_para_disciplina()
                break
            if event == 'Salvar':
                nome = values['nome']
                professor_selecionado = values['professor']
                especialidade = values['especialidade']

                if nome and professor_selecionado and especialidade:
                    tamanho_nome_valido = validar_tamanho_campo(nome)
                    caracteres_numericos_nome = validar_caracteres_numericos(nome)
                    caracteres_especiais_nome = validar_caracteres_especiais(nome)
                    tamanho_especialidade_valido = validar_tamanho_campo(especialidade)
                    caracteres_especiais_especialidade = validar_caracteres_especiais(especialidade)

                    if not tamanho_nome_valido or not tamanho_especialidade_valido:
                        sg.popup('Os campos devem ter um tamanho mínimo de 3 caracteres e máximo de 100 caracteres')
                    elif not caracteres_numericos_nome or not caracteres_especiais_nome:
                        sg.popup('O campo de Nome não pode conter caracteres numéricos ou especiais (exceto espaços)')
                    elif not caracteres_especiais_especialidade:
                        sg.popup('O campo de Especialidade não pode conter caracteres especiais (exceto espaços)')
                    else:
                        id_professor = next(prof[0] for prof in self.professores if prof[1] == professor_selecionado)
                        self.disciplinaModel.atualizar_disciplina(self.disciplina['id'], nome, id_professor,
                                                                  especialidade)
                        sg.popup('Cadastro realizado com sucesso!', f'Nome: {nome}',
                                 f'Professor: {professor_selecionado}', f'Especialidade: {especialidade}')

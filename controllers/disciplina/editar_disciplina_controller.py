from model.professor_model import ProfessorModel
from service.page_service import NavegacaoService
from model.disciplina_model import DisciplinaModel
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
        self.window = TelaEditarDisciplina(self.professores,self.disciplina).window
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
                    if len(nome) > 100 or len(especialidade) > 100:
                        sg.popup('Os campos têm um tamanho máximo de 100 caracteres')
                    else:
                        id_professor = next(prof[0] for prof in self.professores if prof[1] == professor_selecionado)
                        self.disciplinaModel.atualizar_disciplina(self.disciplina['id'],nome, id_professor, especialidade)
                        sg.popup('Cadastro realizado com sucesso!', f'Nome: {nome}', f'Professor: {professor_selecionado}', f'Especialidade: {especialidade}')
from model.aluno_model import AlunoModel
from service.page_service import NavegacaoService
from views.aluno.editar_aluno  import TelaEditarAluno
import PySimpleGUI as sg
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
                 if len(nome) > 100 or len(endereco) > 100:
                  sg.popup('Os campos tem uma tamanho máximo de 100 caracteres')
                 else:
                    self.alunoModel.atualizar_aluno(nome,endereco,self.aluno['id'])
                    self.navegacaoService.navegar_para_alunos();

            else:
                sg.popup('Por favor, preencha todos os campos.')
        
        if event == sg.WIN_CLOSED or event == 'cancelar':
            self.window.close();
            self.navegacaoService.navegar_para_alunos()
            break


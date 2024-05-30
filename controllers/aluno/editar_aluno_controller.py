from database.aluno import editar_aluno
from service.page_service import NavegacaoService
from views.aluno.editar_aluno  import TelaEditarAluno
import PySimpleGUI as sg
class EditarAlunoController:

    def __init__(self, aluno):
        self.window = None
        self.paginaService = NavegacaoService()
        self.aluno = aluno
        self.navegacaoService = NavegacaoService()
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
                    editar_aluno(self.aluno['id'],nome,endereco)
                    self.navegacaoService.navegar_para_alunos();

            else:
                sg.popup('Por favor, preencha todos os campos.')
        
        if event == sg.WIN_CLOSED or event == 'cancelar':
            self.window.close();
            self.paginaService.navegar_para_alunos()
            break


from service.page_service import NavegacaoService
from views.aluno.adicionar_aluno import TelaAdicionarAluno
#from model.queries_prolog import prolog;
from model.aluno_model import AlunoModel
import PySimpleGUI as sg
class AdicionarAlunoController:
    def __init__(self):
        self.window = None
        self.alunoModel = AlunoModel();
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
                 if len(nome) > 100 or len(endereco) > 100:
                  sg.popup('Os campos tem uma tamanho máximo de 100 caracteres')
                 else:
                    self.alunoModel.adicionar_aluno(nome,endereco)
                  #  prolog.assertz(f"aluno('{nome}')")
                    sg.popup('Cadastro realizado com sucesso!', f'Nome: {nome}\nEndereço: {endereco}')
            else:
                sg.popup('Por favor, preencha todos os campos.')
        
        if event == sg.WIN_CLOSED or event == 'cancelar':
            self.window.close();
            paginaService = NavegacaoService()
            paginaService.navegar_para_alunos()
            break


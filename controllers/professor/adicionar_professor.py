from database.professores import adicionar
from service.page_service import NavegacaoService
from views.professor.adicionar_professor import TelaAdicionarProfessor
import PySimpleGUI as sg
class AdicionarProfessorController:

    def __init__(self):
        self.window = None
      
    def mostrar_tela(self):
        self.window = TelaAdicionarProfessor().window
        self.retorno()
    def add_professor(self, conexao, nome):
        query = "INSERT INTO professor (nome) VALUES (?)"
        conexao.executar_sql(query, (nome,))
       
    def retorno(self):
     while True:
        event, values = self.window.read()

        if event == sg.WIN_CLOSED or event == 'cancelar':
            self.window.close();
            paginaService = NavegacaoService()
            paginaService.navegar_para_professores()
            break

        if event == 'Cadastrar':
            nome = values['nome']
            if nome:
                 if len(nome) > 100:
                  sg.popup('Os campos tem uma tamanho máximo de 100 caracteres')
                 else:
                    adicionar(nome)
                    sg.popup('Cadastro realizado com sucesso!', f'Nome: {nome}')
                    
                   
            else:
                sg.popup('Por favor, preencha todos os campos.')
        


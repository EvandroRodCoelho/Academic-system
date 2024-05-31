from model.professor_model import ProfessorModel
from service.page_service import NavegacaoService
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
            self.window.close();
            self.navegacaoService.navegar_para_professores()
            break

        if event == 'Cadastrar':
            nome = values['nome']
            if nome:
                 if len(nome) > 100:
                  sg.popup('Os campos tem uma tamanho máximo de 100 caracteres')
                 else:
                    self.professorModel.adicionar_professor(nome)
                    sg.popup('Cadastro realizado com sucesso!', f'Nome: {nome}')            
            else:
                sg.popup('Por favor, preencha todos os campos.')
        


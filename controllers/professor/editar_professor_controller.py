from database.professores import editar_professor
from service.page_service import NavegacaoService
from views.professor.editar_professor import TelaEditarProfessor
import PySimpleGUI as sg
class EditarProfessorController:

    def __init__(self, professor):
        self.window = None
        self.paginaService = NavegacaoService()
        self.professor = professor
        self.navegacaoService = NavegacaoService()
    def mostrar_tela(self):
        self.window = TelaEditarProfessor(self.professor).window
        self.retorno()
    
    def retorno(self):
     while True:
        event, values = self.window.read()
        
        if event == 'Salvar':
            nome = values['nome']
            if nome:
                 if len(nome) > 100:
                  sg.popup('Os campos tem uma tamanho máximo de 100 caracteres')
                 else:
                    editar_professor(self.professor['id'],nome)
                    self.navegacaoService.navegar_para_professores();

            else:
                sg.popup('Por favor, preencha todos os campos.')
        
        if event == sg.WIN_CLOSED or event == 'cancelar':
            self.window.close();
            self.paginaService.navegar_para_professores()
            break


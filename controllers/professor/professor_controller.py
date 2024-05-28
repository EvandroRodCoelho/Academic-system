from database.conexao import Conexao
from database.professores import buscar_professores
from views.professor.tela_professor import TelaProfessor
from service.page_service import NavegacaoService
import PySimpleGUI as sg

class ProfessorController: 
    professores= []
    navegaçãoService = NavegacaoService(); 
    def __init__(self):
        self.window = None   
        self.professores = buscar_professores();

    def mostrar_tela(self):
        self.window = TelaProfessor(self.professores).window
        self.retorno()
    
    def retorno(self):
     while True:
        event, values = self.window.read()
        if event == sg.WIN_CLOSED or event == 'voltar':
            break
        if event == 'Adicionar': 
            self.window.close()
            homeService = NavegacaoService()
            homeService.navegar_para_adicionar_professor()
            break

    

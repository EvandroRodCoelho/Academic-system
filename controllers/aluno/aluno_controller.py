# from controllers.home_controller import HomeController
from views.aluno.tela_alunos import TelaAlunos
from service.page_service import NavegacaoService
import PySimpleGUI as sg

class AlunoController:
    def __init__(self):
        self.window = None

    def mostrar_tela(self):
        self.window = TelaAlunos().window
        self.retorno()
    
    def retorno(self):
        while True:
            event, values = self.window.read()
            if event == 'Visualizar':
                self.window.close()
                homeService = NavegacaoService()
                homeService.navegar_para_visualizar_alunos()
                break
            if event == 'Adicionar': 
                self.window.close()
                homeService = NavegacaoService()
                homeService.navegar_para_adicionar_alunos()
                break
            if event == sg.WIN_CLOSED or event == 'Sair':
                self.window.close()
               # self.home_controller.mostrar_tela_principal()
                break

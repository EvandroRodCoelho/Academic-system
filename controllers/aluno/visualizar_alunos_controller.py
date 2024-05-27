from database.aluno import buscar_alunos
from service.page_service import NavegacaoService
from views.aluno.visualizar_aluno import VisualizarAlunoView
import PySimpleGUI as sg
class VisualizarAlunoController:
    def __init__(self):
        self.window = None
    def mostrar_tela(self):
        alunos = buscar_alunos() 
        self.window = VisualizarAlunoView(alunos).window
        self.retorno()
    def retorno(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED or event == 'Fechar':
                self.window.close();
                paginaService = NavegacaoService()
                paginaService.navegar_para_alunos()
                break
        

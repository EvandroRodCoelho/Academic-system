from views.professor.tela_professor import TelaProfessor
from service.page_service import NavegacaoService
import PySimpleGUI as sg

class ProfessorController: 
    def __init__(self):
        self.window = None
    
    def mostrar_tela(self):
        self.window = TelaProfessor().window
        self.retorno()
    
    def retorno(self):
     while True:
        event, values = self.window.read()

        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break
        if event == 'Adicionar': 
            self.window.close()
            homeService = NavegacaoService()
            homeService.na()
            break

    

from views.home import HomeView
import PySimpleGUI as sg
from service.page_service import NavegacaoService
class HomeController:
    def __init__(self):
        self.window = None

    def mostrar_tela(self):
        self.window = HomeView().window
        self.retorno()

    def retorno(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED or event == 'Sair':
                break
            if event == 'Alunos':
                  self.window.close();
                  paginaService = NavegacaoService()
                  paginaService.navegar_para_alunos();
            
            elif event == 'Professores':
                self.window.close();
                paginaService = NavegacaoService()
                paginaService.navegar_para_professores()

            elif event == 'Disciplinas':
                sg.popup('Navegar para a tela de Disciplinas')

            elif event == 'Turmas':
                sg.popup('Navegar para a tela de Turmas')
 

            elif event == 'Salas de Aulas':
                sg.popup('Navegar para a tela de Salas de Aulas')

            elif event == 'Horários':
                sg.popup('Navegar para a tela de Horários')

            elif event == 'Aulas':
                sg.popup('Navegar para a tela de Aulas')

        self.window.close()

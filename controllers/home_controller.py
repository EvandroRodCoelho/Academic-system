from views.home import HomeView
import PySimpleGUI as sg
from service.page_service import NavegacaoService
class HomeController:
    def __init__(self):
        self.window = None
        self.paginaService = NavegacaoService()

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
                self.paginaService.navegar_para_professores()

            elif event == 'Disciplinas':
                 self.window.close();
                 self.paginaService.navegar_para_disciplina()

            elif event == 'Salas de Aulas':
                self.window.close()
                self.paginaService.navegar_para_salas_de_aula()

            elif event == 'Horários':
               self.window.close()
               self.paginaService.navegar_para_horarios()

            elif event == 'Aulas':
                self.window.close()
                self.paginaService.navegar_para_aulas()

        self.window.close()

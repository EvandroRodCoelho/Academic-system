# from controllers.home_controller import HomeController
from database.aluno import buscar_alunos
from views.aluno.tela_alunos import TelaAlunos
from service.page_service import NavegacaoService
import PySimpleGUI as sg

class AlunoController:
    alunos = buscar_alunos() 
    def __init__(self):
        self.window = None

    def mostrar_tela(self):
        self.window = TelaAlunos(self.alunos).window
        self.retorno()
    
    def retorno(self):
        while True:
            event, values = self.window.read()
            print(event)
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
            if event == '-TABLE-': 
                selected_row_index = values['-TABLE-'][0] if values['-TABLE-'] else None
                if selected_row_index is not None:
                    selected_aluno = self.alunos[selected_row_index]
                    self.window.close()
                    homeService = NavegacaoService()
                    homeService.navegar_para_adicionar_alunos()
                    sg.popup(f'Você selecionou o aluno:\n\nID: {selected_aluno[0]}\nNome: {selected_aluno[1]}\nEndereço: {selected_aluno[2]}')


            if event == sg.WIN_CLOSED or event == 'Sair':
                self.window.close()
                break

# from controllers.home_controller import HomeController
from database.aluno import buscar_alunos
from views.aluno.tela_alunos import TelaAlunos
from service.page_service import NavegacaoService
import PySimpleGUI as sg

class AlunoController:
    alunos = []
    navegaçãoService = NavegacaoService(); 
    def __init__(self):
        self.window = None
        self.alunos = buscar_alunos()

    def mostrar_tela(self):
        self.window = TelaAlunos(self.alunos).window
        self.retorno()
    
    def retorno(self):
        while True:
            event, values = self.window.read()
            if event == 'Adicionar': 
                self.window.close()
                self.navegaçãoService.navegar_para_adicionar_alunos()
                break
            # Caso implementar Edição 
            # if event == '-TABLE-': 
            #     selected_row_index = values['-TABLE-'][0] if values['-TABLE-'] else None
            
            #     if selected_row_index is not None:
            #         selected_aluno = self.alunos[selected_row_index]
            #         #    self.window.close()
            #         # homeService = NavegacaoService()
            #         # homeService.navegar_para_adicionar_alunos()
            #         sg.popup(f'Você selecionou o aluno:\n\nID: {selected_aluno[0]}\nNome: {selected_aluno[1]}\nEndereço: {selected_aluno[2]}')


            if event == sg.WIN_CLOSED or event == 'voltar':
                self.window.close()
                self.navegaçãoService.navegar_para_home()
                break

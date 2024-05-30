from database.conexao import Conexao
from database.professores import buscar_professores
from views.professor.tela_professor import TelaProfessor
from service.page_service import NavegacaoService
import PySimpleGUI as sg

class ProfessorController: 
    professores= []
    navegaçãoService = NavegacaoService(); 
    selected_professor = None
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
            
        if event == 'Editar': 
                if self.selected_professor:
                    self.window.close()
                    self.navegaçãoService.navegar_para_editar_professor(self.selected_professor)
        if event == '-TABLE-': 
                selected_row_index = values['-TABLE-'][0] if values['-TABLE-'] else None
                if selected_row_index is not None:
                  linha_selecionada = self.professores[selected_row_index]
                  self.selected_professor =  {'id': linha_selecionada[0], 'nome': linha_selecionada[1]}

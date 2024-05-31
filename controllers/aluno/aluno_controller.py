from database.aluno import buscar_alunos
from service.page_service import NavegacaoService
from database.aluno import excluir
from views.aluno.tela_alunos import TelaAlunos
import PySimpleGUI as sg

class AlunoController:
    alunos = []
    selected_aluno = None
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
            if event == 'Editar': 
                if self.selected_aluno:
                    self.window.close()
                    self.navegaçãoService.navegar_para_editar_alunos(self.selected_aluno)
            if event == 'Excluir':
                if self.selected_aluno:
                    excluir(self.selected_aluno['id'])
                    self.alunos = buscar_alunos();
                    self.window['-TABLE-'].update(values=self.alunos)
                    self.selected_aluno = None

            if event == '-TABLE-': 
                selected_row_index = values['-TABLE-'][0] if values['-TABLE-'] else None
            
                if selected_row_index is not None:
                  linha_selecionada = self.alunos[selected_row_index]
                  self.selected_aluno =  {'id': linha_selecionada[0], 'nome': linha_selecionada[1], 'endereco': linha_selecionada[2]}
  
            if event == sg.WIN_CLOSED or event == 'voltar':
                self.window.close()
                self.navegaçãoService.navegar_para_home()
                break

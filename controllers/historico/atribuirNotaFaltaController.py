from model.historico_aluno_model import HistoricoAlunoModel
from views.historico.tela_atribuir_nota_falta import TelaAtribuirNotaFalta
import PySimpleGUI as sg
from service.page_service import NavegacaoService
from validations.validators import validar_nota, validar_falta

class AtribuirNotaFaltaController:
    def __init__(self, id_aluno, id_disciplina):
        self.window = None
        self.id_aluno = id_aluno
        self.id_disciplina = id_disciplina
        self.historicoAlunoModel = HistoricoAlunoModel()
        self.navegacaoService = NavegacaoService()

    def mostrar_tela(self):
        self.window = TelaAtribuirNotaFalta().window
        self.retorno()

    def retorno(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Cancelar':
                self.window.close()
                self.navegacaoService.navegar_para_historico()
                break
            elif event == 'confirmar':
                notas = values['nota']
                faltas = values['faltas']
                if notas.isdigit() and faltas.isdigit():
                    notas = int(notas)
                    faltas = int(faltas)
                    if validar_nota(notas) and validar_falta(faltas): 
                        if self.historicoAlunoModel.pegar_alunos(self.id_disciplina, self.id_aluno):
                            self.atribuir_nota_e_falta(notas, faltas)
                            sg.popup("Nota e faltas atribuídas com sucesso!")
                        else:
                            self.adicionar_historico(notas, faltas)
                            sg.popup("Nota e faltas atribuídas com sucesso!")
                    else:
                        sg.popup_error("Por favor, digite números válidos para nota (0-10) faltas (0-45)")
                else:
                    sg.popup_error("Por favor, digite números válidos para nota e faltas.")

    def atribuir_nota_e_falta(self, notas, faltas):
        self.historicoAlunoModel.atribuir_nota_e_falta(self.id_aluno, self.id_disciplina, notas, faltas)

    def adicionar_historico(self, notas, faltas):
        self.historicoAlunoModel.adicionar_historico_alunos(self.id_aluno, self.id_disciplina, notas, faltas)

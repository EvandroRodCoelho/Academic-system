from model.historico_aluno_model import HistoricoAlunoModel
from views.historico.tela_atribuir_nota_falta import TelaAtribuirNotaFalta
import PySimpleGUI as sg
from service.page_service import NavegacaoService


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
                print(self.id_aluno)
                nota = values['nota']
                faltas = values['faltas']
                print(nota, faltas)
                if nota.isdigit() and faltas.isdigit():

                    nota = int(nota)
                    faltas = int(faltas)
                    self.atribuir_nota_e_falta(nota, faltas)
                    sg.popup("Nota e faltas atribuídas com sucesso!")

                else:
                    sg.popup_error("Por favor, digite números válidos para nota e faltas.")

    def atribuir_nota_e_falta(self, nota, faltas):
        self.historicoAlunoModel.atribuir_nota_e_falta(self.id_aluno, self.id_disciplina, nota, faltas)

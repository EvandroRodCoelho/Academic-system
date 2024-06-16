from pyswip import Prolog
import PySimpleGUI as sg
from model.sala_de_aula_model import SalaDeAulaModel
from model.aluno_model import AlunoModel
from service.page_service import NavegacaoService
from views.historico.tela_historico import TelaHistorico

class HistoricoController:
    def __init__(self):
        self.window = None
        self.alunosModel = AlunoModel()
        self.salaDeAulaModel = SalaDeAulaModel()
        self.navegacaoService = NavegacaoService()
        self.salas = self.salaDeAulaModel.consultar_salas_aulas()
        self.alunos = self.alunosModel.consultar_alunos()
        self.prolog = Prolog()
        self.prolog.assertz("faltas_aceitaveis(Faltas) :- Faltas =< 10") 
        self.prolog.assertz("nota_suficiente(Nota) :- Nota >= 6")

    def mostrar_tela(self):
        formatted_salas = [f"{sala[0]} {sala[1]} - {sala[2]}" for sala in self.salas]
        self.window = TelaHistorico(formatted_salas, self.alunos).window
        self.retorno()

    def retorno(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'voltar':
                self.window.close()
                self.navegacaoService.navegar_para_home()
                break
            

               
            elif event == 'Buscar':
                aluno_selecionado = values['aluno']
                sala_selecionada = values['sala']
                
                if aluno_selecionado and sala_selecionada:
                    id_sala = int(sala_selecionada.split()[0]) 
                    id_aluno = int(aluno_selecionado.split()[0]) 
                   
                    id_disciplina = self.salaDeAulaModel.consultar_por_id_salas(id_sala)
                
                    dados_historico = self.salaDeAulaModel.pegar_alunos(id_disciplina[0][4], id_aluno)
                    
                    historico = self.processar_historico(dados_historico, aluno_selecionado)
                    self.window['tabela'].update(values=historico)
                  
                else:
                    sg.popup("Por favor, selecione um aluno e uma sala.")

    
    def processar_historico(self, historico, aluno):
        dados_tabela = []
        aluno_id = int(aluno.split()[0]) 
        aluno_nome = aluno.split()[1]
        for registro in historico:
            nota, faltas = registro
            situacao = self.verificar_situacao(nota, faltas)
            dados_tabela.append([aluno_id, aluno_nome, nota, faltas, situacao])
        return dados_tabela

    def verificar_situacao(self, nota, faltas):      
        faltas_query = f"faltas_aceitaveis({faltas})"
        nota_query = f"nota_suficiente({nota})"
        try:
            faltas_aceitaveis = list(self.prolog.query(faltas_query))
            nota_suficiente = list(self.prolog.query(nota_query))
            
            if faltas_aceitaveis and nota_suficiente:
                return 'Aprovado'
            else:
                return 'Reprovado'
        except Exception as e:
            print(f"Erro durante a consulta Prolog: {str(e)}")
            return 'Erro'
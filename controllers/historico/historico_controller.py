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
        self.configurar_prolog()

    def configurar_prolog(self):
        self.prolog.assertz("faltas_aceitaveis(Faltas) :- Faltas =< 10") 
        self.prolog.assertz("nota_suficiente(Nota) :- Nota >= 6")

    def mostrar_tela(self):
        formatted_salas = [f"{sala[0]} - {sala[1]} - {sala[2]}" for sala in self.salas]
        self.window = TelaHistorico(formatted_salas, self.alunos).window
        self.retorno()

    def retorno(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'voltar':
                self.fechar_janela()
                break
            elif event == 'Buscar':
                self.buscar_historico(values)
            elif event == 'att-falta':
                self.atribuir_falta(values)

    def fechar_janela(self):
        self.window.close()
        self.navegacaoService.navegar_para_home()

    def buscar_historico(self, values):
        aluno_selecionado = values.get('aluno')
        sala_selecionada = values.get('sala')
        if aluno_selecionado and sala_selecionada:
            id_sala, id_aluno = self.obter_ids(sala_selecionada, aluno_selecionado)
            dados_historico = self.obter_dados_historico(id_sala, id_aluno)
            historico = self.processar_historico(dados_historico, aluno_selecionado)
            self.window['tabela'].update(values=historico)
        else:
            sg.popup("Por favor, selecione um aluno e uma sala.")

    def atribuir_falta(self, values):
        aluno_selecionado = values.get('aluno')
        sala_selecionada = values.get('sala')
        if aluno_selecionado & sala_selecionada:
            id_sala, id_aluno = self.obter_ids(sala_selecionada, aluno_selecionado)
            id_disciplina = self.obter_id_disciplina(id_sala)
            self.salaDeAulaModel.atribuir_falta(id_aluno, id_disciplina)
            dados_historico = self.obter_dados_historico(id_sala, id_aluno)
            historico = self.processar_historico(dados_historico, aluno_selecionado)
            self.window['tabela'].update(values=historico)
        else:
            sg.popup("Por favor, selecione um aluno e uma sala.")

    def obter_ids(self, sala_selecionada, aluno_selecionado):
        id_sala = int(sala_selecionada.split()[0]) 
        id_aluno = int(aluno_selecionado.split()[0]) 
        return id_sala, id_aluno

    def obter_id_disciplina(self, id_sala):
        consultar_salas_por_id = self.salaDeAulaModel.consultar_por_id_salas(id_sala)
        return consultar_salas_por_id[0][4]

    def obter_dados_historico(self, id_sala, id_aluno):
        id_disciplina = self.obter_id_disciplina(id_sala)
        return self.salaDeAulaModel.pegar_alunos(id_disciplina, id_aluno)

    def processar_historico(self, historico, aluno):
        dados_tabela = []
        aluno_id, aluno_nome = self.extrair_dados_aluno(aluno)
        for registro in historico:
            nota, faltas = registro
            situacao = self.verificar_situacao(nota, faltas)
            dados_tabela.append([aluno_id, aluno_nome, nota, faltas, situacao])
        return dados_tabela

    def extrair_dados_aluno(self, aluno):
        aluno_id = int(aluno.split()[0]) 
        aluno_nome = aluno.split()[1]
        return aluno_id, aluno_nome

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
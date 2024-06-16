import sqlite3
from database.conexao import Conexao

class HistoricoAlunoModel:
    def __init__(self):
        self.db = Conexao()

    def pegar_alunos(self, id_disciplina, id_aluno):
        try:
            self.db.iniciar_conn()
            query = '''
                SELECT notas, faltas
                FROM historico_alunos
                WHERE id_disciplina = ? AND id_aluno = ?
            '''
            self.db.executar_sql(query, (id_disciplina, id_aluno))
            return self.db.fetchall()
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a busca: {e}")
        finally:
            self.db.fechar_conn()

    def obter_dados_historico(self, aluno_id, id_sala):
        try:
            self.db.iniciar_conn()
            query = '''
                SELECT notas, faltas 
                FROM historico_alunos
                WHERE id_aluno = ? AND id_sala = ?
            '''
            self.db.executar_sql(query, (aluno_id, id_sala))
            return self.db.fetchall()
        except sqlite3.Error as e:
            print(f"Erro ao buscar dados do histórico: {e}")
        finally:
            self.db.fechar_conn()

    def atribuir_falta(self, id_aluno, disciplina_id):
        try:
            self.db.iniciar_conn()
            query = '''
                UPDATE historico_alunos
                SET faltas = faltas + 1
                WHERE id_aluno = ? AND id_disciplina = ?
            '''
            self.db.executar_sql(query, (id_aluno, disciplina_id))
        except Exception as e:
            print(f"Erro ao atribuir falta: {str(e)}")
        finally:
            self.db.fechar_conn()
import sqlite3
from database.conexao import Conexao


class SalaDeAulaModel:
    def __init__(self):
        self.db = Conexao()

    def consultar_salas_aulas(self):
        try:
            self.db.iniciar_conn()
            query = '''
        SELECT ga.id, p.nome AS professor,d.nome AS disciplina, ga.horario, d.id
        FROM grade_aulas ga
        JOIN professor p ON ga.id_professor = p.id
        JOIN disciplina d ON ga.id_disciplina = d.id
      '''
            self.db.executar_sql(query)

            return self.db.fetchall()
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a busca: {e.args[0]}")
        finally:
            self.db.fechar_conn()

    def consultar_alunos_aula(self, id_aula):
        try:
            self.db.iniciar_conn()
            query = '''
            SELECT a.id, a.nome, a.endereco
            FROM salas_aulas sa
            JOIN aluno a ON sa.id_aluno = a.id
            WHERE sa.id_aula = ?
        '''
            self.db.executar_sql(query, (id_aula,))
            return self.db.fetchall()
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a busca: {e}")
        finally:
            self.db.fechar_conn()

    def pegar_alunos(self, id_disciplina, id_aluno):
        try:
            self.db.iniciar_conn()
            query = '''
            SELECT notas, faltas
            FROM historico_alunos
            WHERE id_disciplina = ? AND id_aluno = ?
        '''
            self.db.executar_sql(query, (id_disciplina, id_aluno,))
            return self.db.fetchall()
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a busca: {e}")
        finally:
            self.db.fechar_conn()

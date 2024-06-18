import sqlite3
from database.conexao import Conexao


class SalaDeAulaModel:
    def __init__(self):
        self.db = Conexao()

    def adicionar_sala_de_aula(self, id_professor, id_disciplina, data):
        try:
            self.db.iniciar_conn()
            query = "INSERT INTO salas_aulas (id_professor, id_disciplina, data) VALUES (?, ?, ?)"
            self.db.executar_sql(query, (id_professor, id_disciplina, data))
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a inserção: {e.args[0]}")
        finally:
            self.db.fechar_conn()

    def consultar_sala_de_aula_id(self, id_sala):
        try:
            self.db.iniciar_conn()
            query = '''
                SELECT ga.id, p.nome AS professor, d.nome AS disciplina, ga.data, d.id
                FROM salas_aulas ga
                JOIN professor p ON ga.id_professor = p.id
                JOIN disciplina d ON ga.id_disciplina = d.id
                WHERE ga.id = ?
            '''
            self.db.executar_sql(query, (id_sala,))
            salas_do_aluno = self.db.fetchall()
            return salas_do_aluno
        except sqlite3.Error as e:
            print(f"Erro ao consultar salas de aula por aluno: {e}")
        finally:
            self.db.fechar_conn()

    def consultar_salas_de_aulas(self):
        try:
            self.db.iniciar_conn()
            self.db.executar_sql("""
            SELECT ga.id, p.nome, d.nome, ga.data
            FROM salas_aulas ga
            JOIN professor p ON ga.id_professor = p.id
            JOIN disciplina d ON ga.id_disciplina = d.id
            """)
            return self.db.fetchall()
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a busca: {e.args[0]}")
        finally:
            self.db.fechar_conn()

    def atualizar_sala_de_aula(self, id_disciplina, id_professor, data, id_sala_de_aula):
        try:
            self.db.iniciar_conn()
            self.db.executar_sql("UPDATE salas_aulas SET id_disciplina = ?, "
                                 "id_professor = ?, data = ? WHERE id = ?",
                                 (id_disciplina, id_professor, data, id_sala_de_aula))
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a atualização: {e.args[0]}")
        finally:
            self.db.fechar_conn()

    def excluir_sala_de_aula(self, id_sala_de_aula):
        try:
            self.db.iniciar_conn()
            query = "DELETE FROM salas_aulas WHERE id = ?"
            self.db.executar_sql(query, (id_sala_de_aula,))
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a remoção: {e.args[0]}")
        finally:
            self.db.fechar_conn()

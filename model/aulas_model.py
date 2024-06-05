import sqlite3
from database.conexao import Conexao


class AulasModel:
    def __init__(self):
        self.db = Conexao()

    def adicionar_aula(self, id_professor, id_disciplina, horario):
        try:
            self.db.iniciar_conn()
            query = "INSERT INTO grade_aulas (id_professor, id_disciplina, horario) VALUES (?, ?, ?)"
            self.db.executar_sql(query, (id_professor, id_disciplina, horario))
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a inserção: {e.args[0]}")
        finally:
            self.db.fechar_conn()

    def atualizar_aula(self, id_professor, id_disciplina, horario, id_aula):
        try:
            self.db.iniciar_conn()
            query = "UPDATE grade_aulas SET id_professor = ?, id_disciplina = ?, horario = ? WHERE id = ?"
            self.db.executar_sql(query, (id_professor, id_disciplina, horario, id_aula))
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a atualização: {e.args[0]}")
        finally:
            self.db.fechar_conn()

    def consultar_aula_id(self, id_aula):
        try:
            self.db.iniciar_conn()
            query = "SELECT * FROM grade_aulas WHERE id = ?"
            self.db.executar_sql(query, (id_aula,))
            return self.db.fetchall()
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a busca por id: {e.args[0]}")
        finally:
            self.db.fechar_conn()

    def excluir_aula(self, id_aula):
        try:
            self.db.iniciar_conn()
            query = "DELETE FROM grade_aulas WHERE id = ?"
            self.db.executar_sql(query, (id_aula,))
        except sqlite3.Error as e:
            print(f"Erro ao excluir aula: {e}")
        finally:
            self.db.fechar_conn()

    def consultar_aulas(self):
        try:
            self.db.iniciar_conn()
            query = "SELECT * FROM grade_aulas"
            self.db.executar_sql(query)
            return self.db.fetchall()
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a busca: {e.args[0]}")
        finally:
            self.db.fechar_conn()

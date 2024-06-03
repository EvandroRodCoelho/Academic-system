import sqlite3
from database.conexao import Conexao


class ProfessorModel:
    def __init__(self):
        self.db = Conexao()

    def adicionar_professor(self, nome):
        try:
            self.db.iniciar_conn()
            self.db.executar_sql("INSERT INTO professor (nome) VALUES (?)", (nome,))
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a inserção: {e.args[0]}")
        finally:
            self.db.fechar_conn()

    def atualizar_professor(self, nome, id_professor):
        try:
            self.db.iniciar_conn()
            self.db.executar_sql("UPDATE professor SET nome = ? WHERE id = ?", (nome, id_professor))
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a atualização: {e.args[0]}")
        finally:
            self.db.fechar_conn()

    def consultar_professor_id(self, id_professor):
        try:
            self.db.iniciar_conn()
            self.db.executar_sql("SELECT * FROM professor WHERE id = ?", (id_professor,))
            return self.db.fetchall()
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a busca por id: {e.args[0]}")
        finally:
            self.db.fechar_conn()

    def excluir_professor(self, id_professor):
        try:
            self.db.iniciar_conn()
            query = "DELETE FROM professor WHERE id = ?"
            self.db.executar_sql(query, (id_professor,))
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a remoção: {e.args[0]}")
        finally:
            self.db.fechar_conn()

    def consultar_professores(self):
        try:
            self.db.iniciar_conn()
            self.db.executar_sql("SELECT * FROM professor")
            return self.db.fetchall()
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a busca: {e.args[0]}")
        finally:
            self.db.fechar_conn()

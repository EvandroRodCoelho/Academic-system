import sqlite3
from database.conexao import Conexao


class AlunoModel:
    def __init__(self):
        self.db = Conexao()

    def adicionar_aluno(self, nome, endereco):
        try:
            self.db.iniciar_conn()
            self.db.executar_sql("INSERT INTO aluno (nome, endereco) VALUES (?, ?)", (nome, endereco))
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a inserção: {e.args[0]}")
        finally:
            self.db.fechar_conn()

    def atualizar_aluno(self, nome, endereco, id_aluno):
        try:
            self.db.iniciar_conn()
            self.db.executar_sql("UPDATE aluno SET nome = ?, endereco = ? WHERE id = ?", (nome, endereco, id_aluno))
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a atualização: {e.args[0]}")
        finally:
            self.db.fechar_conn()

    def consultar_aluno_id(self, id_aluno):
        try:
            self.db.iniciar_conn()
            self.db.executar_sql("SELECT * FROM aluno WHERE id = ?", (id_aluno,))
            return self.db.fetchall()
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a busca por id: {e.args[0]}")
        finally:
            self.db.fechar_conn()

    def consultar_alunos(self):
        try:
            self.db.iniciar_conn()
            self.db.executar_sql("SELECT * FROM aluno")
            return self.db.fetchall()
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a busca: {e.args[0]}")
        finally:
            self.db.fechar_conn()

    def remover_aluno(self, id_aluno):
        try:
            self.db.iniciar_conn()
            self.db.executar_sql("DELETE FROM aluno WHERE id = ?", (id_aluno,))
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a remoção: {e.args[0]}")
        finally:
            self.db.fechar_conn()

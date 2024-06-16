import sqlite3
from database.conexao import Conexao


class DisciplinaModel:
    def __init__(self):
        self.db = Conexao()

    def adicionar_disciplina(self, nome, id_professor, especialidade):
        try:
            self.db.iniciar_conn()
            self.db.executar_sql("INSERT INTO disciplina (nome, id_professor, especialidade) VALUES (?, ?, ?)", (nome, id_professor, especialidade))
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a inserção: {e.args[0]}")
        finally:
            self.db.fechar_conn()

    def atualizar_disciplina(self, id_disciplina, nome, id_professor, especialidade):
        try:
            self.db.iniciar_conn()
            self.db.executar_sql("UPDATE disciplina SET nome = ?, id_professor = ?, especialidade = ? WHERE id = ?", (nome, id_professor, especialidade, id_disciplina))
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a atualização: {e.args[0]}")
        finally:
            self.db.fechar_conn()

    def consultar_disciplina_id(self, id_disciplina):
        try:
            self.db.iniciar_conn()
            self.db.executar_sql("SELECT * FROM disciplina WHERE id = ?", (id_disciplina,))
            return self.db.fetchall()
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a busca por id: {e.args[0]}")
        finally:
            self.db.fechar_conn()

    def excluir_disciplina(self, id_disciplina):
        try:
            self.db.iniciar_conn()
            self.db.executar_sql("DELETE FROM disciplina WHERE id = ?", (id_disciplina,))
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a remoção: {e.args[0]}")
        finally:
            self.db.fechar_conn()

    def consultar_disciplinas(self):
        try:
            self.db.iniciar_conn()
            self.db.executar_sql("""
                SELECT d.id, d.nome, p.nome, d.especialidade 
                FROM disciplina d
                JOIN professor p ON d.id_professor = p.id
            """)
            return self.db.fetchall()
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a busca: {e.args[0]}")
        finally:
            self.db.fechar_conn()

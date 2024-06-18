import sqlite3
from database.conexao import Conexao


class AlunosSalaDeAulaModel:
    def __init__(self):
        self.db = Conexao()

    def adicionar_alunos_sala_de_aula(self, id_sala_de_aula, id_aluno):
        try:
            self.db.iniciar_conn()
            self.db.executar_sql("INSERT INTO alunos_salas_aulas (id_sala_aula, id_aluno) VALUES (?, ?)",
                                 (id_sala_de_aula, id_aluno))
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a inserção: {e.args[0]}")
        finally:
            self.db.fechar_conn()

    def consultar_alunos_sala_de_aula_id(self, id_aluno_sala_de_aula):
        try:
            self.db.iniciar_conn()
            query = '''
                SELECT a.id, a.id_aluno, a.id_sala_aula, b.nome as nome_aluno, 
                e.nome || ' - ' || d.nome || ' - ' || c.data as nome_sala_de_aula
                FROM alunos_salas_aulas a
                JOIN aluno b ON a.id_aluno = b.id
                JOIN salas_aulas c ON a.id_sala_aula = b.id 
                JOIN disciplina d ON c.id_disciplina = d.id
                JOIN professor e ON c.id_professor = e.id
                WHERE a.id = ?
            '''
            self.db.executar_sql(query, (id_aluno_sala_de_aula,))
            return self.db.fetchall()
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a busca por id: {e}")
        finally:
            self.db.fechar_conn()

    def consultar_alunos_sala_de_aula(self):
        try:
            self.db.iniciar_conn()
            query = '''
                SELECT a.id, b.nome as nome_aluno, e.nome || ' - ' || d.nome || ' - ' || c.data as nome_sala_de_aula
                FROM alunos_salas_aulas a
                JOIN aluno b ON a.id_aluno = b.id
                JOIN salas_aulas c ON a.id_sala_aula = b.id 
                JOIN disciplina d ON c.id_disciplina = d.id
                JOIN professor e ON c.id_professor = e.id
            '''
            self.db.executar_sql(query)
            return self.db.fetchall()
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a busca: {e.args[0]}")
        finally:
            self.db.fechar_conn()

    def excluir_alunos_sala_de_aula(self, id_aluno_sala_de_aula):
        try:
            self.db.iniciar_conn()
            query = "DELETE FROM alunos_salas_aulas WHERE id = ?"
            self.db.executar_sql(query, (id_aluno_sala_de_aula,))
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a remoção: {e.args[0]}")
        finally:
            self.db.fechar_conn()

    def consultar_salas_de_aulas(self):
        try:
            self.db.iniciar_conn()
            self.db.executar_sql("""
            SELECT ga.id, p.nome || ' - ' || d.nome || ' - ' || ga.data as nome_sala_de_aula
            FROM salas_aulas ga
            JOIN professor p ON ga.id_professor = p.id
            JOIN disciplina d ON ga.id_disciplina = d.id
            """)
            return self.db.fetchall()
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a busca: {e.args[0]}")
        finally:
            self.db.fechar_conn()

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

    def obter_dados_historico(self, aluno_id, id_disciplina):
        try:
            self.db.iniciar_conn()
            query = '''
                SELECT notas, faltas 
                FROM historico_alunos
                WHERE id_aluno = ? AND id_disciplina = ?
            '''
            self.db.executar_sql(query, (aluno_id, id_disciplina))
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
            self.db.executar_sql(query, (id_aluno, disciplina_id,))
            return self.db.fetchall()
        except Exception as e:
            print(f"Erro ao atribuir falta: {str(e)}")
        finally:
            self.db.fechar_conn()

    def atribuir_nota(self, id_aluno, disciplina_id, nota):
        try:
            self.db.iniciar_conn()
            query = '''
                UPDATE historico_alunos 
                SET notas = ?
                WHERE id_aluno = ? AND id_disciplina = ?
            '''
            self.db.executar_sql(query, (nota, id_aluno, disciplina_id,))

        except Exception as e:
            print(f"Erro ao atribuir nota: {str(e)}")
        finally:
            self.db.fechar_conn()

    def atribuir_falta_especifico(self, id_aluno, id_disciplina, faltas):
        try:
            self.db.iniciar_conn()
            query = '''
            UPDATE historico_alunos 
            SET faltas =  ? 
            WHERE id_aluno = ? AND id_disciplina = ?'''
            self.db.executar_sql(query, (faltas, id_aluno, id_disciplina))
        except Exception as e:
            print(f"Erro ao atribuir falta: {str(e)}")
        finally:
            self.db.fechar_conn()

    def atribuir_nota_e_falta(self, id_aluno, id_disciplina, nota, faltas):
        print(f"id_aluno:{id_aluno} id_disciplina:{id_disciplina} nota:{nota} faltas:{faltas} ")
        try:
            self.db.iniciar_conn()
            query = '''
                UPDATE historico_alunos 
                SET notas = ?,
                    faltas = ?
                WHERE id_aluno = ? AND id_disciplina = ?
            '''
            self.db.executar_sql(query, (nota, faltas, id_aluno, id_disciplina,))
        except Exception as e:
            print(f"Erro ao atribuir nota e faltas: {str(e)}")
        finally:
            self.db.fechar_conn()

    def adicionar_historico_alunos(self, id_aluno, id_disciplina, notas, faltas):
        try:
            self.db.iniciar_conn()
            query = '''
                INSERT INTO historico_alunos (id_aluno, id_disciplina, notas, faltas)
                VALUES (?, ?, ?, ?)
            '''
            self.db.executar_sql(query, (id_aluno, id_disciplina, notas, faltas))
        except sqlite3.Error as e:
            print(f"Erro ao adicionar histórico: {e}")
        finally:
            self.db.fechar_conn()

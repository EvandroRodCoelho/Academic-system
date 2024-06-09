import sqlite3
from database.conexao import Conexao


class HorariosModel:
    def __init__(self):
        self.db = Conexao()
    def consultar_horarios(self):
        try:
            self.db.iniciar_conn()
            self.db.executar_sql('''
                    SELECT 
                        grade_aulas.id,
                        professor.nome AS professor,
                        disciplina.nome AS disciplina,
                        grade_aulas.horario
                    FROM 
                        grade_aulas
                    JOIN 
                        professor ON grade_aulas.id_professor = professor.id
                    JOIN 
                        disciplina ON grade_aulas.id_disciplina = disciplina.id
                    ''') 
            return self.db.fetchall()
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a busca: {e.args[0]}")
        finally:
            self.db.fechar_conn()
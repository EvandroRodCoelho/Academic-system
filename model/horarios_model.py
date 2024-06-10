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
                        ga.id,
                        professor.nome AS professor,
                        disciplina.nome AS disciplina,
                        ga.horario
                    FROM 
                        grade_aulas ga
                    JOIN 
                        professor ON ga.id_professor = professor.id
                    JOIN 
                        disciplina ON ga.id_disciplina = disciplina.id
                    ORDER BY ga.horario
                    ''') 
            return self.db.fetchall()
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a busca: {e.args[0]}")
        finally:
            self.db.fechar_conn()
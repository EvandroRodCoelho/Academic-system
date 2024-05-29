import sqlite3
from database.conexao import Conexao
def adicionar_aluno(nome, endereco):
    # Inicializa a conexão com o banco de dados
    conexao = Conexao()
    conexao.iniciar_conn()

    try:
        query = "INSERT INTO aluno (nome, endereco) VALUES (?, ?)"
        conexao.executar_sql(query, (nome, endereco))
        conexao.conn.commit()
        print("Aluno adicionado com sucesso!")
    finally:
        conexao.fechar_conn()

def buscar_alunos():
    conexao = Conexao()
    conexao.iniciar_conn()
    try:
        query = "SELECT id, nome, endereco FROM aluno"
        conexao.executar_sql(query)
        
        alunos = conexao.fetchall()
        return alunos
    except Exception as e:
        print("Erro ao buscar alunos:", e)
        return None
    finally:
        conexao.fechar_conn()




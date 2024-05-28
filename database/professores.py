import sqlite3
from database.conexao import Conexao
def adicionar(nome):
    # Inicializa a conexão com o banco de dados
    conexao = Conexao()
    conexao.iniciar_conn()

    try:
        query = "INSERT INTO professor (nome) VALUES (?)"
        conexao.executar_sql(query, (nome,))
        conexao.conn.commit()
        print("Aluno adicionado com sucesso!")
    finally:
        conexao.fechar_conn()

def buscar_professores():
    # Inicializa a conexão com o banco de dados
    conexao = Conexao()
    conexao.iniciar_conn()

    try:
        # Define a consulta SQL para buscar todos os alunos
        query = "SELECT id, nome FROM professor"
        
        # Executa a consulta SQL
        conexao.executar_sql(query)
        
        # Recupera todos os alunos
        alunos = conexao.fetchall()
        
        return alunos
    
    except Exception as e:
        print("Erro ao buscar alunos:", e)
        return None
    
    finally:
        # Fecha a conexão com o banco de dados
        conexao.fechar_conn()


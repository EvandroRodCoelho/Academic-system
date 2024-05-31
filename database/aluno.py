import sqlite3
from database.conexao import Conexao
def adicionar_aluno(nome, endereco):
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
def excluir(id):
    conexao = Conexao()
    conexao.iniciar_conn()
    try:
        query = "DELETE FROM aluno WHERE id = ?"
        conexao.executar_sql(query, (id,))
        conexao.conn.commit()
        print("Aluno excluído com sucesso!")
    except Exception as e:
        print("Erro ao excluir aluno:", e)
    finally:
        conexao.fechar_conn()

def editar_aluno(id, nome, endereco):
    conexao = Conexao()
    conexao.iniciar_conn()

    try:
        query = "UPDATE aluno SET nome =?, endereco =? WHERE id =?"
        conexao.executar_sql(query, (nome, endereco, id))
        conexao.conn.commit()
        print("Aluno editado com sucesso!")
    except Exception as e:
        print("Erro ao editar aluno:", e)
    finally:
        conexao.fechar_conn()


from database.conexao import Conexao
def adicionar(nome):
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
    conexao = Conexao()
    conexao.iniciar_conn()
    try:
        query = "SELECT id, nome FROM professor"
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
        query = "DELETE FROM professor WHERE id = ?"
        conexao.executar_sql(query, (id,))
        conexao.conn.commit()
        print("Professor excluído com sucesso!")
    except Exception as e:
        print("Erro ao excluir aluno:", e)
    finally:
        conexao.fechar_conn()

def editar_professor(id, nome):
    conexao = Conexao()
    conexao.iniciar_conn()
    try:
        query = "UPDATE professor SET nome =? WHERE id =?"
        conexao.executar_sql(query, (nome, id))
        conexao.conn.commit()
        print("Professor editado com sucesso!")
    except Exception as e:
        print("Erro ao editar aluno:", e)
    finally:
        conexao.fechar_conn()


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


import sqlite3

conn = sqlite3.connect('db.db')
db = conn.cursor()

def iniciar_conn():
    db.execute("""
        CREATE TABLE aluno (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100) NOT NULL DEFAULT '',
            endereco VARCHAR(100) NOT NULL DEFAULT '',
            criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
def fechar_conn():
    db.close()
    
iniciar_conn()
    

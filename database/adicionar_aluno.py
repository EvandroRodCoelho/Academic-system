import sqlite3
def adicionar_aluno(nome, endereco):
    conn = sqlite3.connect('db.db')
    db = conn.cursor()
    db.execute("INSERT INTO aluno (nome, endereco) VALUES (?, ?)", (nome, endereco))
    conn.commit()
    db.close()
    conn.close()
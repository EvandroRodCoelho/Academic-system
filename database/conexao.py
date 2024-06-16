import os
import sqlite3


class Conexao:
    def __init__(self):
        self.conn = None
        self.db = None

        self.iniciar_conn()
        self.cadastrar_tabelas(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tabelas.sql'))

    def cadastrar_tabelas(self, arquivo_sql):
        try:
            with open(arquivo_sql, 'r') as f:
                sql = f.read()
            self.conn.executescript(sql)
        except Exception as e:
            print(f"Erro ao cadastrar tabelas: {e}")

    def iniciar_conn(self):
        self.conn = sqlite3.connect('./database/sqlite_database.db')
        self.db = self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def fechar_conn(self):
        if self.db:
            self.db.close()
            self.db = None
        if self.conn:
            self.conn.commit()
            self.conn.close()
            self.conn = None

    def executar_sql(self, query, params=()):
        self.db.execute(query, params)

    def fetchall(self):
        return self.db.fetchall()

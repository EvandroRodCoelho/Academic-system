import sqlite3


class Conexao:
    def __init__(self):
        self.conn = None
        self.db = None

    def cadastrar_tabelas(self, arquivo_sql):
        with open(arquivo_sql, 'r') as f:
            sql = f.read()
        self.db.executescript(sql)

    def iniciar_conn(self):
        self.conn = sqlite3.connect('sqlite_database.db')
        self.db = self.conn.cursor()

    def fechar_conn(self):
        if self.db:
            self.conn.commit()
            self.conn.close()
            self.conn = None
            self.db.close()

    def executar_sql(self, query, params=()):
        self.db.execute(query, params)

    def fetchall(self):
        return self.db.fetchall()

    def __del__(self):
        self.fechar_conn()

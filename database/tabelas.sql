CREATE TABLE IF NOT EXISTS aluno (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL DEFAULT '',
    endereco VARCHAR(100) NOT NULL DEFAULT '',
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS professor (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL DEFAULT '',
    criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS disciplina (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL DEFAULT '',
    id_professor INTEGER NOT NULL,
    especialidade VARCHAR(100) NOT NULL DEFAULT '',
    FOREIGN KEY(id_professor) REFERENCES professor(id)
);

CREATE TABLE IF NOT EXISTS grade_aulas (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    id_professor INTEGER NOT NULL,
    id_disciplina INTEGER NOT NULL,
    horario DATETIME,
    FOREIGN KEY(id_professor) REFERENCES professor(id),
    FOREIGN KEY(id_disciplina) REFERENCES disciplina(id)
);

CREATE TABLE IF NOT EXISTS salas_aulas (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    id_aula INTEGER NOT NULL,
    id_aluno INTEGER NOT NULL,
    FOREIGN KEY(id_aluno) REFERENCES aluno(id),
    FOREIGN KEY(id_aula) REFERENCES grade_aulas(id)
);

CREATE TABLE IF NOT EXISTS historico_alunos (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    id_aluno INTEGER NOT NULL,
    id_disciplina INTEGER NOT NULL,
    notas FLOAT,
    faltas INTEGER,
    FOREIGN KEY(id_aluno) REFERENCES aluno(id),
    FOREIGN KEY(id_disciplina) REFERENCES disciplina(id)
);
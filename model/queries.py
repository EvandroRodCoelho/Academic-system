from pyswip import Prolog

prolog = Prolog()

# Definindo as regras Prolog
prolog.assertz("aluno(X) :- estudante(X)")
prolog.assertz("cursando(X, Y) :- aluno(X), disciplina(Y), matriculado(X, Y)")
prolog.assertz("aprovado(X, Y) :- cursando(X, Y), nota(X, Y, Nota), Nota >= 6")
prolog.assertz("calcular_media(X, Media) :- findall(Nota, (cursando(X, Disc), nota(X, Disc, Nota)), Notas), "
               "length(Notas, N), ""sumlist(Notas, Soma), Media is Soma / N")

prolog.assertz("reprovado(X, Y) :- cursando(X, Y), nota(X, Y, Nota), Nota < 6")
prolog.assertz("concluiu(X, Y) :- cursando(X, Y), nota(X, Y, Nota), Nota >= 6")
prolog.assertz("faltas(X, Y, F) :- aluno(X), disciplina(Y), matriculado(X, Y), faltas(X, Y, F)")
prolog.assertz("faltou(X, Y) :- faltas(X, Y, F), F > Limite")

prolog.assertz("cadastrar_aluno(X) :- assertz(aluno(X))")
prolog.assertz("editar_aluno(X, Y) :- retract(aluno(X)), assertz(aluno(Y))")
prolog.assertz("excluir_aluno(X) :- retract(aluno(X))")

prolog.assertz("cadastrar_professor(X) :- assertz(professor(X))")
prolog.assertz("editar_professor(X, Y) :- retract(professor(X)), assertz(professor(Y))")
prolog.assertz("excluir_professor(X) :- retract(professor(X))")

prolog.assertz("cadastrar_disciplina(X) :- assertz(disciplina(X))")
prolog.assertz("editar_disciplina(X, Y) :- retract(disciplina(X)), assertz(disciplina(Y))")
prolog.assertz("excluir_disciplina(X) :- retract(disciplina(X))")

prolog.assertz("adicionar_aluno_disciplina(X, Y) :- assertz(matriculado(X, Y))")
prolog.assertz("remover_aluno_disciplina(X, Y) :- retract(matriculado(X, Y))")

prolog.assertz("cadastrar_sala(X, Y, Z) :- assertz(sala(X, Y, Z))")
prolog.assertz("remover_sala(X) :- retract(sala(X, _, _))")

# Dados Prolog simulados
# prolog.assertz("estudante(joao)")
# prolog.assertz("estudante(maria)")
# prolog.assertz("disciplina(mate)")
# prolog.assertz("disciplina(fisica)")
# prolog.assertz("disciplina(quimica)")
# prolog.assertz("matriculado(joao, mate)")
# prolog.assertz("matriculado(joao, fisica)")
# prolog.assertz("matriculado(maria, quimica)")
# prolog.assertz("nota(joao, mate, 7)")
# prolog.assertz("nota(joao, fisica, 5)")
# prolog.assertz("nota(maria, quimica, 8)")

# def aluno():
#     prolog.assertz("aluno(X) :- estudante(X)")
#     prolog.assertz("cadastrar_aluno(X) :- assertz(aluno(X))")
#     prolog.assertz("editar_aluno(X, Y) :- retract(aluno(X)), assertz(aluno(Y))")
#     prolog.assertz("excluir_aluno(X) :- retract(aluno(X))")



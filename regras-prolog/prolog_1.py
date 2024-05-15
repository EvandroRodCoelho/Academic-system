from pyswip import Prolog
import PySimpleGUI as sG

# Inicializando o interpretador Prolog
prolog = Prolog()

# Definindo as regras Prolog
prolog.assertz("aluno(X) :- estudante(X).")
prolog.assertz("cursando(X, Y) :- aluno(X), disciplina(Y), matriculado(X, Y).")
prolog.assertz("aprovado(X, Y) :- cursando(X, Y), nota(X, Y, Nota), Nota >= 6.")
prolog.assertz("calcular_media(X, Media) :- findall(Nota, (cursando(X, Disc), nota(X, Disc, Nota)), Notas), length(Notas, N), ""sumlist(Notas, Soma), Media is Soma / N.")

# Dados Prolog simulados
prolog.assertz("estudante(joao).")
prolog.assertz("estudante(maria).")
prolog.assertz("disciplina(mate).")
prolog.assertz("disciplina(fisica).")
prolog.assertz("disciplina(quimica).")
prolog.assertz("matriculado(joao, mate).")
prolog.assertz("matriculado(joao, fisica).")
prolog.assertz("matriculado(maria, quimica).")
prolog.assertz("nota(joao, mate, 7).")
prolog.assertz("nota(joao, fisica, 5).")
prolog.assertz("nota(maria, quimica, 8).")

layout = [
    [sG.Text("Consultar se um aluno está cursando uma disciplina:")],
    [sG.Text("Aluno:"), sG.InputText(key="aluno")],
    [sG.Text("Disciplina:"), sG.InputText(key="disciplina")],
    [sG.Button("Consultar")],
    [sG.Text("", size=(30, 1), key="consulta_resultado")],
    [sG.Text("Calcular média de um aluno:")],
    [sG.Text("Aluno:"), sG.InputText(key="aluno_media")],
    [sG.Button("Calcular")],
    [sG.Text("", size=(30, 1), key="calculo_resultado")],
]

window = sG.Window("Consulta Prolog", layout)

while True:
    event, values = window.read()
    if event == sG.WINDOW_CLOSED:
        break
    elif event == "Consultar":
        aluno_consulta = values["aluno"]
        disciplina_consulta = values["disciplina"]
        if list(prolog.query(f"cursando({aluno_consulta}, {disciplina_consulta})")):
            window["consulta_resultado"].update(f"{aluno_consulta} está cursando {disciplina_consulta}.")
        else:
            window["consulta_resultado"].update(f"{aluno_consulta} não está cursando {disciplina_consulta}.")
    elif event == "Calcular":
        aluno_calculo = values["aluno_media"]
        media = list(prolog.query(f"calcular_media({aluno_calculo}, Media)"))[0]["Media"]
        window["calculo_resultado"].update(f"A média de {aluno_calculo} é {media:.2f}.")

window.close()

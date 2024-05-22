import PySimpleGUI as sG



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

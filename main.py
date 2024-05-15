import PySimpleGUI as sG


# Lógica de Prolog
def aluno(x):
    return x in estudante


def cursando(x, y):
    return aluno(x) and y in disciplina and (x, y) in matriculado


def aprovado(x, y):
    return cursando(x, y) and (x, y) in nota and nota[(x, y)] >= 6


def calcular_media(x):
    notas_aluno = [nota[(x, d)] for d in disciplina if (x, d) in nota]
    if notas_aluno:
        return sum(notas_aluno) / len(notas_aluno)
    else:
        return 0


# Dados de Prolog simulados
estudante = {"Joao", "Maria", "Pedro"}
disciplina = {"Matemática", "Física", "Química"}
matriculado = {("Joao", "Matemática"), ("Joao", "Física"), ("Maria", "Química")}
nota = {("Joao", "Matemática"): 7, ("Joao", "Física"): 5, ("Maria", "Química"): 8}

# Interface gráfica
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
        if cursando(aluno_consulta, disciplina_consulta):
            window["consulta_resultado"].update(f"{aluno_consulta} está cursando {disciplina_consulta}.")
        else:
            window["consulta_resultado"].update(f"{aluno_consulta} não está cursando {disciplina_consulta}.")
    elif event == "Calcular":
        aluno_calculo = values["aluno_media"]
        media = calcular_media(aluno_calculo)
        window["calculo_resultado"].update(f"A média de {aluno_calculo} é {media:.2f}.")

window.close()

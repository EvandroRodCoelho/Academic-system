from database.aluno import buscar_alunos
from views.aluno.visualizar_aluno import tela_visualizar_alunos
import PySimpleGUI as sg

def visualizar_alunos_controller():
    alunos = buscar_alunos()
    window = tela_visualizar_alunos(alunos)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Fechar':
            break

    window.close()

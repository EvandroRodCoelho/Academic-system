from database.aluno import adicionar_aluno
from views.aluno.adicionar_aluno import tela_adicionar_aluno
import PySimpleGUI as sg
    
def adicionar_aluno_controller():
    window = tela_adicionar_aluno()

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break

        if event == 'Cadastrar':
            nome = values['nome']
            endereco = values['endereco']
            if nome and endereco:
                 if len(nome) > 100 or len(endereco) > 100:
                  sg.popup('Os campos tem uma tamanho máximo de 100 caracteres')
                 else:
                    adicionar_aluno(nome, endereco)
                    sg.popup('Cadastro realizado com sucesso!', f'Nome: {nome}\nEndereço: {endereco}')
            else:
                sg.popup('Por favor, preencha todos os campos.')
    window.close()



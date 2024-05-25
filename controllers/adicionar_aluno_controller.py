from database.adicionar_aluno import adicionar_aluno
from view.adicionar_aluno import tela_adicionar_aluno
import PySimpleGUI as sg
    
def logica_cadastro():
    window = tela_adicionar_aluno()

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Cancelar':
            break

        if event == 'Cadastrar':
            nome = values['nome']
            endereco = values['endereco']
            if nome and endereco:
                 if len(nome) > 3 or len(endereco) > 3:
                  sg.popup('Os campos tem uma tamanho máximo de 100 caracteres')
                 else:
                    adicionar_aluno(nome, endereco)
                    sg.popup('Cadastro realizado com sucesso!', f'Nome: {nome}\nEndereço: {endereco}')
            else:
                sg.popup('Por favor, preencha todos os campos.')
    window.close()



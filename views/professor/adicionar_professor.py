import PySimpleGUI as sg
class TelaAdicionarProfessor: 
   def __init__(self):
     self.layout = [
                [sg.Text('Nome:', font=("Helvetica",14))],
                [sg.InputText(key='nome')],
                [sg.Text('Endereço:', font=("Helvetica",14))],
                [sg.InputText(key='endereco',font=("Helvetica",14))],
                [sg.Button('Cadastrar',font=("Helvetica",14)), sg.Button('Cancelar',font=("Helvetica",14))]
     ]
     self.window = sg.Window('Cadastro de Aluno', self.layout, finalize=True)
    
   def mostrar(self):
        return self.window.read()

   def fechar(self):
        self.window.close()
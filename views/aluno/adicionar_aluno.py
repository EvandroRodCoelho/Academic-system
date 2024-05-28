import PySimpleGUI as sg
class TelaAdicionarAluno: 
   def __init__(self, aluno=None):
     self.layout = [
                [sg.Text('Nome:', font=("Helvetica",14))],
                [sg.InputText(key='nome', default_text=self.aluno[1] if self.aluno else '')],
                [sg.Text('Endereço:', font=("Helvetica",14))],
                [sg.InputText(key='endereco',default_text=self.aluno[2] if self.aluno else '',font=("Helvetica",14))],
                [sg.Button('Cadastrar',font=("Helvetica",14)), sg.Button('Cancelar',font=("Helvetica",14))]
     ]
     self.window = sg.Window('Cadastro de Aluno', self.layout, finalize=True)
    
   def mostrar(self):
        return self.window.read()

   def fechar(self):
        self.window.close()
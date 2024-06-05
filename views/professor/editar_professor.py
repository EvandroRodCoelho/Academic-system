import PySimpleGUI as sg
class TelaEditarProfessor:
   def __init__(self, professor):
     self.professor = professor
     self.layout = [
                [sg.Text('Nome:', font=("Helvetica",14))],
                [sg.InputText(default_text=professor['nome'], key='nome')],
                [sg.Button('Salvar',font=("Helvetica",14)), sg.Button('Cancelar',font=("Helvetica",14), key="cancelar")]
     ]
     self.window = sg.Window('Editar Aluno', self.layout, finalize=True)
    
   def mostrar(self):
        return self.window.read()

   def fechar(self):
        self.window.close()
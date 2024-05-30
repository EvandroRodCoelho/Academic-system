class NavegacaoService:
    def navegar_para_home(self):
        from controllers.home_controller import HomeController
        home_controller = HomeController()
        home_controller.mostrar_tela()

    def navegar_para_alunos(self):
        from controllers.aluno.aluno_controller import AlunoController
        aluno_controller = AlunoController()
        aluno_controller.mostrar_tela()


    def navegar_para_adicionar_alunos(self):
        from controllers.aluno.adicionar_aluno_controller import AdicionarAlunoController
        adicionarAlunoController = AdicionarAlunoController()
        adicionarAlunoController.mostrar_tela() 
    def navegar_para_editar_alunos(self, aluno):
        from controllers.aluno.editar_aluno_controller import EditarAlunoController
        adicionarAlunoController = EditarAlunoController(aluno)
        adicionarAlunoController.mostrar_tela()
   
    def navegar_para_adicionar_professor(self):
        from controllers.professor.adicionar_professor import AdicionarProfessorController
        adicionarAlunoController = AdicionarProfessorController()
        adicionarAlunoController.mostrar_tela()

    def navegar_para_professores(self):
        from controllers.professor.professor_controller import ProfessorController
        professorController = ProfessorController()
        professorController.mostrar_tela()

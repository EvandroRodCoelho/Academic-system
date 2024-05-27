class NavegacaoService:

    def navegar_para_home():
        from controllers.home_controller import HomeController
        home_controller = HomeController()
        home_controller.mostrar_tela()

    def navegar_para_alunos(self):
        from controllers.aluno.aluno_controller import AlunoController
        aluno_controller = AlunoController()
        aluno_controller.mostrar_tela()

    def navegar_para_visualizar_alunos(self):
        from controllers.aluno.visualizar_alunos_controller import VisualizarAlunoController
        visualizarAlunoController = VisualizarAlunoController()
        visualizarAlunoController.mostrar_tela()
    def navegar_para_adicionar_alunos(self):
        from controllers.aluno.adicionar_aluno_controller import AdicionarAlunoController
        adicionarAlunoController = AdicionarAlunoController()
        adicionarAlunoController.mostrar_tela()

    def navegar_para_professores():
        # Lógica de negócios para navegar para a tela de Professores
        pass
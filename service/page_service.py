

class NavegacaoService:
    @staticmethod
    def navegar_para_home():
        from controllers.home_controller import HomeController
        home_controller = HomeController()
        home_controller.mostrar_tela()

    @staticmethod
    def navegar_para_alunos():
        from controllers.aluno.aluno_controller import AlunoController
        aluno_controller = AlunoController()
        aluno_controller.mostrar_tela()

    @staticmethod
    def navegar_para_adicionar_alunos():
        from controllers.aluno.adicionar_aluno_controller import AdicionarAlunoController
        adicionarAlunoController = AdicionarAlunoController()
        adicionarAlunoController.mostrar_tela()

    @staticmethod
    def navegar_para_editar_alunos(aluno):
        from controllers.aluno.editar_aluno_controller import EditarAlunoController
        adicionarAlunoController = EditarAlunoController(aluno)
        adicionarAlunoController.mostrar_tela()

    @staticmethod
    def navegar_para_editar_professor(professor):
        from controllers.professor.editar_professor_controller import EditarProfessorController
        editarProfessorController = EditarProfessorController(professor)
        editarProfessorController.mostrar_tela()

    @staticmethod
    def navegar_para_adicionar_professor():
        from controllers.professor.adicionar_professor import AdicionarProfessorController
        adicionarAlunoController = AdicionarProfessorController()
        adicionarAlunoController.mostrar_tela()

    @staticmethod
    def navegar_para_professores():
        from controllers.professor.professor_controller import ProfessorController
        professorController = ProfessorController()
        professorController.mostrar_tela()

    @staticmethod
    def navegar_para_disciplina():
        from controllers.disciplina.disciplina_controller import DisciplinaController
        disciplinaController = DisciplinaController()
        disciplinaController.mostrar_tela()

    @staticmethod
    def navegar_para_adicionar_disciplina():
        from controllers.disciplina.adicionar_disciplina_controller import AdicionarDisciplinaController
        adicionarDisciplinaController = AdicionarDisciplinaController()
        adicionarDisciplinaController.mostrar_tela()

    @staticmethod
    def navegar_para_editar_disciplina(disciplina):
        from controllers.disciplina.editar_disciplina_controller import EditarDisciplinaController
        editarDisciplinaController = EditarDisciplinaController(disciplina)
        editarDisciplinaController.mostrar_tela()

    @staticmethod
    def navegar_para_salas_de_aula():
        from controllers.sala_de_aula.sala_de_aula_controller import SalaDeAulaController
        salasDeAulaController = SalaDeAulaController()
        salasDeAulaController.mostrar_tela()

    # @staticmethod
    # def navegar_para_salas_de_aula_alunos(aula):
    #     from controllers.sala_de_aula.sala_de_aula_por_id_controller import SalaDeAulaPorIdController
    #     salaDeAulaPorIdController = SalaDeAulaPorIdController(aula)
    #     salaDeAulaPorIdController.mostrar_tela()

    @staticmethod
    def navegar_para_adicionar_sala_de_aula():
        from controllers.sala_de_aula.adicionar_sala_de_aula_controller import AdicionarSalaDeAulaController
        adicionarSalaDeAulaController = AdicionarSalaDeAulaController()
        adicionarSalaDeAulaController.mostrar_tela()

    @staticmethod
    def navegar_para_editar_sala_de_aula(sala_de_aula):
        from controllers.sala_de_aula.editar_sala_de_aula_controller import EditarSalaDeAulaController
        editarSalaDeAulaController = EditarSalaDeAulaController(sala_de_aula)
        editarSalaDeAulaController.mostrar_tela()
        
    @staticmethod
    def navegar_para_historico():
        from controllers.historico.historico_controller import HistoricoController
        historico_controller = HistoricoController()
        historico_controller.mostrar_tela()

    @staticmethod
    def navegar_para_atribuir_nota_falta(id_aluno, id_sala):
        from controllers.historico.atribuirNotaFaltaController import AtribuirNotaFaltaController
        atribuirNotaFaltaController = AtribuirNotaFaltaController(id_aluno, id_sala)
        atribuirNotaFaltaController.mostrar_tela()

    @staticmethod
    def navegar_para_alunos_sala_de_aula():
        from controllers.alunos_sala_de_aula.alunos_sala_de_aula_controller import AlunosSalaDeAulaController
        alunosSalaDeAulaController = AlunosSalaDeAulaController()
        alunosSalaDeAulaController.mostrar_tela()

    @staticmethod
    def navegar_para_adicionar_alunos_sala_de_aula():
        from controllers.alunos_sala_de_aula.adicionar_alunos_sala_de_aula_controller import \
            AdicionarAlunosSalaDeAulaController
        adicionarAlunosSalaDeAulaController = AdicionarAlunosSalaDeAulaController()
        adicionarAlunosSalaDeAulaController.mostrar_tela()

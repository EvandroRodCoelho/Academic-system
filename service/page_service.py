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
    def navegar_para_editar_professor(self, professor):
        from controllers.professor.editar_professor_controller import EditarProfessorController
        editarProfessorController = EditarProfessorController(professor)
        editarProfessorController.mostrar_tela()
    def navegar_para_adicionar_professor(self):
        from controllers.professor.adicionar_professor import AdicionarProfessorController
        adicionarAlunoController = AdicionarProfessorController()
        adicionarAlunoController.mostrar_tela()

    def navegar_para_professores(self):
        from controllers.professor.professor_controller import ProfessorController
        professorController = ProfessorController()
        professorController.mostrar_tela()


    def navegar_para_disciplina(self):
        from controllers.disciplina.disciplina_controller import DisciplinaController
        disciplinaController = DisciplinaController()
        disciplinaController.mostrar_tela()
    def navegar_para_adicionar_disciplina(self):
        from controllers.disciplina.adicionar_disciplina_controller import AdicionarDisciplinaController
        adicionarDisciplinaController = AdicionarDisciplinaController()
        adicionarDisciplinaController.mostrar_tela()
    def navegar_para_editar_disciplina(self,disciplina): 
        from controllers.disciplina.editar_disciplina_controller import EditarDisciplinaController
        editarDisciplinaController = EditarDisciplinaController(disciplina)
        editarDisciplinaController.mostrar_tela()

    def navegar_para_turmas(self):
        from controllers.turma.turma_controller import TurmasController
        turmasController = TurmasController()
        turmasController.mostrar_tela()

    # def navegar_para_adicionar_turma(self):
    #     from controllers.turmas.adicionar_turma_controller import AdicionarTurmaController
    #     adicionarTurmaController = AdicionarTurmaController()
    #     adicionarTurmaController.mostrar_tela()

    # def navegar_para_editar_turma(self, turma):
    #     from controllers.turmas.editar_turma_controller import EditarTurmaController
    #     editarTurmaController = EditarTurmaController(turma)
    #     editarTurmaController.mostrar_tela()

    # # Funções de navegação para Sala de Aula
    def navegar_para_salas_de_aula(self):
        from controllers.sala_de_aula.sala_de_aula_controller import SalaDeAulaController
        salasDeAulaController = SalaDeAulaController()
        salasDeAulaController.mostrar_tela()

    def navegar_para_adicionar_sala_de_aula(self):
        from controllers.sala_de_aula import AdicionarSalaDeAulaController
        adicionarSalaDeAulaController = AdicionarSalaDeAulaController()
        adicionarSalaDeAulaController.mostrar_tela()

    # def navegar_para_editar_sala_de_aula(self, sala_de_aula):
    #     from controllers.sala_de_aula.editar_sala_de_aula_controller import EditarSalaDeAulaController
    #     editarSalaDeAulaController = EditarSalaDeAulaController(sala_de_aula)
    #     editarSalaDeAulaController.mostrar_tela()

    # # Funções de navegação para Aulas
    def navegar_para_aulas(self):
        from controllers.aulas.aulas_controller import AulasController
        aulasController = AulasController()
        aulasController.mostrar_tela()

    def navegar_para_adicionar_aula(self):
        from controllers.aulas.adicionar_aula import AdicionarAulaController
        adicionarAulaController = AdicionarAulaController()
        adicionarAulaController.mostrar_tela()

    # def navegar_para_editar_aula(self, aula):
    #     from controllers.aulas.editar_aula_controller import EditarAulaController
    #     editarAulaController = EditarAulaController(aula)
    #     editarAulaController.mostrar_tela()

    # # Funções de navegação para Horários
    def navegar_para_horarios(self):
        from controllers.horarios.horarios_controller import HorariosController
        horariosController = HorariosController()
        horariosController.mostrar_tela()

    # def navegar_para_adicionar_horario(self):
    #     from controllers.horarios.adicionar_horario_controller import AdicionarHorarioController
    #     adicionarHorarioController = AdicionarHorarioController()
    #     adicionarHorarioController.mostrar_tela()

    # def navegar_para_editar_horario(self, horario):
    #     from controllers.horarios.editar_horario_controller import EditarHorarioController
    #     editarHorarioController = EditarHorarioController(horario)
    #     editarHorarioController.mostrar_tela()
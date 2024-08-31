class EstruturaRepetivel:
    def search_header(tipo_plural: str, ver_detalhes: bool):
        print()
        print(f"-------- {tipo_plural.title()} Cadastrados --------")
        print()
        # if ver_detalhes:
        #     print(f"Digite \"+\" para cadastrar mais {tipo_plural}") 
        print("Digite \"Voltar\" para voltar a página anterior")
        print("Digite \"Sair\" para sair da aplicação")
        print()
        print()

    def print_info_curso(id: int, nome: str, sigla: str):
        print()
        print(f" ID: {id}")
        print(f" Nome: {nome}")
        print(f" Sigla: {sigla}")
        print()
        print("- - - - - - - - - - - - - - - - - - - - -")

    def print_info_turma(id: int, nome: str, curso: str, ano_inicio: int):
        print()
        print(f" ID: {id}")
        print(f" Nome: {nome}")
        print(f" Curso: {curso}")
        print(f" Ano de Início: {ano_inicio}")
        print()
        print("- - - - - - - - - - - - - - - - - - - - -")

    def print_info_professor(id: int, nome: str, cpf: str):
        print()
        print(f" ID: {id}")
        print(f" Nome: {nome}")
        print(f" CPF: {cpf}")
        print()
        print("- - - - - - - - - - - - - - - - - - - - -")

    def print_info_aluno(id: int, nome: str, cpf: str, curso: str, turma: str):
        print()
        print(f" ID: {id}")
        print(f" Nome: {nome}")
        print(f" CPF: {cpf}")
        print(f" Curso: {curso}")
        print(f" Turma: {turma}")
        print()
        print("- - - - - - - - - - - - - - - - - - - - -")
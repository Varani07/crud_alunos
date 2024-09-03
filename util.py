class EstruturaRepetivel:
    def search_header(tipo_plural: str):
        print()
        print(f"-------- {tipo_plural.title()} Cadastrados --------")
        print()
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

    def print_info_professor(id: int, nome: str, cpf: str, data, idade):
        print()
        print(f" ID: {id}")
        print(f" Nome: {nome}")
        print(f" CPF: {cpf}")
        print(f" Data de nascimento: {data}  |  Idade: {idade}")
        print()
        print("- - - - - - - - - - - - - - - - - - - - -")

    def print_info_aluno(id: int, nome: str, cpf: str, data, idade, curso: str, turma: str):
        print()
        print(f" ID: {id}")
        print(f" Nome: {nome}")
        print(f" CPF: {cpf}")
        print(f" Data de nascimento: {data}  |  Idade: {idade}")
        print(f" Curso: {curso}")
        print(f" Turma: {turma}")
        print()
        print("- - - - - - - - - - - - - - - - - - - - -")

    def op_pesquisa(nome: str):
        print()
        print(f"-------- {nome.upper()} --------")
        print()
        print()
        print("[1] Ver todos")
        print("[2] Pesquisar por ID")
        print("[3] Pesquisar por nome")
        tipo = nome.split(" ")[0]
        if tipo == "cursos":
            print("[4] Pesquisar por sigla")
            print()
            print("[5] Voltar")
            print("[6] Sair")
        elif tipo == "turmas":
            print("[4] Pesquisar por curso")
            print("[5] Pesquisar por ano")
            print()
            print("[6] Voltar")
            print("[7] Sair")
        else:
            print("[4] Pesquisar por CPF")
            if tipo == "professores":
                print()
                print("[5] Voltar")
                print("[6] Sair")
            else:
                print("[5] Pesquisar por curso")
                print("[6] Pesquisar por Turma")
                print()
                print("[7] Voltar")
                print("[8] Sair")
        print()
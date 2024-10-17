from dao import DAO

from datetime import datetime
from dateutil.relativedelta import relativedelta

import os

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

    def ver_cursos_ou_turmas_prof(id_professor: int, curso_ou_turma: str):
        tipo = curso_ou_turma[:-1]
        if tipo == "turma":
            adição = "uma"
            negacao = "nenhuma"
        else:
            adição = "um"
            negacao = "nenhum"

        alvo = "da turma" if tipo == "aluno" else "do professor"
        alvo2 = "Esta turma" if tipo == "aluno" else "Este professor"

        lista_id = []
        
        answer = ""

        while answer == "":
            print()
            print(f"-------- ALTERAR {curso_ou_turma.upper()} --------")
            print()
            print()
            print(f"Escolha {adição} {tipo} existente para excluir da lista {alvo}.")
            print(f"Digite \"+\" para adicionar mais {adição} {tipo}.")
            print("Digite \"Voltar\" para voltar ao menu anterior.")
            print("Digite \"Sair\" para sair do sistema.")
            print()

            get_info_dao = DAO()

            if tipo == "curso":
                result = get_info_dao.visualizar("id_curso", "prof_curso", " WHERE id_professor = %s", (id_professor, ), True)
                if result != None:
                    for id_cursos in result:
                        get_info_cursos = DAO()
                        info = get_info_cursos.visualizar("id_curso, nome_curso, sigla", "cursos", " WHERE id_curso = %s", (id_cursos, ), False)
                        for item in info:
                            EstruturaRepetivel.print_info_curso(item[0], item[1], item[2])
                            lista_id.append(item[0])
                else:
                    print(f"Este professor ainda não possui {negacao} {tipo}.")
            elif tipo == "turma":
                result = get_info_dao.visualizar("id_turma", "turmas", " WHERE id_professor = %s", (id_professor, ), False)
                if result != None:
                    for id_turma in result:
                        get_info_turmas = DAO()
                        info = get_info_turmas.visualizar("id_turma, nome_turma, id_curso, ano_inicio", "turmas", " WHERE id_turma = %s", (id_turma[0], ), False)
                        for item in info:
                            get_nome_curso = DAO()
                            nome_curso = get_nome_curso.visualizar("nome_curso", "cursos", " WHERE id_curso = %s", (item[2], ), True)
                            for nome in nome_curso:
                                EstruturaRepetivel.print_info_turma(item[0], item[1], nome, item[3])
                                lista_id.append(item[0]) 
                else:
                    print(f"Este professor ainda não possui {negacao} {tipo}.")
            else:
                result = get_info_dao.visualizar("id_aluno", "alunos", " WHERE id_turma = %s", (id_professor, ), False)
                if result != None and result != []:
                    for id_aluno in result:
                        get_info_aluno = DAO()
                        info = get_info_aluno.visualizar("id_aluno, nome_aluno, cpf, data_birth, id_curso, id_turma", "alunos", " WHERE id_aluno = %s", (id_aluno[0], ), False) #AQUI
                        
                        for item in info:
                            get_nome_curso = DAO()
                            nome_curso = get_nome_curso.visualizar("nome_curso", "cursos", " WHERE id_curso = %s", (item[4], ), True)
                            for nomeC in nome_curso:
                                nome_c = nomeC
                            
                            if item[5] != None:
                                get_nome_turma = DAO()
                                nome_turma = get_nome_turma.visualizar("nome_turma", "turmas", " WHERE id_turma = %s", (item[5], ), True)
                                for nomeT in nome_turma:
                                    nome_t = nomeT
                            else:
                                nome_t = ""

                            hoje = datetime.now()
                            idade = int(relativedelta(hoje, item[3]).years)
                            data_formatada = item[3].strftime("%d/%m/%Y")

                            EstruturaRepetivel.print_info_aluno(item[0], item[1], item[2], data_formatada, idade, nome_c, nome_t)
                            lista_id.append(item[0])
                else:
                    print(f"Esta turma ainda não possui nenhum aluno cadastrado.")

            print() 
            answer = input("Escolha uma opção: ")
            os.system("cls")
            try:
                num = int(answer)
                if len(lista_id) == 0:
                    input(f"{alvo2} ainda não tem {negacao} {tipo} para selecionar.... Pressione ENTER para voltar.")
                    answer = ""
                    os.system("cls")
                    continue
                else:
                    if not num in lista_id:
                        print("-----------------------------")
                        print("| DIGITE UM CARACTER VÁLIDO |")
                        print("-----------------------------")
                        print()
                        answer = ""
                        continue
                    else:
                        if tipo == "curso":
                            deletar_dao = DAO()
                            deletar_dao.deletar("prof_curso", "id_curso = %s AND id_professor = %s", (id_professor, num), "curso deletado")
                        elif tipo == "turma":
                            update_dao = DAO()
                            update_dao.atualizar("turmas", "id_professor = %s", "id_turma = %s", "turma alterada", (None, num))
                        else:
                            tirar_aluno_da_turma = DAO()
                            tirar_aluno_da_turma.atualizar("alunos", "id_turma = %s", "id_aluno = %s", "aluno alterado", (None, num))

                        answer = ""
                        continue
                
            except ValueError:
                if answer == "sair":
                    return "sair"
                elif answer == "voltar":
                    break
                elif answer == "+":
                    if tipo != "aluno":
                        if EstruturaRepetivel.escolher(curso_ou_turma, negacao, id_professor, "") == "sair":
                            return "sair"
                    else:
                        get_id_curso = DAO()
                        get_id_curso_item = get_id_curso.visualizar("id_curso", "turmas", " WHERE id_turma = %s", (id_professor, ), True)
                        for item_id in get_id_curso_item:
                            if EstruturaRepetivel.escolher(curso_ou_turma, negacao, id_professor, item_id) == "sair":
                                return "sair"
                    answer = ""
                    continue
                else:
                    print("-----------------------------")
                    print("| DIGITE UM CARACTER VÁLIDO |")
                    print("-----------------------------")
                    print()
                    answer = ""
                    continue
            except Exception as e:
                print()
                print(f"*ERRO! {e}")
                print()
                print("- - - - - - - - - - - - - - - - - - - - - - ")
                print()
                answer = ""
                continue

    def escolher(entidade, negacao: str, id_professor, id_alternativo):
        answer = ""
        list_id = []
        while answer == "":
            EstruturaRepetivel.search_header(entidade)

            get_info_dao = DAO()

            if entidade == "cursos":
                info = get_info_dao.visualizar("id_curso, nome_curso, sigla", "cursos", "", "", False)
                for item in info:
                    EstruturaRepetivel.print_info_curso(item[0], item[1], item[2])
                    list_id.append(item[0])
            elif entidade == "turmas":
                info = get_info_dao.visualizar("id_turma, nome_turma, id_curso, ano_inicio", "turmas", " WHERE id_professor = %s", (None, ), False)
                for item in info:
                    get_nome_curso = DAO()
                    nome_curso = get_nome_curso.visualizar("nome_curso", "cursos", " WHERE id_curso = %s", (item[2], ), True)
                    for nome in nome_curso:
                        EstruturaRepetivel.print_info_turma(item[0], item[1], nome, item[3])
                        list_id.append(item[0]) 
            elif entidade == "professor":
                result = get_info_dao.visualizar("id_professor", "prof_curso", " WHERE id_curso = %s", (id_professor, ), True)
                if result != None:
                    for id in result:
                        get_id_dao = DAO()
                        info = get_id_dao.visualizar("id_professor, nome_professor, cpf, data_birth", "professores", " WHERE id_professor = %s", (id, ), False)
                        for item in info:
                            hoje = datetime.now()
                            idade = int(relativedelta(hoje, item[3]).years)
                            data_formatada = item[3].strftime("%d/%m/%Y")

                            EstruturaRepetivel.print_info_professor(item[0], item[1], item[2], data_formatada, idade)
                            list_id.append(item[0])
                else:
                    input("Nenhum professor encontrado..... Pressione ENTER para voltar.")
                    os.system("cls")
                    break
            elif entidade == "alunos": # ALTERAR
                result = get_info_dao.visualizar("id_aluno, nome_aluno, cpf, data_birth, id_curso, id_turma", "alunos", " WHERE id_curso = %s", (id_alternativo, ), False) # AQUI
                if result != None and result != []:
                    for item in result:
                        get_nome_curso = DAO()
                        nome_curso = get_nome_curso.visualizar("nome_curso", "cursos", " WHERE id_curso = %s", (item[4], ), True)
                        for nomeC in nome_curso:
                            nome_c = nomeC
                        if item[5] != None:
                            get_nome_turma = DAO()
                            nome_turma = get_nome_turma.visualizar("nome_turma", "turmas", " WHERE id_turma = %s", (item[5], ), True)
                            for nomeT in nome_turma:
                                nome_t = nomeT
                        else:
                            nome_t = ""

                        hoje = datetime.now()
                        idade = int(relativedelta(hoje, item[3]).years)
                        data_formatada = item[3].strftime("%d/%m/%Y")

                        if nome_t == "":
                            EstruturaRepetivel.print_info_aluno(item[0], item[1], item[2], data_formatada, idade, nome_c, nome_t)
                            list_id.append(item[0])
                else:
                    input("Nenhum aluno encontrado..... Pressione ENTER para voltar.")
                    os.system("cls")
                    break

            else:
                result = get_info_dao.visualizar("id_turma, nome_turma, id_curso, ano_inicio", "turmas", " WHERE id_curso = %s", (id_professor, ), False)
                if result != None:
                    for item in result:
                        get_nome_curso = DAO()
                        nome_curso = get_nome_curso.visualizar("nome_curso", "cursos", " WHERE id_curso = %s", (item[2], ), True)
                        for nome in nome_curso:
                            EstruturaRepetivel.print_info_turma(item[0], item[1], nome, item[3])
                            list_id.append(item[0])
                else:
                    input("Nenhuma turma encontrada..... Pressione ENTER para voltar.")
                    os.system("cls")
                    break
            
            answer = input("Digite um ID: ")
            os.system("cls")
            try:
                num = int(answer)
                if len(list_id) == 0:
                    input(f"{negacao.title} {entidade[:-1]} por aqui.... Pressione ENTER para voltar.")
                    break
                else:
                    if not num in list_id:
                        print("-----------------------------")
                        print("| DIGITE UM CARACTER VÁLIDO |")
                        print("-----------------------------")
                        print()
                        answer = ""
                        continue
                    else:
                        if entidade == "cursos":
                            cadastrar_dao = DAO()
                            try:
                                cadastrar_dao.cadastrar("prof_curso", "id_curso, id_professor", "%s, %s", (num, id_professor, ), "curso vinculado ao professor")
                            except:
                                print("-------------------------------------------")
                                print("| PROFESSOR JÁ FOI VINCULADO A ESTE CURSO |")
                                print("-------------------------------------------")
                                print()
                                answer = ""
                                continue
                        elif entidade == "turmas":
                            update_dao = DAO()
                            update_dao.atualizar("turmas", "id_professor = %s", "id_turma = %s", "turma alterada", (id_professor, num))
                        elif entidade == "alunos":
                            update_turma_alunos = DAO()
                            update_turma_alunos.atualizar("alunos", "id_turma = %s", "id_aluno = %s", "aluno alterado", (id_professor, num))
                        else:
                            return num

                        break
            except ValueError:
                if answer == "sair":
                    return "sair"
                elif answer == "voltar":
                    break
                else:
                    print("-----------------------------")
                    print("| DIGITE UM CARACTER VÁLIDO |")
                    print("-----------------------------")
                    print()
                    answer = ""
                    continue
            except Exception as e:
                print()
                print(f"*ERRO! {e}")
                print()
                print("- - - - - - - - - - - - - - - - - - - - - - ")
                print()
                answer = ""
                continue
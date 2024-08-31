import os
from campos import Campos
from set_dao import SetDAO
from pesquisar_view import Pesquisar
from get_dao import GetDAO

class Cadastro:
    def cadastro_curso():
        tela = "CADASTRAR"
        answer = 1
        nome = ""
        sigla = ""
        while 0 < answer < 6:
            nome_requisito = "*" if nome == "" else " "
            sigla_requisito = "*" if sigla == "" else " "
            print()
            print(f"-------- CADASTRAR CURSO --------")
            print()
            print()
            print(f"[1] {nome_requisito}Nome: {nome}")
            print(f"[2] {sigla_requisito}Sigla: {sigla}")
            print()
            print("[3] Confirmar Cadastro")
            print("[4] Voltar")
            print("[5] Sair")
            print()
            try:
                num = int(input("Escolha uma opção: "))
                os.system("cls")
                if num == 1:
                    nome = Campos.texto(tela, 60, "nome")
                    if nome == "sair":
                        return "sair"

                elif num == 2:
                    sigla = Campos.texto(tela, 7, "sigla")
                    if sigla == "sair":
                        return "sair"

                elif num == 3:
                    if nome == "" or sigla == "":
                        print("----------------------------------------------")
                        print("| PREENCHA TODOS OS CAMPOS SINALIZADOS COM * |")
                        print("----------------------------------------------")
                        print()
                        answer = 1
                        continue
                    else:
                        info_curso = (nome, sigla)
                        cadastrar_curso = SetDAO()
                        cadastrar_curso.cadastrar("cursos", "nome_curso, sigla", "%s, %s", info_curso, "curso cadastrado")
                        nome = ""
                        sigla = ""

                elif num == 4:
                    break

                elif num == 5:
                    return "sair"

                else:
                    print("---------------------------")
                    print("| DIGITE UM NUMERO VÁLIDO |")
                    print("---------------------------")
                    print()
                    answer = 1
                    continue
            except ValueError:
                os.system("cls")
                print("--------------------")
                print("| DIGITE UM NUMERO |")
                print("--------------------")
                print()
                answer = 1
                continue
            except Exception as e:
                print()
                print(f"*ERRO! {e}")
                print()
                print("- - - - - - - - - - - - - - - - - - - - - - ")
                print()
                answer = 1
                continue

    def cadastro_turma():
        tela = "CADASTRAR"
        answer = 1
        curso = ""
        ano_inicio = ""
        id_curso = ""
        while 0 < answer < 6:
            curso_requisito = "*" if curso == "" else " "
            ano_inicio_requisito = "*" if ano_inicio == "" else " "
            print()
            print(f"-------- CADASTRAR TURMA --------")
            print()
            print()
            print(f"[1] {curso_requisito}Curso: {curso}")
            print(f"[2] {ano_inicio_requisito}Ano de Início: {ano_inicio}")
            print()
            print("[3] Confirmar Cadastro")
            print("[4] Voltar")
            print("[5] Sair")
            print()
            try:
                num = int(input("Escolha uma opção: "))
                os.system("cls")
                if num == 1:
                    id_curso = Pesquisar.curso(0)
                    if id_curso == "sair":
                        return "sair"
                    elif id_curso == None:
                        answer = 1
                        continue
                    else:
                        get_curso_info = GetDAO()
                        result = get_curso_info.visualizar("nome_curso", "cursos", " WHERE id_curso = %s", (id_curso, ), True)
                        for item in result:
                            curso = item

                elif num == 2:
                    ano_inicio = Campos.ano(tela, "ano")
                    if ano_inicio == "sair":
                        return "sair"

                elif num == 3:
                    if curso == "" or ano_inicio == "":
                        print("----------------------------------------------")
                        print("| PREENCHA TODOS OS CAMPOS SINALIZADOS COM * |")
                        print("----------------------------------------------")
                        print()
                        answer = 1
                        continue
                    else:
                        # CONTINUAR AQUI
                        info_curso = (nome, sigla)
                        cadastrar_curso = SetDAO()
                        cadastrar_curso.cadastrar(info_curso)
                        nome = ""
                        sigla = ""

                elif num == 4:
                    break

                elif num == 5:
                    return "sair"

                else:
                    print("---------------------------")
                    print("| DIGITE UM NUMERO VÁLIDO |")
                    print("---------------------------")
                    print()
                    answer = 1
                    continue
            except ValueError:
                os.system("cls")
                print("--------------------")
                print("| DIGITE UM NUMERO |")
                print("--------------------")
                print()
                answer = 1
                continue
            except Exception as e:
                print()
                print(f"*ERRO! {e}")
                print()
                print("- - - - - - - - - - - - - - - - - - - - - - ")
                print()
                answer = 1
                continue
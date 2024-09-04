import os
from cadastro_view import Cadastro, Pesquisar

class Estrutura:
    def inicio():
        os.system("cls")
        answer = 1
        while 0 < answer < 4:
            print()
            print("-------- EXERCÍCIO CRUD --------")
            print()
            print()
            print("[1] Cadastrar")
            print("[2] Visualizar Informações")
            print("[3] Sair")
            print()
            try:
                num = int(input("Escolha uma opção: "))
                os.system("cls")
                if 0 < num < 3:
                    if Estrutura.opcoes(num) == "sair":
                        break
                elif num == 3:
                    break
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
    
    def opcoes(escolha):
        answer = 1
        if escolha == 1:
            tela = "CADASTRAR"
        else:
            tela = "VISUALIZAR"
        while 0 < answer < 7:
            print()
            print(f"-------- {tela} --------")
            print()
            print()
            print("[1] Cursos")
            print("[2] Turmas")
            print("[3] Professores")
            print("[4] Alunos")
            print()
            print("[5] Voltar")
            print("[6] Sair")
            print()
            try:
                num = int(input("Escolha uma opção: "))
                os.system("cls")
                if num == 1:
                    if escolha == 1:
                        if Cadastro.cadastro_curso(1, "") == "sair":
                            return "sair"
                    else:
                        if Pesquisar.curso(1, "cursos cadastrados") == "sair":
                            return "sair"

                elif num == 2:
                    if escolha == 1:
                        if Cadastro.cadastro_turma(1, "") == "sair":
                            return "sair"
                    else:
                        if Pesquisar.curso(1, "turmas cadastradas") == "sair":
                            return "sair"

                elif num == 3:
                    if escolha == 1:
                        if Cadastro.cadastro_professor(1, "") == "sair":
                            return "sair"
                    else:
                        if Pesquisar.curso(1, "professores cadastrados") == "sair":
                            return "sair"

                elif num == 4:
                    if escolha == 1:
                        pass
                    else:
                        if Pesquisar.curso(1, "alunos cadastrados") == "sair":
                            return "sair"

                elif num == 5:
                    break

                elif num == 6:
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
import os
from cadastro_view import Cadastro

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
            except:
                os.system("cls")
                print("--------------------")
                print("| DIGITE UM NUMERO |")
                print("--------------------")
                print()
                answer = 1
                continue
    
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
                if escolha == 2 and 0 < num < 5:
                    pass

                elif num == 1:
                    if Cadastro.cadastro_curso() == "sair":
                        return "sair"

                elif num == 2:
                    pass

                elif num == 3:
                    pass

                elif num == 4:
                    pass

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
            except:
                os.system("cls")
                print("--------------------")
                print("| DIGITE UM NUMERO |")
                print("--------------------")
                print()
                answer = 1
                continue
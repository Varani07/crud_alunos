import os

class Cadastro:
    def cadastro_curso():
        answer = 1
        nome = ""
        sigla = ""
        while 0 < answer < 6:
            nome_requisito = "*" if nome == "" else " "
            sigla_requisito = "*" if sigla == "" else " "
            print()
            print("-------- CADASTRAR CURSO --------")
            print()
            print()
            print(f"[1] {nome_requisito}Nome: {nome}")
            print(f"[2] {sigla_requisito}Sigla: {sigla_requisito}")
            print()
            print("[3] Confirmar Cadastro")
            print("[4] Voltar")
            print("[5] Sair")
            print()
            try:
                num = int(input("Escolha uma opção: "))
                os.system("cls")
                if num == 1:
                    pass

                elif num == 2:
                    pass

                elif num == 3:
                    pass

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
            except:
                os.system("cls")
                print("--------------------")
                print("| DIGITE UM NUMERO |")
                print("--------------------")
                print()
                answer = 1
                continue
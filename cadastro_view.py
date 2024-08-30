import os
from campos import Campos
from set_dao import setDAO

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
            print(f"-------- {tela} CURSO --------")
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
                    if nome == "sair":
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
                        cadastrar_curso = setDAO()
                        cadastrar_curso.cadastrar_curso(info_curso)
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
            except:
                os.system("cls")
                print("--------------------")
                print("| DIGITE UM NUMERO |")
                print("--------------------")
                print()
                answer = 1
                continue
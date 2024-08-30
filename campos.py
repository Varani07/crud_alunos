import os

class Campos:
    def texto(tela: str, length: int, tipo: str):
        answer = ""
        while answer == "":
            print()
            print(f"-------- {tela} {tipo.upper()} --------")
            print()
            print()
            print("[1] Voltar")
            print("[2] Sair")
            print()
            answer = input(f"{tipo.title()}: ")
            try:
                num = int(answer)
                os.system("cls")
                answer = ""
                if num == 1:
                    return answer
                elif num == 2:
                    return "sair"
                else:
                    print("---------------------------")
                    print("| DIGITE UM NUMERO VÁLIDO |")
                    print("---------------------------")
                    print()
                    continue
            except:
                os.system("cls")
                if len(answer) > length:
                    print("----------------------------------")
                    print(f"| {tipo.upper()} COM EXCESSO DE CARACTERES |")
                    print("----------------------------------")
                    print()
                    answer = ""
                    continue
                else:
                    return answer.upper()
import os
from datetime import datetime

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
                    answer = ""
                    continue
            except ValueError:
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
            except Exception as e:
                print()
                print(f"*ERRO! {e}")
                print()
                print("- - - - - - - - - - - - - - - - - - - - - - ")
                print()
                answer = ""
                continue
                
    def ano(tela: str, tipo: str):
        answer = ""
        while answer == "":
            hoje = datetime.now().year
            print()
            print(f"-------- {tela} {tipo.upper()} --------")
            print()
            print()
            print(f"[1] {hoje}")
            print(f"[2] {hoje + 1}")
            print(f"[3] {hoje + 2}")
            print(f"[4] {hoje + 3}")
            print(f"[5] {hoje + 4}")
            print(f"[6] {hoje + 5}")
            print()
            print("[7] Voltar")
            print("[8] Sair")
            print()
            answer = input(f"Escolha um ano: ")
            try:
                num = int(answer)
                os.system("cls")
                answer = ""
                if num == 1:
                    return hoje
                elif num == 2:
                    return hoje + 1
                elif num == 3:
                    return hoje + 2
                elif num == 4:
                    return hoje + 3
                elif num == 5:
                    return hoje + 4
                elif num == 6:
                    return hoje + 5
                elif num == 7:
                    return answer
                elif num == 8:
                    return "sair"
                else:
                    print("---------------------------")
                    print("| DIGITE UM NUMERO VÁLIDO |")
                    print("---------------------------")
                    print()
                    continue
            except ValueError:
                os.system("cls")
                print("---------------------------")
                print("| DIGITE UM NUMERO VÁLIDO |")
                print("---------------------------")
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
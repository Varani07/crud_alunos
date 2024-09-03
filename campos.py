import os
from datetime import datetime
from dateutil.relativedelta import relativedelta

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

    def data(tela: str, tipo: str, professor: bool):
        if professor:
            min_num = 18
            max_num = 159
        else:
            min_num = 14
            max_num = 159
        data_formato_certo = True
        answer = ""
        while answer == "":
            print()
            print(f"-------- {tela} {tipo.upper()} --------")
            print()
            print()
            print("[1] Voltar")
            print("[2] Sair")
            print()
            answer = input(f"{tipo.title()} (dd/mm/yyyy): ")
            try:
                num = int(answer)
                os.system("cls")
                answer = ""
                if num == 1:
                    return answer, ""
                elif num == 2:
                    return "sair", ""
                else:
                    print("---------------------------")
                    print("| DIGITE UM NUMERO VÁLIDO |")
                    print("---------------------------")
                    print()
                    answer = ""
                    continue
            except ValueError:
                os.system("cls")
                if len(answer) != 10:
                    answer = ""
                    continue 
                i = 0
                for char in answer:
                    if 0 <= i < 2 or 2 < i < 5 or 5 < i < 10:
                        try:
                            int(char)
                        except ValueError as e:
                            print("------------------------------------")
                            print("| PREENCHA O CAMPO CONFORME MODELO |")
                            print("------------------------------------")
                            print()
                            data_formato_certo = False
                            break
                    elif i == 2 and char != "/" or i == 5 and char != "/":
                        print("------------------------------------")
                        print("| PREENCHA O CAMPO CONFORME MODELO |")
                        print("------------------------------------")
                        print()
                        data_formato_certo = False
                        break
                    i += 1
                if data_formato_certo:
                    aniversario = datetime.strptime(answer, "%d/%m/%Y")
                    hoje = datetime.now()
                    difference_in_years = int(relativedelta(hoje, aniversario).years)
                    if difference_in_years < min_num or difference_in_years > max_num:
                        answer = ""
                        print("-----------------------------")
                        print("| DATA FORNECIDA É INVÁLIDA |")
                        print("-----------------------------")
                        print()
                        continue
                    else:
                        return answer, difference_in_years
                else:
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

    def cpf(tela: str):
        cpf_formato_certo = True
        answer = ""
        while answer == "":
            print()
            print(f"-------- {tela} CPF --------")
            print()
            print()
            print("[1] Voltar")
            print("[2] Sair")
            print()
            answer = input("CPF (000.000.000-00): ")
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
                if len(answer) != 14:
                    print("------------------------------------")
                    print("| PREENCHA O CAMPO CONFORME MODELO |")
                    print("------------------------------------")
                    print()
                    answer = ""
                    continue 
                i = 0
                for char in answer:
                    if 0 <= i < 3 or 3 < i < 7 or 7 < i < 11 or 11 < i < 14:
                        try:
                            int(char)
                        except ValueError as e:
                            print("------------------------------------")
                            print("| PREENCHA O CAMPO CONFORME MODELO |")
                            print("------------------------------------")
                            print()
                            cpf_formato_certo = False
                            break
                    elif i == 3 and char != "." or i == 7 and char != ".":
                        print("------------------------------------")
                        print("| PREENCHA O CAMPO CONFORME MODELO |")
                        print("------------------------------------")
                        print()
                        cpf_formato_certo = False
                        break
                    elif i == 11 and char != "-":
                        print("------------------------------------")
                        print("| PREENCHA O CAMPO CONFORME MODELO |")
                        print("------------------------------------")
                        print()
                        cpf_formato_certo = False
                        break
                    i += 1
                if cpf_formato_certo:
                    return answer
                else:
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
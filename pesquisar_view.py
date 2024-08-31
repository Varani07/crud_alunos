import os
from util import EstruturaRepetivel
from get_dao import GetDAO

class Pesquisar:
    def curso(ver_detalhes):
        os.system("cls")
        answer = 1
        id_curso = ""
        while 0 < answer < 7:
            print()
            print("-------- CURSOS CADASTRADOS --------")
            print()
            print()
            print("[1] Ver todos")
            print("[2] Pesquisar por ID")
            print("[3] Pesquisar por nome")
            print("[4] Pesquisar por sigla")
            print()
            print("[5] Voltar")
            print("[6] Sair")
            print()
            answer = input("Escolha uma opção: ")
            try:
                num = int(answer)
                os.system("cls")
                if 0 < num < 5:
                    id_curso = TelaInfo.mostrar_info(num, ver_detalhes, "curso", "cursos")
                    if id_curso == "sair":
                        return "sair"
                    elif id_curso == None:
                        answer = 1
                        continue
                    else:
                        return id_curso
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
                answer = 1
                continue

class TelaInfo:
    def mostrar_info(num: int, ver_detalhes: bool, tipo: str, tipo_plural: str):
        id = ""
        while id == "":
            EstruturaRepetivel.search_header(tipo_plural, ver_detalhes)

            if  1 != num:
                answer = ""
                while answer == "":
                    answer = input("Pesquisar: ")
                    os.system("cls")
                    try:
                        answer = int(answer)
                        if num != 2:
                            print("------------------------------------------")
                            print("| NUMEROS NÃO SÃO PERMITIDOS NESSE CAMPO |")
                            print("------------------------------------------")
                            print()
                            EstruturaRepetivel.search_header(tipo_plural, ver_detalhes)
                            answer = ""
                            continue

                    except ValueError:
                        if answer.lower() == "voltar":
                            break
                        elif answer.lower() == "sair":
                            return "sair"
                        # elif ver_detalhes:
                        #     if answer == "+":
                        #         answer = ""

                        #         if tipo == "curso":
                        #             if Cadastro.cadastro_curso() == "sair":
                        #                 return "sair", ""
                                    
                        #         elif tipo == "turma":
                        #             pass

                        #         elif tipo == "professor":
                        #             pass

                        #         elif tipo == "aluno":
                        #             pass

                                # ADICIONAR OUTROS ACIMA
                        elif num == 2:
                            print("--------------------")
                            print("| DIGITE UM NUMERO |")
                            print("--------------------")
                            print()
                            EstruturaRepetivel.search_header(tipo_plural, ver_detalhes)
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
                EstruturaRepetivel.search_header(tipo_plural, ver_detalhes)
            
            lista_id = []
            if num == 1:
                vis_inf = GetDAO()

                if tipo == "curso":
                    result = vis_inf.visualizar("id_curso, nome_curso, sigla", "cursos", "", "", False)
                    for item in result:
                        EstruturaRepetivel.print_info_curso(item[0], item[1], item[2])
                        lista_id.append(item[0])
                    
                elif tipo == "turma":
                    result = vis_inf.visualizar("")

                elif tipo == "professor":
                    pass

                elif tipo == "aluno":
                    pass

            elif num == 2:
                vis_inf = GetDAO()

                if tipo == "curso":
                    pass
                    
                elif tipo == "turma":
                    pass

                elif tipo == "professor":
                    pass

                elif tipo == "aluno":
                    pass

            elif num == 3:
                vis_inf = GetDAO()

                if tipo == "curso":
                    pass
                    
                elif tipo == "turma":
                    pass

                elif tipo == "professor":
                    pass

                elif tipo == "aluno":
                    pass

            elif num == 4:
                vis_inf = GetDAO()

                if tipo == "curso":
                    pass
                    
                elif tipo == "turma":
                    pass

                elif tipo == "professor":
                    pass

                elif tipo == "aluno":
                    pass

            elif num == 5:
                vis_inf = GetDAO()

                if tipo == "turma":
                    pass

                elif tipo == "aluno":
                    pass

            elif num == 6:
                vis_inf = GetDAO()


            if len(lista_id) == 0:
                input(f"Zero resultados pesquisando por {answer} em {tipo_plural.upper()}")
            else:
                print()
                id = input("Digite o ID: ")
                os.system("cls")
                try:
                    id = int(id)
                    if id in lista_id:
                        if not ver_detalhes:
                            return id
                    else:
                        print("---------------------------")
                        print("| DIGITE UM NUMERO VÁLIDO |")
                        print("---------------------------")
                        print()
                        id = ""
                        continue
                except ValueError:
                    if id.lower() == "voltar":
                            break
                    elif id.lower() == "sair":
                        return "sair"
                    else:
                        print("--------------------")
                        print("| DIGITE UM NUMERO |")
                        print("--------------------")
                        print()
                        id = ""
                        continue
                except Exception as e:
                    print()
                    print(f"*ERRO! {e}")
                    print()
                    print("- - - - - - - - - - - - - - - - - - - - - - ")
                    print()
                    id = ""
                    continue
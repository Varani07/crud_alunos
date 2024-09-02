import os
from util import EstruturaRepetivel
from get_dao import GetDAO

class Pesquisar:
    def curso(ver_detalhes, titulo: str):
        os.system("cls")
        answer = 1
        id_curso = ""
        tipo_interacao_plural = titulo.split(" ")[0]
        if tipo_interacao_plural == "professores":
            tipo_interacao = tipo_interacao_plural[:-2]
        else:
            tipo_interacao = tipo_interacao_plural[:-1]
        if tipo_interacao == "turma":
            max_num = 8
        elif tipo_interacao == "aluno":
            max_num = 9
        else: 
            max_num = 7
        while 0 < answer < max_num:
            EstruturaRepetivel.op_pesquisa(titulo)
            answer = input("Escolha uma opção: ")
            try:
                num = int(answer)
                os.system("cls")
                if 0 < num < max_num - 2:
                    id_curso = TelaInfo.mostrar_info(num, ver_detalhes, tipo_interacao, tipo_interacao_plural)
                    if id_curso == "sair":
                        return "sair"
                    elif id_curso == None:
                        answer = 1
                        continue
                    else:
                        return id_curso
                elif num == max_num - 2:
                    break
                elif num == max_num - 1:
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
            if num == 1: #PESQUISAR SEM WHERE DEFINIDO
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

            elif num == 2: #FILTRAR PELO ID
                vis_inf = GetDAO()

                if tipo == "curso":
                    result = vis_inf.visualizar("id_curso, nome_curso, sigla", "cursos", f" WHERE id_cursos LIKE '%{answer}%'")
                    
                elif tipo == "turma":
                    pass

                elif tipo == "professor":
                    pass

                elif tipo == "aluno":
                    pass

            elif num == 3: #FILTRAR PELO NOME
                vis_inf = GetDAO()

                if tipo == "curso":
                    result = vis_inf.visualizar("id_curso, nome_curso, sigla", "cursos", f" WHERE nome_curso LIKE '%{answer}%'")
                    
                elif tipo == "turma":
                    pass

                elif tipo == "professor":
                    pass

                elif tipo == "aluno":
                    pass

            elif num == 4:
                vis_inf = GetDAO()

                if tipo == "curso": #FILTRAR POR SIGLA
                    result = vis_inf.visualizar("id_curso, nome_curso, sigla", "cursos", f" WHERE sigla LIKE '%{answer}%'")
                    
                elif tipo == "turma": #FILTRAR POR CURSO
                    pass

                elif tipo == "professor": #FILTRAR POR CPF
                    pass

                elif tipo == "aluno": #FILTRAR POR CPF
                    pass

            elif num == 5:
                vis_inf = GetDAO()

                if tipo == "turma": #FILTRAR POR ANO
                    pass

                elif tipo == "aluno": #FILTRAR POR CURSO
                    pass

            elif num == 6: #FILTRAR POR TURMA
                vis_inf = GetDAO()

            # Iterando pelos itens presentes no resultado da pesquisa
            if tipo == "curso": 
                for item in result:
                    EstruturaRepetivel.print_info_curso(item[0], item[1], item[2])
                    lista_id.append(item[0])
                
            elif tipo == "turma":
                pass

            elif tipo == "professor":
                pass

            elif tipo == "aluno":
                pass

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
import os
from campos import Campos

from set_dao import SetDAO
from get_dao import GetDAO
from update_dao import UpdateDAO
from delete_dao import DeleteDAO

from util import EstruturaRepetivel

class Cadastro:
    def cadastro_curso(cadastrar, id):
        if cadastrar:
            tela = "CADASTRAR"
            confirmar = "Cadastro"
            nome = ""
            sigla = ""
        else:
            tela = "ATUALIZAR"
            confirmar = "Alterações"
            get_info = GetDAO()
            result = get_info.visualizar("nome_curso, sigla", "cursos", " WHERE id_curso = %s", (id, ), False)
            for item in result:
                nome = item[0]
                sigla = item[1]
                nome_confirm = item[0]
                sigla_confirm = item[1]

        answer = 1

        while 0 < answer < 6:
            nome_requisito = "*" if nome == "" else " "
            sigla_requisito = "*" if sigla == "" else " "
            print()
            print(f"-------- {tela} CURSO --------")
            print()
            print(f"[1] {nome_requisito}Nome: {nome}")
            print(f"[2] {sigla_requisito}Sigla: {sigla}")
            print()
            print(f"[3] Confirmar {confirmar}")
            print("[4] Voltar")
            print("[5] Sair")
            print()
            if not cadastrar:
                print("*Digite 'DELETAR' para excluir curso.")
            print()
            answer = input("Escolha uma opção: ")
            os.system("cls")
            try:
                num = int(answer)
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
                    else:
                        if cadastrar:
                            info_curso = (nome, sigla)
                            cadastrar_curso = SetDAO()
                            cadastrar_curso.cadastrar("cursos", "nome_curso, sigla", "%s, %s", info_curso, "curso cadastrado")
                            nome = ""
                            sigla = ""
                        else:
                            if sigla == sigla_confirm and nome == nome_confirm:
                                print("-----------------------------------------------")
                                print("| ALTERE ALGUMA INFORMAÇÃO ANTES DE CONFIRMAR |")
                                print("-----------------------------------------------")
                                print()
                            else:
                                atualizar_curso = UpdateDAO()
                                info = (nome, sigla)
                                atualizar_curso.atualizar("cursos", "nome_curso = %s, sigla = %s", f"id_curso = {id}", "curso alterado", info)
                                nome_confirm = nome
                                sigla_confirm = sigla

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
                if not cadastrar and answer.upper() == "DELETAR":
                    deletar_curso = DeleteDAO()
                    deletar_curso.deletar("cursos", "id_curso = %s", (id, ), "curso deletado")
                    break
                else:
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

    def cadastro_turma(cadastrar, id):
        if cadastrar:
            tela = "CADASTRAR"
            confirmar = "Cadastro"
            curso = ""
            ano_inicio = ""
            id_curso = ""
        else:
            tela = "ATUALIZAR"
            confirmar = "Alterações"

            get_info = GetDAO()
            result = get_info.visualizar("id_curso, ano_inicio", "cursos", " WHERE id_turma = %s", (id, ), False)
            for item in result:
                id_curso = item[0]
                ano_inicio = item[1]

            get_curso_info = GetDAO()
            result = get_curso_info.visualizar("nome_curso", "cursos", " WHERE id_curso = %s", (id_curso, ), True)
            for item in result:
                curso = item

        answer = 1

        while 0 < answer < 6:
            curso_requisito = "*" if curso == "" else " "
            ano_inicio_requisito = "*" if ano_inicio == "" else " "
            print()
            print(f"-------- {tela} TURMA --------")
            print()
            print()
            print(f"[1] {curso_requisito}Curso: {curso}")
            print(f"[2] {ano_inicio_requisito}Ano de Início: {ano_inicio}")
            print()
            print(f"[3] Confirmar {confirmar}")
            print("[4] Voltar")
            print("[5] Sair")
            print()
            try:
                num = int(input("Escolha uma opção: "))
                os.system("cls")
                if num == 1:
                    id_curso = Pesquisar.curso(0, "cursos cadastrados")
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
                        info_turma = (id_curso, ano_inicio)
                        cadastrar_turma = SetDAO()
                        cadastrar_turma.cadastrar("turmas", "id_curso, ano_inicio", "%s, %s", info_turma, "turma cadastrada")
                        ano_inicio = ""
                        curso = ""

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
            EstruturaRepetivel.search_header(tipo_plural)

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
                            EstruturaRepetivel.search_header(tipo_plural)
                            answer = ""
                            continue

                    except ValueError:
                        if answer.lower() == "voltar":
                            return None
                        elif answer.lower() == "sair":
                            return "sair"
                        elif num == 2:
                            print("--------------------")
                            print("| DIGITE UM NUMERO |")
                            print("--------------------")
                            print()
                            EstruturaRepetivel.search_header(tipo_plural)
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
                EstruturaRepetivel.search_header(tipo_plural)
            
            lista_id = []
            if num == 1: #PESQUISAR SEM WHERE DEFINIDO
                vis_inf = GetDAO()

                if tipo == "curso":
                    result = vis_inf.visualizar("id_curso, nome_curso, sigla", "cursos", "", "", False)
                    
                elif tipo == "turma":
                    result = vis_inf.visualizar("")

                elif tipo == "professor":
                    pass

                elif tipo == "aluno":
                    pass

            elif num == 2: #FILTRAR PELO ID
                vis_inf = GetDAO()

                if tipo == "curso":
                    result = vis_inf.visualizar("id_curso, nome_curso, sigla", "cursos", f" WHERE id_curso LIKE '%{answer}%'", "", False)
                    
                elif tipo == "turma":
                    pass

                elif tipo == "professor":
                    pass

                elif tipo == "aluno":
                    pass

            elif num == 3: #FILTRAR PELO NOME
                vis_inf = GetDAO()

                if tipo == "curso":
                    result = vis_inf.visualizar("id_curso, nome_curso, sigla", "cursos", f" WHERE nome_curso LIKE '%{answer}%'", "", False)
                    
                elif tipo == "turma":
                    pass

                elif tipo == "professor":
                    pass

                elif tipo == "aluno":
                    pass

            elif num == 4:
                vis_inf = GetDAO()

                if tipo == "curso": #FILTRAR POR SIGLA
                    result = vis_inf.visualizar("id_curso, nome_curso, sigla", "cursos", f" WHERE sigla LIKE '%{answer}%'", "", False)
                    
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
                input(f"Zero resultados pesquisando por {answer} em {tipo_plural.upper()}..... Pressione ENTER para continuar.")
                os.system("cls")
                id = ""
                answer = ""
                continue
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
                            if tipo == "curso": 
                                if Cadastro.cadastro_curso(0, id) == "sair":
                                    return "sair"
                                
                            elif tipo == "turma":
                                pass

                            elif tipo == "professor":
                                pass

                            elif tipo == "aluno":
                                pass
        
                    else:
                        print("---------------------------")
                        print("| DIGITE UM NUMERO VÁLIDO |")
                        print("---------------------------")
                        print()
                        id = ""
                        continue
                except ValueError:
                    if id.lower() == "voltar":
                            if num == 1:
                                break
                            else:
                                id = ""
                                answer = ""
                                continue
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
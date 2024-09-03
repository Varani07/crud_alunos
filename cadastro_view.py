import os
from datetime import datetime
from dateutil.relativedelta import relativedelta

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
            professor_responsavel = ""
        else:
            tela = "ATUALIZAR"
            confirmar = "Alterações"

            get_info = GetDAO()
            result = get_info.visualizar("id_curso, ano_inicio, id_professor", "turmas", " WHERE id_turma = %s", (id, ), False)
            for item in result:
                id_curso = item[0]
                ano_inicio = item[1]
                id_professor = item[2]

            get_curso_info = GetDAO()
            get_nome_curso = get_curso_info.visualizar("nome_curso", "cursos", " WHERE id_curso = %s", (id_curso, ), True)
            for nome in get_nome_curso:
                curso = nome

            if id_professor != None:
                get_professor_info = GetDAO()
                get_nome_professor = get_professor_info.visualizar("nome_professor", "professores", " WHERE id_professor = %s", (id_professor, ), True)
                for nome_prof in get_nome_professor:
                    professor_responsavel = nome_prof

            curso_confirm = curso
            ano_inicio_confirm = ano_inicio
            professor_responsavel_confirm = professor_responsavel

        answer = 1

        while 0 < answer < 7:
            curso_requisito = "*" if curso == "" else " "
            ano_inicio_requisito = "*" if ano_inicio == "" else " "
            print()
            print(f"-------- {tela} TURMA --------")
            print()
            print()
            print(f"[1] {curso_requisito}Curso: {curso}")
            print(f"[2] {ano_inicio_requisito}Ano de Início: {ano_inicio}")
            print(f"[3]  Professor Responsável: {professor_responsavel}")
            print()
            print(f"[4] Confirmar {confirmar}")
            print("[5] Voltar")
            print("[6] Sair")
            print()
            if not cadastrar:
                print("*Digite 'DELETAR' para excluir turma.")
            print()
            answer = input("Escolha uma opção: ")
            os.system("cls")
            try:
                num = int(answer)
                if num == 1:
                    id_curso = Pesquisar.curso(0, "cursos cadastrados")
                    if id_curso == "sair":
                        return "sair"
                    elif id_curso == None:
                        curso = ""
                    else:
                        get_curso_info = GetDAO()
                        get_nome_curso = get_curso_info.visualizar("nome_curso", "cursos", " WHERE id_curso = %s", (id_curso, ), True)
                        for nome in get_nome_curso:
                            curso = nome

                elif num == 2:
                    ano_inicio = Campos.ano(tela, "ano de início da turma")
                    if ano_inicio == "sair":
                        return "sair"
                    
                elif num == 3:
                    id_professor = Pesquisar.curso(0, "professores cadastrados")
                    if id_professor == "sair":
                        return "return"
                    elif id_professor == None:
                        professor_responsavel = ""
                    else:
                        get_professor_info = GetDAO()
                        get_nome_professor = get_professor_info.visualizar("nome_professor", "professores", " WHERE id_professor = %s", (id_professor, ), True)
                        for nome_prof in get_nome_professor:
                            professor_responsavel = nome_prof

                elif num == 4:
                    if curso == "" or ano_inicio == "":
                        print("----------------------------------------------")
                        print("| PREENCHA TODOS OS CAMPOS SINALIZADOS COM * |")
                        print("----------------------------------------------")
                        print()
                    else:
                        if id_professor == "":
                            id_professor = None
                        if cadastrar:
                            info_turma = (id_curso, ano_inicio, id_professor)
                            cadastrar_turma = SetDAO()
                            cadastrar_turma.cadastrar("turmas", "id_curso, ano_inicio, id_professor", "%s, %s, %s", info_turma, "turma cadastrada")
                            curso = ""
                            ano_inicio = ""
                        else:
                            if curso == curso_confirm and ano_inicio == ano_inicio_confirm and professor_responsavel == professor_responsavel_confirm:
                                print("-----------------------------------------------")
                                print("| ALTERE ALGUMA INFORMAÇÃO ANTES DE CONFIRMAR |")
                                print("-----------------------------------------------")
                                print()
                            else:
                                atualizar_curso = UpdateDAO()
                                info = (id_curso, ano_inicio, id_professor)
                                atualizar_curso.atualizar("turmas", "id_curso = %s, ano_inicio = %s, id_professor = %s", f"id_turma = {id}", "turma alterada", info)
                                curso_confirm = curso
                                ano_inicio_confirm = ano_inicio
                                professor_responsavel_confirm = professor_responsavel

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
                if not cadastrar and answer.upper() == "DELETAR":
                    deletar_curso = DeleteDAO()
                    deletar_curso.deletar("turmas", "id_turma = %s", (id, ), "turma deletada")
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

    def cadastro_professor(cadastrar, id):
        if cadastrar:
            tela = "CADASTRAR"
            confirmar = "Cadastro"
            alterar = False

            nome_professor = ""
            data_nascimento = ""
            idade = ""
            cpf = ""

            num_confirmar = 4
            num_voltar = 5
            num_sair = 6
        else:
            tela = "ATUALIZAR"
            confirmar = "Alterações"
            alterar = True

            get_info = GetDAO()
            result = get_info.visualizar("nome_professor, data_birth, cpf", "professores", " WHERE id_professor = %s", (id, ), False)
            for item in result:
                nome_professor = item[0]
                data_nascimento = item[1].strftime("%d/%m/%Y")
                cpf = item[2]
                hoje = datetime.now()
                idade = int(relativedelta(hoje - item[1]).years)

                num_confirmar = 6
                num_voltar = 7
                num_sair = 8

            nome_professor_confirm = nome_professor
            data_nascimento_confirm = data_nascimento
            cpf_confirm = cpf

        answer = 1

        while 0 < answer < 9:
            nome_professor_requisito = "*" if nome_professor == "" else " "
            data_nascimento_requisito = "*" if data_nascimento == "" else " "
            cpf_requisito = "*" if cpf == "" else " "
            print()
            print(f"-------- {tela} PROFESSOR --------")
            print()
            print()
            print(f"[1] {nome_professor_requisito}Nome: {nome_professor}")
            print(f"[2] {data_nascimento_requisito}Ano de Início: {data_nascimento}  | Idade {idade}")
            print(f"[3] {cpf_requisito}CPF: {cpf}")
            print()
            if alterar:
                print("[4] Cursos")
                print("[5] Ver Turmas")
                print()
            print(f"[{num_confirmar}] Confirmar {confirmar}")
            print(f"[{num_voltar}] Voltar")
            print(f"[{num_sair}] Sair")
            print()
            if not cadastrar:
                print("*Digite 'DELETAR' para excluir professor.")
            print()
            answer = input("Escolha uma opção: ")
            os.system("cls")
            try:
                num = int(answer)
                if num == 1:
                    nome_professor = Campos.texto(tela, 100, "nome")
                    if nome_professor == "sair":
                        return "sair"

                elif num == 2:
                    data_nascimento, idade = Campos.data(tela, "data de nascimenento", True)
                    if data_nascimento == "sair":
                        return "sair"
                    
                elif num == 3:
                    cpf = Campos.cpf(tela)
                    if cpf == "sair":
                        return "sair"
                    
                elif num == 4 and alterar:
                    EstruturaRepetivel.ver_cursos_ou_turmas_prof(id, "cursos")

                elif num == 5 and alterar:
                    pass

                elif num == num_confirmar:
                    if curso == "" or ano_inicio == "":
                        print("----------------------------------------------")
                        print("| PREENCHA TODOS OS CAMPOS SINALIZADOS COM * |")
                        print("----------------------------------------------")
                        print()
                    else:
                        if cadastrar:
                            info_turma = (id_curso, ano_inicio)
                            cadastrar_turma = SetDAO()
                            cadastrar_turma.cadastrar("turmas", "id_curso, ano_inicio", "%s, %s", info_turma, "turma cadastrada")
                            curso = ""
                            ano_inicio = ""
                        else:
                            if curso == curso_confirm and ano_inicio == ano_inicio_confirm:
                                print("-----------------------------------------------")
                                print("| ALTERE ALGUMA INFORMAÇÃO ANTES DE CONFIRMAR |")
                                print("-----------------------------------------------")
                                print()
                            else:
                                atualizar_curso = UpdateDAO()
                                info = (id_curso, ano_inicio)
                                atualizar_curso.atualizar("turmas", "id_curso = %s, ano_inicio = %s", f"id_turma = {id}", "turma alterada", info)
                                curso_confirm = curso
                                ano_inicio_confirm = ano_inicio

                elif num == num_voltar:
                    break

                elif num == num_sair:
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
                    deletar_curso.deletar("turmas", "id_turma = %s", (id, ), "turma deletada")
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

class Pesquisar:
    def curso(ver_detalhes, titulo: str):
        os.system("cls")

        answer = 1
        id = ""

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
                    id = TelaInfo.mostrar_info(num, ver_detalhes, tipo_interacao, tipo_interacao_plural)
                    if id == "sair":
                        return "sair"
                    elif id == None:
                        answer = 1
                        continue
                    else:
                        return id
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
                    result = vis_inf.visualizar("id_turma, nome_turma, id_curso, ano_inicio", "turmas", "", "", False)

                elif tipo == "professor":
                    result = vis_inf.visualizar("id_professor, nome_professor, cpf, data_birth", "professores", "", "", False)

                elif tipo == "aluno":
                    result = vis_inf.visualizar("id_aluno, nome_aluno, cpf, data_birth, id_curso, id_turma", "alunos", "", "", False)

            elif num == 2: #FILTRAR PELO ID
                vis_inf = GetDAO()

                if tipo == "curso":
                    result = vis_inf.visualizar("id_curso, nome_curso, sigla", "cursos", f" WHERE id_curso LIKE '%{answer}%'", "", False)
                    
                elif tipo == "turma":
                    result = vis_inf.visualizar("id_turma, nome_turma, id_curso, ano_inicio", "turmas", f" WHERE id_turma LIKE '%{answer}%'", "", False)

                elif tipo == "professor":
                    result = vis_inf.visualizar("id_professor, nome_professor, cpf, data_birth", "professores", f" WHERE id_professor LIKE '%{answer}%'", "", False)

                elif tipo == "aluno":
                    result = vis_inf.visualizar("id_aluno, nome_aluno, cpf, data_birth, id_curso, id_turma", "alunos", f" WHERE id_aluno LIKE '%{answer}%'", "", False)

            elif num == 3: #FILTRAR PELO NOME
                vis_inf = GetDAO()

                if tipo == "curso":
                    result = vis_inf.visualizar("id_curso, nome_curso, sigla", "cursos", f" WHERE nome_curso LIKE '%{answer}%'", "", False)
                    
                elif tipo == "turma":
                    result = vis_inf.visualizar("id_turma, nome_turma, id_curso, ano_inicio", "turmas", f" WHERE nome_turma LIKE '%{answer}%'", "", False)

                elif tipo == "professor":
                    result = vis_inf.visualizar("id_professor, nome_professor, cpf, data_birth", "professores", f" WHERE nome_professor LIKE '%{answer}%'", "", False)

                elif tipo == "aluno":
                    result = vis_inf.visualizar("id_aluno, nome_aluno, cpf, data_birth, id_curso, id_turma", "alunos", f" WHERE nome_aluno LIKE '%{answer}%'", "", False)

            elif num == 4:
                vis_inf = GetDAO()

                if tipo == "curso": #FILTRAR POR SIGLA
                    result = vis_inf.visualizar("id_curso, nome_curso, sigla", "cursos", f" WHERE sigla LIKE '%{answer}%'", "", False)
                    
                elif tipo == "turma": #FILTRAR POR CURSO
                    os.system("cls")
                    id_curso_para_filtrar_turma = Pesquisar.curso(0, "cursos cadastrados")
                    if id_curso_para_filtrar_turma == "sair":
                        return "sair"
                    elif id_curso_para_filtrar_turma == None:
                        id = ""
                        answer = ""
                        continue
                    else:
                        EstruturaRepetivel.search_header(tipo_plural)
                        result = vis_inf.visualizar("id_turma, nome_turma, id_curso, ano_inicio", "turmas", f" WHERE id_curso LIKE '%{id_curso_para_filtrar_turma}%'", "", False)

                elif tipo == "professor": #FILTRAR POR CPF
                    result = vis_inf.visualizar("id_professor, nome_professor, cpf, data_birth", "professores", f" WHERE cpf LIKE '%{answer}%'", "", False)

                elif tipo == "aluno": #FILTRAR POR CPF
                    result = vis_inf.visualizar("id_aluno, nome_aluno, cpf, data_birth, id_curso, id_turma", "alunos", f" WHERE cpf LIKE '%{answer}%'", "", False)

            elif num == 5:
                vis_inf = GetDAO()

                if tipo == "turma": #FILTRAR POR ANO
                    result = vis_inf.visualizar("id_turma, nome_turma, id_curso, ano_inicio", "turmas", f" WHERE ano_inicio LIKE '%{answer}%'", "", False)

                elif tipo == "aluno": #FILTRAR POR CURSO
                    os.system("cls")
                    id_curso_para_filtrar_aluno = Pesquisar.curso(0, "cursos cadastrados")
                    if id_curso_para_filtrar_aluno == "sair":
                        return "sair"
                    elif id_curso_para_filtrar_aluno == None:
                        id = ""
                        answer = ""
                        continue
                    else:
                        EstruturaRepetivel.search_header(tipo_plural)
                        result = vis_inf.visualizar("id_aluno, nome_aluno, cpf, data_birth, id_curso, id_turma", "alunos", f" WHERE id_curso LIKE '%{id_curso_para_filtrar_aluno}%'", "", False)

            elif num == 6: #FILTRAR POR TURMA
                vis_inf = GetDAO()
                os.system("cls")
                id_turma_para_filtrar_aluno = Pesquisar.curso(0, "turmas cadastradas")
                if id_turma_para_filtrar_aluno == "sair":
                    return "sair"
                elif id_turma_para_filtrar_aluno == None:
                    id = ""
                    answer = ""
                    continue
                else:
                    EstruturaRepetivel.search_header(tipo_plural)
                    result = vis_inf.visualizar("id_aluno, nome_aluno, cpf, data_birth, id_curso, id_turma", "alunos", f" WHERE id_turma LIKE '%{id_turma_para_filtrar_aluno}%'", "", False)

            # Iterando pelos itens presentes no resultado da pesquisa
            if tipo == "curso": 
                for item in result:
                    EstruturaRepetivel.print_info_curso(item[0], item[1], item[2])
                    lista_id.append(item[0])
                
            elif tipo == "turma":
                for item in result:
                    get_nome_curso = GetDAO()
                    nome_curso = get_nome_curso.visualizar("nome_curso", "cursos", " WHERE id_curso = %s", (item[2], ), True)
                    for nome in nome_curso:
                        EstruturaRepetivel.print_info_turma(item[0], item[1], nome, item[3])
                        lista_id.append(item[0])
                
                if num == 4:
                    answer = nome

            elif tipo == "professor": # CALCULAR IDADE
                for item in result:
                    hoje = datetime.now()
                    idade = int(relativedelta(hoje - item[3]).years)
                    data_formatada = item[3].strftime("%d/%m/%Y")

                    EstruturaRepetivel.print_info_professor(item[0], item[1], item[2], data_formatada, idade)
                    lista_id.append(item[0])

            elif tipo == "aluno": # CALCULAR IDADE
                for item in result:

                    get_nome_curso = GetDAO()
                    nome_curso = get_nome_curso.visualizar("nome_curso", "cursos", " WHERE id_curso = %s", (item[4], ), True)
                    for nomeC in nome_curso:
                        nome_c = nomeC
                    
                    get_nome_turma = GetDAO()
                    nome_turma = get_nome_turma.visualizar("nome_turma", "turmas", " WHERE id_turma = %s", (item[5], ), True)
                    for nomeT in nome_turma:
                        nome_t = nomeT

                    hoje = datetime.now()
                    idade = int(relativedelta(hoje - item[3]).years)
                    data_formatada = item[3].strftime("%d/%m/%Y")

                    EstruturaRepetivel.print_info_aluno(item[0], item[1], item[2], data_formatada, idade, nome_c, nome_t)
                    lista_id.append(item[0])
                
                if num == 5:
                    answer = nome_c
                elif num == 6:
                    answer = nome_t

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
                                if Cadastro.cadastro_turma(0, id) == "sair":
                                    return "sair"

                            elif tipo == "professor":
                                if Cadastro.cadastro_professor(0, id) == "sair":
                                    return "sair"

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
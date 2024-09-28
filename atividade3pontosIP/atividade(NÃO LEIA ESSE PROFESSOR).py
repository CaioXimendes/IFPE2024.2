#Adição de alunos (solicitar apenas o nome)
nome_alunos = []
notas_1_alunos = []
notas_2_alunos = []
frequencia_alunos = []
opcao = 0
situacao = ""
carga_horaria_alunos = []
indice_lista_nome_alunos = 0
database_alunos_geral = ["",]
database_alunos_aprovados = ["",]
database_alunos_reprovados_falta = ["",]
database_alunos_reprovados_nota = ["",]

def calcular_situacao_aluno():
    """if (frequencia_alunos[indice_lista_nome_alunos]/ carga_horaria_alunos[indice_lista_nome_alunos]) < 0.75:
        situacao = "Reprovado(a) por falta"
        database_alunos_reprovados_falta.insert(indice_lista_nome_alunos,f"{indice_lista_nome_alunos+1} - Aluno(a): {nome_alunos[indice_lista_nome_alunos]}, Média: {(notas_1_alunos[indice_lista_nome_alunos]+notas_2_alunos[indice_lista_nome_alunos])/2}, frequência: {frequencia_alunos[indice_lista_nome_alunos]} aulas, Situação: {situacao}")
        database_alunos_geral.insert(indice_lista_nome_alunos,f"{indice_lista_nome_alunos+1} - Aluno(a): {nome_alunos[indice_lista_nome_alunos]}, Média: {(notas_1_alunos[indice_lista_nome_alunos]+notas_2_alunos[indice_lista_nome_alunos])/2}, frequência: {frequencia_alunos[indice_lista_nome_alunos]} aulas, Situação: {situacao}")
    elif ((notas_1_alunos[indice_lista_nome_alunos]+notas_2_alunos[indice_lista_nome_alunos])/2) < 7:
        situacao = "Reprovado(a) por nota"
        database_alunos_reprovados_nota.insert(indice_lista_nome_alunos,f"{indice_lista_nome_alunos+1} - Aluno(a): {nome_alunos[indice_lista_nome_alunos]}, Média: {(notas_1_alunos[indice_lista_nome_alunos]+notas_2_alunos[indice_lista_nome_alunos])/2}, frequência: {frequencia_alunos[indice_lista_nome_alunos]} aulas, Situação: {situacao}")
        database_alunos_geral.insert(indice_lista_nome_alunos,f"{indice_lista_nome_alunos+1} - Aluno(a): {nome_alunos[indice_lista_nome_alunos]}, Média: {(notas_1_alunos[indice_lista_nome_alunos]+notas_2_alunos[indice_lista_nome_alunos])/2}, frequência: {frequencia_alunos[indice_lista_nome_alunos]} aulas, Situação: {situacao}")"""
    if (frequencia_alunos[indice_lista_nome_alunos]/ carga_horaria_alunos[indice_lista_nome_alunos]) >= 0.75 and ((notas_1_alunos[indice_lista_nome_alunos]+notas_2_alunos[indice_lista_nome_alunos])/2) >= 7:
        situacao = "Aprovado(a)"
        database_alunos_aprovados.insert(indice_lista_nome_alunos,f"{indice_lista_nome_alunos+1} - Aluno(a): {nome_alunos[indice_lista_nome_alunos]}, Média: {(notas_1_alunos[indice_lista_nome_alunos]+notas_2_alunos[indice_lista_nome_alunos])/2}, frequência: {frequencia_alunos[indice_lista_nome_alunos]} aulas, Situação: {situacao}")
        database_alunos_geral.insert(indice_lista_nome_alunos,f"{indice_lista_nome_alunos+1} - Aluno(a): {nome_alunos[indice_lista_nome_alunos]}, Média: {(notas_1_alunos[indice_lista_nome_alunos]+notas_2_alunos[indice_lista_nome_alunos])/2}, frequência: {frequencia_alunos[indice_lista_nome_alunos]} aulas, Situação: {situacao}")
    elif (frequencia_alunos[indice_lista_nome_alunos]/ carga_horaria_alunos[indice_lista_nome_alunos]) < 0.75:
        situacao = "Reprovado(a) por falta"
        database_alunos_reprovados_falta.insert(indice_lista_nome_alunos,f"{indice_lista_nome_alunos+1} - Aluno(a): {nome_alunos[indice_lista_nome_alunos]}, Média: {(notas_1_alunos[indice_lista_nome_alunos]+notas_2_alunos[indice_lista_nome_alunos])/2}, frequência: {frequencia_alunos[indice_lista_nome_alunos]} aulas, Situação: {situacao}")
        database_alunos_geral.insert(indice_lista_nome_alunos,f"{indice_lista_nome_alunos+1} - Aluno(a): {nome_alunos[indice_lista_nome_alunos]}, Média: {(notas_1_alunos[indice_lista_nome_alunos]+notas_2_alunos[indice_lista_nome_alunos])/2}, frequência: {frequencia_alunos[indice_lista_nome_alunos]} aulas, Situação: {situacao}")
    else:
        situacao = "Reprovado(a) por nota"
        database_alunos_reprovados_nota.insert(indice_lista_nome_alunos,f"{indice_lista_nome_alunos+1} - Aluno(a): {nome_alunos[indice_lista_nome_alunos]}, Média: {(notas_1_alunos[indice_lista_nome_alunos]+notas_2_alunos[indice_lista_nome_alunos])/2}, frequência: {frequencia_alunos[indice_lista_nome_alunos]} aulas, Situação: {situacao}")
        database_alunos_geral.insert(indice_lista_nome_alunos,f"{indice_lista_nome_alunos+1} - Aluno(a): {nome_alunos[indice_lista_nome_alunos]}, Média: {(notas_1_alunos[indice_lista_nome_alunos]+notas_2_alunos[indice_lista_nome_alunos])/2}, frequência: {frequencia_alunos[indice_lista_nome_alunos]} aulas, Situação: {situacao}")
while opcao != 10:
    opcao = int(input("Seja bem vindo ao sistema academico: "
          "\n Menu de opções:"
          "\n 1-Adição de alunos"
          "\n 2-Edição de informações de nome do aluno"
          "\n 3-Remoção de aluno(a)"
          "\n 4-Adição de notas em aluno existente (no máximo 4 notas)"
          "\n 5-Adição de frequência em aluno existente"
          "\n 6-Impressão de relatório de situação dos alunos"
          "\n 7-Impressão de relatório de uma situação específica"
          "\n 10-Sair\n"))
    match opcao:
        case 1:
            nome_aluno = str(input("Informe o nome do aluno(a): "))
            nome_alunos.append(nome_aluno)
            indice_lista_nome_alunos = nome_alunos.index(nome_aluno)
        case 2:
            nome_aluno = str(input("Informe o nome do aluno(a) para edição de informações: "))
            indice_lista_nome_alunos = nome_alunos.index(nome_aluno)
            opcao_edicao = int(input(" 1 - Editar o nome do aluno(a):\n"
                                     " 2 - Editar notas:\n"
                                     " 3 - Editar frequência (Qtd. de aulas):\n"))
            match opcao_edicao:
                case 1:
                    nome_alunos[indice_lista_nome_alunos] = str(input("Informe o novo nome: "))
                case 2:
                    alterar_nota = int(input("Digite 1 - Primeira unidade"
                                                    "2 - Segunda unidade \n"))
                    match alterar_nota:
                        case 1:
                            notas_1_alunos[indice_lista_nome_alunos] = float(input("Informe a nova nota da 1ª unidade: \n"))
                        case 2:
                            notas_2_alunos[indice_lista_nome_alunos] = float(input("Informe a nova nota da 2ª unidade: \n"))
                case 3:
                    frequencia_alunos[indice_lista_nome_alunos] = int(input("Informe a nova frequência(Qtd aulas): \n"))
            database_alunos_geral[indice_lista_nome_alunos] = (f"{indice_lista_nome_alunos+1} - Aluno(a): {nome_alunos[indice_lista_nome_alunos]}, Média: {(notas_1_alunos[indice_lista_nome_alunos]+notas_2_alunos[indice_lista_nome_alunos])/2}, frequência: {frequencia_alunos[indice_lista_nome_alunos]} aulas, Situação: {situacao}")
            
        case 3:
            while True:
                try:
                    nome_aluno = str(input("Informe o nome do aluno(a) para remover: \n"))
                    if nome_aluno not in nome_alunos:
                        retorno = str(input("Não encontrei este aluno(a), deseja retornar ao menu? sim ou não"))
                        if retorno == "sim":
                            break
                    else:
                        indice_lista_nome_alunos = nome_alunos.index(nome_aluno)
                        nome_alunos.pop(indice_lista_nome_alunos)
                        notas_1_alunos.pop(indice_lista_nome_alunos)
                        notas_2_alunos.pop(indice_lista_nome_alunos)
                        frequencia_alunos.pop(indice_lista_nome_alunos)
                        database_alunos_aprovados.pop(indice_lista_nome_alunos)
                        database_alunos_reprovados_falta.pop(indice_lista_nome_alunos)
                        database_alunos_reprovados_nota.pop(indice_lista_nome_alunos)
                        database_alunos_geral.pop(indice_lista_nome_alunos)
                        break
                except:
                    None

        case 4:
            while True:
                try:
                    nome_aluno = str(input("Informe o nome do aluno(a) para adicionar as notas: \n"))
                    if nome_aluno not in nome_alunos:
                        print("Não encontrei este aluno(a)")
                    else:
                        indice_lista_nome_alunos = nome_alunos.index(nome_aluno)
                        nota_1_aluno = float (input(f"Informe a nota da primeira unidade de {nome_aluno}:\n"))
                        notas_1_alunos.insert(indice_lista_nome_alunos, nota_1_aluno)
                        nota_2_aluno = float (input(f"Informe a nota da segunda unidade de {nome_aluno}:\n"))
                        notas_2_alunos.insert(indice_lista_nome_alunos, nota_2_aluno)
                        break
                except:
                    None
        case 5:
            while True:
                try:
                    nome_aluno = str(input("Informe o nome do aluno(a) para adicionar a frequência: \n"))
                    if nome_aluno not in nome_alunos:
                        print("Não encontrei este aluno(a)")
                    else:
                        indice_lista_nome_alunos = nome_alunos.index(nome_aluno)
                        carga_horaria_aluno = float(input("Por gentileza, informe a carga horária da disciplina: "))
                        frequencia_aluno = float(input(f"Informe a frequência do aluno(a) {nome_aluno}: \n"))
                        frequencia_alunos.insert(indice_lista_nome_alunos , frequencia_aluno)
                        carga_horaria_alunos.insert(indice_lista_nome_alunos, carga_horaria_aluno)
                        break
                except:
                    None
            calcular_situacao_aluno()
        case 6:
            """def calcular_situacao_aluno():
                for x in nome_alunos:
                    if (frequencia_alunos[x]/ carga_horaria_alunos[x]) < 0.75:
                        situacao = "Reprovado(a) por falta"
                    elif ((notas_1_alunos[x]+notas_2_alunos[x])/2) < 7:
                        situacao = "Reprovado(a) por nota"
                    else:
                        situacao = "Aprovado(a)"
                    print(f"Aluno(a): {nome_alunos[x]}, Média: {(notas_1_alunos[x]+notas_2_alunos[x])/2}, frequência: {frequencia_alunos[x]} aulas, Situação: {situacao}")"""
            for p in database_alunos_geral:
                print(p+"\n")
            #print(f"Aluno(a): {nome_alunos[x]}, Média: {(notas_1_alunos[x]+notas_2_alunos[x])/2}, frequência: {frequencia_alunos[x]} aulas, Situação: {situacao}")
        case 7:
            filtro = int(input("1 - Para Aprovados: \n"
                               "2 - Para Reprovados por falta: \n"
                               "3 - Para Reprovados por nota: \n"))
            match filtro:
                case 1:
                    for x in database_alunos_aprovados:
                        print(x+"\n")
                case 2:
                    for y in database_alunos_reprovados_falta:
                        print(y+"\n")
                    #print(f"Aluno(a): {nome_alunos[x]}, Média: {(notas_1_alunos[x]+notas_2_alunos[x])/2}, frequência: {frequencia_alunos[x]} aulas, Situação: {situacao}")
                case 3:
                    for k in database_alunos_reprovados_nota:
                        print(k+"\n")
                    #print(f"Aluno(a): {nome_alunos[x]}, Média: {(notas_1_alunos[x]+notas_2_alunos[x])/2}, frequência: {frequencia_alunos[x]} aulas, Situação: {situacao}")
                        


                
    


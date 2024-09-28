#Adição de alunos (solicitar apenas o nome)
nome_alunos = {}
database_alunos = {}
database_alunos_temp = {}
informacoes_alunos_lista = [None]*3
opcao = 0

def calcular_situacao_aluno_nota():
    if informacoes_alunos_lista[1] >= 75 and informacoes_alunos_lista[0] >= 7:
        informacoes_alunos_lista[2] = "Aprovado"
    elif informacoes_alunos_lista[1] < 75:
        informacoes_alunos_lista[2] = "Reprovado por falta"
    else:
        informacoes_alunos_lista[2] = "Reprovado por nota"

def calcular_situacao_aluno():
    informacoes_alunos_lista[0]=((nota_1_aluno+nota_2_aluno)/2)
    informacoes_alunos_lista[1] = frequencia_aluno
    check_frequencia = frequencia_aluno/carga_horaria
    if check_frequencia >= 0.75 and informacoes_alunos_lista[0] >= 7:
        informacoes_alunos_lista[2] = "Aprovado"
    elif check_frequencia < 0.75:
        informacoes_alunos_lista[2] = "Reprovado por falta"
    else:
        informacoes_alunos_lista[2] = "Reprovado por nota"

def calcular_situacao_aluno_frequencia():
    check_frequencia = frequencia_aluno/carga_horaria
    if check_frequencia >= 0.75 and informacoes_alunos_lista[0] >= 7:
        informacoes_alunos_lista[2] = "Aprovado"
    elif check_frequencia < 0.75:
        informacoes_alunos_lista[2] = "Reprovado por falta"
    else:
        informacoes_alunos_lista[2] = "Reprovado por nota"
    
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
    informacoes_alunos_lista = [None]*3
    match opcao:
        case 1:
            nome_aluno = str(input("Informe o nome do aluno(a): "))
            #nome_alunos.append(nome_aluno)
            #indice_lista_nome_alunos = nome_alunos.index(nome_aluno)
            database_alunos.update({nome_aluno:None})
        case 2:
            while True:
                #alterar_nota = 0
                try:
                    nome_aluno = str(input("Informe o nome do aluno(a): \n"))
                    if nome_aluno not in database_alunos.keys():
                        print(f"Não encontrei {nome_aluno} no banco de dados!")
                    else:
                        editar = int(input(" 1 - Editar o nome do aluno(a):\n"
                                        " 2 - Editar notas:\n"
                                        " 3 - Editar frequência (Qtd. de aulas):\n"))
                        match editar:
                            case 1:
                                informacoes_alunos_lista = database_alunos.get(nome_aluno)
                                #database_alunos_temp.update({nome_aluno:informacoes_alunos_lista})
                                #print(informacoes_alunos_lista)
                                database_alunos.pop(nome_aluno)
                                #print(database_alunos)
                                nome_aluno = str(input("Informe o novo nome do aluno(a): \n"))
                                database_alunos.update({nome_aluno:informacoes_alunos_lista})
                                #print(database_alunos)
                                #database_alunos_temp.pop(nome_aluno)
                            case 2:
                                #alterar_nota = int(input("Alterar a 1ª unidade ou 2ª unidade? Responda 1 ou 2: \n"))
                                informacoes_alunos_lista = database_alunos.get(nome_aluno)
                                #database_alunos_temp.update({nome_aluno:informacoes_alunos_lista})
                                database_alunos.pop(nome_aluno)

                                nota_1_aluno = float(input(f"Digite a 1ª nota do aluno(a) {nome_aluno}: \n"))
                                nota_2_aluno = float(input(f"Digite a 2ª nota do aluno(a) {nome_aluno}: \n"))
                                informacoes_alunos_lista[0]=((nota_1_aluno+nota_2_aluno)/2)
                                #database_alunos_temp.pop(nome_aluno)
                                calcular_situacao_aluno_nota()
                                database_alunos.update({nome_aluno:(informacoes_alunos_lista)})
                            case 3:
                                informacoes_alunos_lista = database_alunos.get(nome_aluno)
                                #database_alunos_temp.update({nome_aluno:informacoes_alunos_lista})
                                database_alunos.pop(nome_aluno)
                                carga_horaria = float(input(f"Por gentileza, informe a carga horária da disciplina em que {nome_aluno} está matriculado: \n"))
                                informacoes_alunos_lista[1] = frequencia_aluno = float(input("Informe a frequência do aluno(a): \n"))
                                #print(informacoes_alunos_lista)
                                #print(database_alunos)
                                database_alunos.update({nome_aluno:informacoes_alunos_lista})
                                #print(database_alunos)
                                #database_alunos_temp.pop(nome_aluno)
                                calcular_situacao_aluno_frequencia()
                                #print(database_alunos)
                        break
                    informacoes_alunos_lista = [None]*3
                    
                except:
                    None
                
                """editar = int(input(" 1 - Editar o nome do aluno(a):\n"
                                        " 2 - Editar notas:\n"
                                        " 3 - Editar frequência (Qtd. de aulas):\n"))
                match editar:
                    case 1:
                        nome_aluno = str(input("Informe o novo nome do aluno(a): \n"))
                    case 2:
                        alterar_nota = int(input("Alterar a 1ª unidade ou 2ª unidade? Responda 1 ou 2: \n"))
                        match alterar_nota:
                            case 1:
                                nota_1_aluno = float(input("Digite a 1ª nota do aluno(a): \n"))
                            case 2:
                                nota_2_aluno = float(input("Digite a 2ª nota do aluno(a): \n"))
                        informacoes_alunos_lista[0]=((nota_1_aluno+nota_2_aluno)/2)
                        database_alunos.update({nome_aluno:(informacoes_alunos_lista[1])})
                    case 3:
                        carga_horaria = float(input("Por gentileza, informe a carga horária da disciplina: \n"))
                        informacoes_alunos_lista[2] = frequencia_aluno = float(input("Informe a frequência do aluno(a): \n"))
                        database_alunos.update({nome_aluno:informacoes_alunos_lista})
                calcular_situacao_aluno()
                break"""
                    
        case 3:
            while True:
                try:
                    nome_aluno = str(input("Informe o nome do aluno(a) para remover: \n"))
                    if nome_aluno not in database_alunos:
                        print(f"Não foi encontrado {nome_aluno} no banco de dados!")
                    else:
                        database_alunos.pop(nome_aluno)
                        break
                except:
                    None
            """nome_aluno = str(input("Informe o nome do aluno(a) para remover: \n"))
            database_alunos.pop(nome_aluno)"""
        case 4:
            while True:
                try:
                    nome_aluno = str(input("Informe o nome do aluno(a): \n"))
                    if nome_aluno not in database_alunos:
                        print(f"Não foi encontrado {nome_aluno} no banco de dados!")
                    else:
                        nota_1_aluno = float(input(f"Digite a 1ª nota do aluno(a) {nome_aluno}: \n"))
                        nota_2_aluno = float(input(f"Digite a 2ª nota do aluno(a) {nome_aluno}: \n"))
                        informacoes_alunos_lista[0]=((nota_1_aluno+nota_2_aluno)/2)
                        database_alunos.update({nome_aluno:(informacoes_alunos_lista[1])})
                        #print(database_alunos)
                        break
                except:
                    None
            """nome_aluno = str(input("Informe o nome do aluno(a): \n"))
            nota_1_aluno = float(input(f"Digite a 1ª nota do aluno(a) {nome_aluno}: \n"))
            nota_2_aluno = float(input(f"Digite a 2ª nota do aluno(a) {nome_aluno}: \n"))
            informacoes_alunos_lista[0]=((nota_1_aluno+nota_2_aluno)/2)

            database_alunos.update({nome_aluno:(informacoes_alunos_lista[1])})
            #print(database_alunos)"""
        case 5:
            while True:
                try:
                    nome_aluno = str(input("Informe o nome do aluno(a): \n"))
                    if nome_aluno not in database_alunos:
                        print(f"Não foi encontrado {nome_aluno} no banco de dados!")
                    else:
                        carga_horaria = float(input("Por gentileza, informe a carga horária da disciplina: \n"))
                        frequencia_aluno = float(input(f"Informe a frequência do aluno(a) {nome_aluno}: \n"))
                        calcular_situacao_aluno()
                        database_alunos.update({nome_aluno:informacoes_alunos_lista})
                        #print(database_alunos)
                        informacoes_alunos_lista = [None]*3
                        break
                except:
                    None
            """nome_aluno = str(input("Informe o nome do aluno(a): \n"))
            carga_horaria = float(input("Por gentileza, informe a carga horária da disciplina: \n"))
            frequencia_aluno = float(input(f"Informe a frequência do aluno(a) {nome_aluno}: \n"))
            calcular_situacao_aluno()
            database_alunos.update({nome_aluno:informacoes_alunos_lista})
            #print(database_alunos)
            informacoes_alunos_lista = [None]*3"""
            
        case 6:
            #calcular_situacao_aluno()
            for x, elemento in enumerate(database_alunos.keys()):
                print(f" {x+1} - Aluno {elemento}, Nota: {database_alunos[elemento][0]}, Frequência: {database_alunos[elemento][1]}, Situação: {database_alunos[elemento][2]}")
        case 7:
            filtro = int(input("1 - Para Aprovados: \n"
                               "2 - Para Reprovados por falta: \n"
                               "3 - Para Reprovados por nota: \n"))
            match filtro:
                case 1:
                    for x, elemento in enumerate(database_alunos.keys()):
                        if database_alunos[elemento][2] == "Aprovado":
                            print(f" {x+1} - Aluno {elemento}, Nota: {database_alunos[elemento][0]} ,Frequência: {database_alunos[elemento][1]}, Situação: {database_alunos[elemento][2]}")
                case 2:
                    for x, elemento in enumerate(database_alunos.keys()):
                        if database_alunos[elemento][2] == "Reprovado por falta":
                            print(f" {x+1} - Aluno {elemento}, Nota: {database_alunos[elemento][0]} ,Frequência: {database_alunos[elemento][1]}, Situação: {database_alunos[elemento][2]}")
                case 3:
                    for x, elemento in enumerate(database_alunos.keys()):
                        if database_alunos[elemento][2] == "Reprovado por nota":
                            print(f" {x+1} - Aluno {elemento}, Nota: {database_alunos[elemento][0]} ,Frequência: {database_alunos[elemento][1]}, Situação: {database_alunos[elemento][2]}")
                
        case 10:
            print("parabens para quem entendeu esse codigo 💀💀💀💀")
            break
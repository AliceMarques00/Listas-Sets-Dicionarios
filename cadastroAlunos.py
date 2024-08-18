alunos = {}

while True:
    print("\nMenu:")
    print("1. Cadastrar um aluno")
    print("2. Consultar se um aluno já está cadastrado")
    print("3. Remover um aluno")
    print("4. Cadastrar uma disciplina cursada")
    print("5. Verificar se um aluno já cursou uma disciplina")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cpf = input("Digite o CPF do aluno: ")
        if cpf in alunos:
            print("Aluno já cadastrado!")
        else:
            nome = input("Digite o nome do aluno: ")
            alunos[cpf] = {"nome": nome, "disciplinas": []}
            print("Aluno cadastrado com sucesso.")

    elif opcao == "2":
        cpf = input("Digite o CPF do aluno: ")
        if cpf in alunos:
            print("Aluno encontrado: Nome:", alunos[cpf]["nome"])
        else:
            print("Aluno não encontrado.")

    elif opcao == "3":
        cpf = input("Digite o CPF do aluno: ")
        if cpf in alunos:
            del alunos[cpf]
            print("Aluno removido com sucesso.")
        else:
            print("Aluno não encontrado.")

    elif opcao == "4":
        cpf = input("Digite o CPF do aluno: ")
        if cpf in alunos:
            codigo = input("Digite o código da disciplina: ")
            nome_disciplina = input("Digite o nome da disciplina: ")
            semestre = input("Digite o semestre que a disciplina foi cursada: ")

            # Adicionar a disciplina ao aluno
            alunos[cpf]["disciplinas"].append({
                "codigo": codigo,
                "nome": nome_disciplina,
                "semestre": semestre
            })
            print("Disciplina cadastrada com sucesso.")
        else:
            print("Aluno não encontrado.")

    elif opcao == "5":
        cpf = input("Digite o CPF do aluno: ")
        if cpf in alunos:
            codigo = input("Digite o código da disciplina: ")
            cursou = False
            for disciplina in alunos[cpf]["disciplinas"]:
                if disciplina["codigo"] == codigo:
                    cursou = True
                    break
            if cursou:
                print("O aluno já cursou essa disciplina.")
            else:
                print("O aluno não cursou essa disciplina.")
        else:
            print("Aluno não encontrado.")

    elif opcao == "6":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")

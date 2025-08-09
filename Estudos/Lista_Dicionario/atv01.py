print("Gerenciador de Tarefas")
tarefas = []

while True:
    print("\nOpções:")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Remover")
    print("4 - Sair")

    opc = int(input("Selecione uma opção: "))

    if opc == 1:
        tarefas.append(input("Digite sua tarefa: "))
        print("Tarefa adicionada.")
        input("Aperte ENTER para continuar.")

    elif opc == 2:
        if tarefas:
            i = 1
            for n in tarefas:
                print(f"{i} - {n}")
                i += 1
        else:
            print("Nenhuma tarefa cadastrada.")
        input("Aperte ENTER para continuar.")

    elif opc == 3:
        print("Ações:")
        print("1 - Específico")
        print("2 - Tudo")
        acao = int(input("Selecione uma ação: "))

        if acao == 1:
            remove = int(input("Selecione o índice: "))
            if 1 <= remove <= len(tarefas):
                tarefas.pop(remove - 1)
                print("Tarefa removida.")
            else:
                print("Índice inválido.")
            input("Aperte ENTER para continuar.")
        elif acao == 2:
            tarefas.clear()
            print("Lista excluída.")
            input("Aperte ENTER para continuar.")

    elif opc == 4:
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida.")
        input("Aperte ENTER para continuar.")

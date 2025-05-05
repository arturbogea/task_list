def adicionar_tarefa(lista):
    tarefa = input("Inclua a sua tarefa: ").strip().lower()
    if tarefa == "":
        print("⚠️ Não pode ser vazio. Digite uma tarefa.")
    else:
        lista.append(tarefa)
        print("✅ Tarefa incluída com sucesso!")
    return lista  # retorna a lista atualizada


def listar_tarefas(lista):
    if lista:
        print("\n📋 Suas tarefas:")
        print("\n".join(f"* {item}" for item in lista))
    else:
        print("📭 Sua lista de tarefas está vazia.")


def remover_tarefa(lista):
    if not lista:
        print("📭 Não há tarefas para remover.")
    else:
        remover = input("Digite o nome da tarefa que deseja remover: ").strip().lower()
        if remover == "":
            print("⚠️ Não pode ser vazio. Digite uma tarefa.")
        elif remover in lista:
            lista.remove(remover)
            print("🗑️ Tarefa removida com sucesso!")
        else:
            print("❌ Tarefa não encontrada na lista.")
    return lista  # retorna a lista (atualizada ou igual)


def gerenciador_tarefas():
    nome = input("Por gentileza, informe o seu nome: ")

    print(f"""
    Olá {nome}, seja bem-vindo(a) ao seu gerenciador de tarefas.
    Aqui você poderá montar e organizar a sua lista de tarefas.
    """)

    lista_tarefas = []

    while True:
        opcao = input("""
Digite a opção que deseja realizar:
1 - Adicionar tarefa
2 - Listar tarefas
3 - Remover tarefa
4 - Sair
Opção: """)

        if opcao == "1":
            lista_tarefas = adicionar_tarefa(lista_tarefas)
        elif opcao == "2":
            listar_tarefas(lista_tarefas)
        elif opcao == "3":
            lista_tarefas = remover_tarefa(lista_tarefas)
        elif opcao == "4":
            print("Sistema encerrando...")
            break
        else:
            print("❌ Digite uma opção válida.")

    print(f"\nObrigado, {nome}, por usar o nosso sistema de tarefas! 👋")



gerenciador_tarefas()

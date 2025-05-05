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
            tarefa = input("Inclua a sua tarefa: ").strip().lower()
            if tarefa == "":
                print("⚠️ Não pode ser vazio. Digite uma tarefa.")
            else:
                lista_tarefas.append(tarefa)
                print("✅ Tarefa incluída com sucesso!")

        elif opcao == "2":
            if lista_tarefas:
                print("\n📋 Suas tarefas:")
                print("\n".join(f"* {item}" for item in lista_tarefas))
            else:
                print("📭 Sua lista de tarefas está vazia.")

        elif opcao == "3":
            if not lista_tarefas:
                print("📭 Não há tarefas para remover.")
            else:
                remover_tarefa = input("Digite o nome da tarefa que deseja remover: ").strip().lower()
                if remover_tarefa == "":
                    print("⚠️ Não pode ser vazio. Digite uma tarefa.")
                elif remover_tarefa in lista_tarefas:
                    lista_tarefas.remove(remover_tarefa)
                    print("🗑️ Tarefa removida com sucesso!")
                else:
                    print("❌ Tarefa não encontrada na lista.")

        elif opcao == "4":
            print("Sistema encerrando...")
            break

        else:
            print("❌ Digite uma opção válida.")

    print(f"\nObrigado, {nome}, por usar o nosso sistema de tarefas! 👋")


# Chamada da função principal
gerenciador_tarefas()
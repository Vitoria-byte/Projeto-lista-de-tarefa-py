# Lista de tarefas
tarefas = []

def adicionar_tarefa():
    tarefa = {
        "Nome": input("Nome da tarefa: "),
        "Categoria": input("Coloque a categoria: "),
        "Prioridade": input("Nível da prioridade (Alta, Média, Baixa): "),
        "Status": "Pendente"
    }
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!\n")

# Função que lista todas as tarefas
def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.\n")
    else:
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa['Nome']} | Categoria: {tarefa['Categoria']} | "
                  f"Prioridade: {tarefa['Prioridade']} | Status: {tarefa['Status']}")
        print()

# Função para marcar tarefas como concluídas
def concluir_tarefa():
    listar_tarefas()
    if tarefas:
        indice = int(input("Digite o número da tarefa para marcar como concluída: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice]["Status"] = "Concluída"
            print("Tarefa concluída com sucesso!\n")
        else:
            print("Número inválido!\n")

# Função para filtrar por prioridade
def filtrar_por_prioridade():
    prioridade = input("Digite a prioridade (Alta, Média, Baixa): ")
    filtradas = [t for t in tarefas if t["Prioridade"].lower() == prioridade.lower()]
    if filtradas:
        for t in filtradas:
            print(f"- {t['Nome']} | Prioridade: {t['Prioridade']} | Status: {t['Status']}")
    else:
        print("Nenhuma tarefa encontrada com essa prioridade.\n")
    print()

# Função para filtrar por categoria
def filtrar_por_categoria():
    categoria = input("Digite a categoria: ")
    filtradas = [t for t in tarefas if t["Categoria"].lower() == categoria.lower()]
    if filtradas:
        for t in filtradas:
            print(f"- {t['Nome']} | Prioridade: {t['Prioridade']} | Status: {t['Status']}")
    else:
        print("Nenhuma tarefa encontrada nessa categoria.\n")
    print()

# Menu principal
while True:
    print(">>>>> MENU DE OPÇÕES <<<<<")
    print("1. Adicionar tarefa")
    print("2. Ver todas as tarefas")
    print("3. Marcar uma tarefa como concluída")
    print("4. Filtrar tarefas por prioridade")
    print("5. Filtrar tarefas por categoria")
    print("0. SAIR")

    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        adicionar_tarefa()
    elif escolha == "2":
        listar_tarefas()
    elif escolha == "3":
        concluir_tarefa()
    elif escolha == "4":
        filtrar_por_prioridade()
    elif escolha == "5":
        filtrar_por_categoria()
    elif escolha == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida! Tente novamente.\n")
           

           

     

      



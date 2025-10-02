#Tarefas diarias:
tarefas = []

def adicionar_tarefas():
    tarefa = {
        "Nome": input("Nome da tarefa?"),
        "Categoria": input("Qual a categoria?"),
        "Prioridade": input("Nivel da prioridade?"),
        "Status": "Pendente"
    }
    tarefas.append(tarefa)
   

adicionar_tarefas()
print(tarefas)
#Menu de interação:
escolha = []
while True:
      input("MENU DE OPÇÕES:") 
      input("1.Adicionar tarefa:") 
      input("2.Ver todas as taredas")
      input("3.Marcar uma tarefa como concluida")
      input("4.Filtrar tarefas por prioridade")
      input("5.Filtrar tarefa por categoria")
      input("0.Sair")

      escolha = input("Escolha uma opção:") 

      if escolha =="1":
           adicionar_tarefas()
      elif escolha =="2":
           tarefas()
      elif escolha =="3":
           indice = int(input("Número de tarefas para concluir"))-1
           if 0 
           

           

     

      


listTasks = []

while True:

   command = input("Insira o comando (add, list, done, exit): ").lower()

   if (command == "add"):

      taskTitle = input("Diga o título da tarefa: ")
      taskPriority = int(input("Diga a prioridade da tarefa (1 - 5): "))
      taskStatus = "aberta"
      tasks = {"titulo": taskTitle,
               "prioridade": taskPriority,
               "status": taskStatus }
      listTasks.append(tasks)
      continue

   if (command == "done"):

      taskTitle = input("Diga o título da tarefa: ")
      task = next((item for item in listTasks if item["titulo"] == taskTitle), None)

      if (not task):
         print("Tarefa não encontrada")
      else:
         print("Tarefa concluída")
         task["status"] = "concluida"
      
   if (command == "list"):
      taskFilter = input("Insira um filtro de tarefas se preferir (Aberta / Concluida): ").lower()

      sortedTasks = sorted(listTasks, key=lambda item: item["prioridade"]) 

      if (taskFilter == "aberta" or taskFilter == "concluida"):
         sortedTasks = list(filter(lambda item: item["status"] == taskFilter, sortedTasks))
      else:
         print("Filtro não usado")
      
      print(sortedTasks)

   if (command == "exit"):
      break
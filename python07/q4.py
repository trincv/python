dictionary = {}

while True:

   name = input("Insira o nome do aluno: ")

   if name == "FIM":
      break

   grade = list(map(float, input("Insira as tres notas do aluno separados por espaço: ").split()))

   media = sum(grade) / len(grade)

   if media >= 7:
      status = "APROVADO"
   elif media < 7 and media >= 5:
      status = "Recuperação"
   else:
      status = "Reprovado"  
   
   dictionary[name] = {
      "notas" : list(grade),
      "media" : round(media,2),
      "status" : status
   }

for name, info in dictionary.items():
   print(f"\nNome: {name}")
   print(f"Notas: {info["notas"]}")
   print(f"Media: {info["media"]}")
   print(f"Status: {info["status"]}")

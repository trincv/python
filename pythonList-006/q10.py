import math

repetition = 0

while True:

   number = int(input("Insira um número pasa saber sua raiz: "))

   if (number < 0):
      print("Número negativo é inválido")
      continue

   print(f"A raiz equivale a: {math.sqrt(number)}")

   repetition += 1

   if (repetition == 10):
      break


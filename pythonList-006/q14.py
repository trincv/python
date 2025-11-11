fuelType = input("Insira o tipo de combustível (A - álcool, G - gasolina): ")
fuelQtd = float(input("Insira a quantidade em L e combustível: "))


if (fuelType == "A"):
   if (fuelQtd <= 20):
      totalCost = (2.5 - 2.5 * 0.03) * fuelQtd
   else:
      totalCost = (2.5 - 2.5 * 0.05) * fuelQtd

elif (fuelType == "G"):
   if (fuelQtd <= 20):
      totalCost = (1.9 - 1.9 * 0.04) * fuelQtd
   else:
      totalCost = (1.9- 1.9 * 0.06) * fuelQtd

else:
   print("Combustível não reconhecido")
   exit()

print(f"O valor a ser pago pelo cliente equivale a: {totalCost}")
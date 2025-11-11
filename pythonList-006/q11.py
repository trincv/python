
fishWeight = float(input("Insira o peso dos peixes pescados: "))

excess = fishWeight - 50

fineCost = 0

if (excess > 0):
   fineCost = excess * 4

print(f"Houve um excesso de {round(excess, 2)} quilos, portanto a multa a ser paga equivale a {round(fineCost, 2)}")




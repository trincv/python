
paintArea = float(input("Insira a área em metros quadrados a ser pintada: "))
paintArea += paintArea * 0.1
qtdPaint = 0
costBiggerCans = 0
costSmallerCans = 0

if (paintArea % 6 == 0):
   qtdPaint = paintArea / 6
else:
   qtdPaint = (paintArea // 6) + 1

if (qtdPaint % 18 == 0):
   costBiggerCans = (qtdPaint / 18) * 80
else:
   costBiggerCans = ((qtdPaint // 18) + 1) * 80

if (qtdPaint % 3.6 == 0):
   costSmallerCans = (qtdPaint / 3.6) * 25
else:
   costSmallerCans = ((qtdPaint // 3.6) + 1) * 25

areaToPaint = paintArea
qtdBiggerCans = 0
qtdSmallerCans = 0
areaPaintedByBigger = 18 * 6
areaPaintedBySmaller = 3.6 * 6

while (areaToPaint > 0):
   if ((areaToPaint - areaPaintedByBigger) >= 0):
      areaToPaint -= areaPaintedByBigger
      qtdBiggerCans += 1
      continue

   areaToPaint -= areaPaintedBySmaller
   qtdSmallerCans += 1

cheaperCost = qtdBiggerCans * 80 + qtdSmallerCans * 25

print(paintArea)
print(qtdPaint)
print(f"O custo das grandes seria: {costBiggerCans}")
print(f"O custo das pequenas seria: {costSmallerCans}")
print(f"O custo mais barato seria o de: {cheaperCost} reais, sendo {qtdBiggerCans} latas grandes de 18L e {qtdSmallerCans} latas menores de 3.6L")



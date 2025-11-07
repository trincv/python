countryA = 5000000
countryB = 7000000

natalityA = 0.03
natalityB = 0.02

anos = 0
while (countryA < countryB):
   anos += 1
   countryA += (countryA * natalityA)
   countryB += (countryB * natalityB) 


print(f"Levou {anos} anos: {countryA:.3} > {countryB:.3}")
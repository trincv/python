heightChico = 1.5
heightJuca = 1.1

growthChico = 0.02
growthJuca = 0.03

anos = 0

while (heightJuca < heightChico):
   anos += 1
   heightJuca = (heightJuca + growthJuca)
   heightChico = (heightChico + growthChico) 


print(f"Levou {anos} anos, Juca: {heightJuca:.3} m > Chico: {heightChico:.3} m")
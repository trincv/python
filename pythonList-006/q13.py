typeOfMeat = input("Qual a carne para a compra?(file duplo, Alcatra, Picanha) ").lower()
qtdMeat = float(input("Qual a quantidade em kg desejada? "))
storeCard = input("Pagamento será realizado com o cartão da loja? (sim ou não) ").lower()
totalCost = 0

if (typeOfMeat == "file duplo"):
   if (qtdMeat <= 5):
      totalCost = qtdMeat * 4.9
   else:
      totalCost = qtdMeat * 5.8

elif (typeOfMeat == "alcatra"):
   if (qtdMeat <= 5):
      totalCost = qtdMeat * 5.9
   else:
      totalCost = qtdMeat * 6.8

elif (typeOfMeat == "picanha"):
   if (qtdMeat <= 5):
      totalCost = qtdMeat * 6.9
   else:
      totalCost = qtdMeat * 7.8
else:
   print("Erro: Tipo de carne não reconhecido.")
   exit()

finalCost = totalCost

if (storeCard == "sim"):
   finalCost -= totalCost * 0.05
   paymentMethod = "Cartão da loja"
else:
   paymentMethod = "Outro cartão / Dinheiro"

order = {"Tipo": typeOfMeat, 
         "quantidade": qtdMeat, 
         "Preço total": totalCost, 
         "Tipo pagamento": paymentMethod,
         "Desconto total": totalCost - finalCost,
         "Preço final": finalCost}

print(order)

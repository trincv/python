consumption = {}
totalConsume = 0
consumeTypes1And2 = 0
qtdConsumersType1And2 = 0

while True:

   consumerType = int(input("Insira o tipo de consumidor: "))

   if (consumerType == 0):
      break

   consumerNumber = int(input("Insira o número do consumidor: "))
   consumerQuantity = int(input("Insira a quantidade de kWh consumido: "))

   consumerBill = 0.0

   if (consumerType == 1):
      consumerBill = consumerQuantity * 0.3
   elif (consumerType == 2):
      consumerBill = consumerQuantity * 0.5
   else:
      consumerBill = consumerQuantity * 0.7

   consumption[consumerNumber] = {"Tipo": consumerType,
                                  "Quantidade kWh": consumerQuantity,
                                  "Custo": consumerBill}

for consume in consumption.values():
   totalConsume += consume["Quantidade kWh"]

for consume in consumption.values():
   if (consume["Tipo"] == 1 or consume["Tipo"] == 2):
      consumeTypes1And2 += consume["Quantidade kWh"]
      qtdConsumersType1And2 += 1

print(f"custo de cada consumidor: {consumption}\n")
print(f"O cosnumo total de energia de todos os consumidores: {totalConsume}\n")
print(f"A média de consumo de energia dos tipos 1 e 2 foi: {round((consumeTypes1And2 / qtdConsumersType1And2), 2)}")
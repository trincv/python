
dictionary = {}

while True:

   product = input("Insira o produto: ")
   price = float(input("Insira o preço do produto: "))

   if price == 0:
      break
   
   dictionary[product] = price

expensiveProduct = max(dictionary, key=dictionary.get)
cheaperProduct = min(dictionary, key=dictionary.get)
averagePrice = sum(dictionary.values()) / len(dictionary)

aboveAverage = {p: price for p, price in dictionary.items() if price > averagePrice}


print(f"Produto mais caro: {expensiveProduct} de valor {dictionary[expensiveProduct]}")
print(f"Produto mais barato: {cheaperProduct} de valor {dictionary[cheaperProduct]}")
print(f"Média dos preços: {averagePrice}")
print(f"Produtos com valor acima da média:\n{aboveAverage}")
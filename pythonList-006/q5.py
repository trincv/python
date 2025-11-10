stock = {"teclado": 12, "mouse": 5, "monitor": 2}
pending = []


while (True):

   product = input("Insira o produto: ")

   if (product == "FIM"):
      break

   if (product not in stock.keys()):
      print("Produto não existente no estoque")
      continue

   quantity = int(input("Insira a quantidade desejada do produto: "))

   order = [{"produto": product}, {"qtd": quantity}]

   if (quantity > stock.get(product)):
      print("Quantidade acima do estocado, pedido em lista de pendentes")
      pending.append(order)
      continue
   
   stock[product] -= quantity
   print("Pedido concluído")

print("\n")

print(f"Estoque atualizado: {stock}")
print(f"Pedidos pendentes: {pending}")


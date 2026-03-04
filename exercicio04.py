produto = input("Nome do produto: ")
preco_unitario = float(input("Preço unitário: "))
quantidade = int(input("Quantidade comprada: "))

total = preco_unitario * quantidade

print("Você comprou", quantidade, "unidades de", produto)
print("Total a pagar: R$", total)
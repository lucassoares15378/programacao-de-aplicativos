compras = []
produtos = input("Digite seu produto: ")

while produtos != "fim":
    compras = compras + [produtos]
    produtos = input("Digite o nome de um produto (ou 'fim' para finalizar a compra): ")

print("Lista de produtos: ")
for item in compras:
    print(f"{item}")
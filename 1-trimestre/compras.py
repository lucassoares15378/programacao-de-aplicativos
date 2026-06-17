compras = []
item = ""

while item != "fim":
    item = input("Digite qual o item (ou fim para encerrar) ")

    if item != "fim":
        compras.append(item)

for produto in compras:
    print(f" {produto}")
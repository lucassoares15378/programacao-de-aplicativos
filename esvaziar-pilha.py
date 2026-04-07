objetos = ["lapis", "borracha", "caneta", "apontador"]
print(f"sua lista original {objetos}")

while objetos:
    removidos = objetos.pop()
    print(f"Removemos {removidos}")

print("Sua lista está vazia!")
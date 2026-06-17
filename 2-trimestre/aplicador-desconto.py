def aplicar_promocao(lista_precos):
    return [preco * 0.85 if preco > 100 else preco for preco in lista_precos]
compras = [150.0, 80.0, 200.0, 50.0]
lista_atualizada = aplicar_promocao(compras)
print(f"Lista original: {compras}")
print(f"Lista atualizada: {lista_atualizada}")

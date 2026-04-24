def esta_na_lista(lista_nomes, nome_busca):
    for item in lista_nomes:
        if item == nome_busca:
            return "Encontrado!"

    return "Não disponível"

ferramentas = ["Martelo", "Chave de fenda", "Alicate", "Trena"]

busca_1 = "Alicate"
resultado_1 = esta_na_lista(ferramentas, busca_1)
print(f"Busca por '{busca_1}': {resultado_1}")

busca_2 = "Furadeira"
resultado_2 = esta_na_lista(ferramentas, busca_2)
print(f"Busca por '{busca_2}': {resultado_2}")
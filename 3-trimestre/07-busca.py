palavras = ["abacaxi", "banana", "casa", "dado"]

def buscar_palavras(palavras, valor): 
    inicio = 0
    fim = len(palavras) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if palavras[meio] == valor:
            return meio
        elif palavras[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1
print(buscar_palavras(palavras, "casa"))
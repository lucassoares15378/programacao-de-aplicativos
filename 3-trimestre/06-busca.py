def busca_binaria(vetor, valor):
    inicio = 0
    fim = len(vetor) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if vetor[meio] == valor:
            return meio
        elif vetor[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1


vetor = [2, 5, 8, 12, 16, 23, 38, 45, 56]

print(busca_binaria(vetor, 23)) 
print(busca_binaria(vetor, 10))  

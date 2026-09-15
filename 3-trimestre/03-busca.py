def maior(lista):
    maior = lista[0]
    posicao = 0
    for n in range(len(lista)):
        if lista[n] > maior:
            maior = lista[n]
            posicao = n
    return maior, posicao 
lista = [10, 25, 7, 50, 30]
print(maior(lista))

def posicoes(lista, numero):
    primeira = -1
    ultima = -1

    for n in range(len(lista)):
        if lista[n] == numero:

            if primeira == -1:
                primeira = n

            ultima = n

    return primeira, ultima


lista = [2, 5, 7, 5, 9, 5, 10]

print(posicoes(lista, 5))

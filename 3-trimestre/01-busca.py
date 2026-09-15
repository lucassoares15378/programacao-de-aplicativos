def buscar(lista, numeros):
    for n in range(10):
        if lista[n] == numeros:
            return n
    return -1
lista = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(buscar(lista, 70))
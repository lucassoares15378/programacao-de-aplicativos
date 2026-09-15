def buscar(lista, numero):
    quantidade = 0
    
    for n in lista:
        if n == numero:
            quantidade = quantidade + 1
    return quantidade
lista = [5, 2, 5, 8, 5, 3, 5]
print(buscar(lista, 5))


numeros = list(range(1, 101)) #cria a lista de 1 á 101

# BUSCA SEQUENCIAL

comparacoes = 0 #cria um contador do 0

for numero in numeros: #percorre a lista numeros, numero por numero
    comparacoes = comparacoes + 1 #aqui começa a contar e adiciona no contador 1

    if numero == 95: #se for igual a 95
        print("Busca Sequencial") 
        print("Número encontrado:", numero)
        print("Comparações:", comparacoes) #mostra quantas comparações foram necessaárias
        break #para a procura


# BUSCA BINÁRIA

inicio = 0 #começo
fim = len(numeros) - 1 #final
comparacoes = 0 #começa a contagem em 0

while inicio <= fim: #enquanto houver numeros, continue procurando
    meio = (inicio + fim) // 2 #enconta o meio do que estamos procurando
    comparacoes = comparacoes + 1 #aumenta o contador depois da verificação

    if numeros[meio] == 95: #se o número chegar em 95 trava
        print("Busca Binária") 
        print("Número encontrado:", numeros[meio])
        print("Comparações:", comparacoes)
        break

    elif numeros[meio] < 95: #o número do meio é menor que o número que estamos procurando, se for começa a procurar antes
        inicio = meio + 1

    else:     #o numero do meio é maior que estamos procurando, se for começa a procurar depois
        fim = meio - 1

cidades = ["São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte"]
tarefa = input("Digite uma cidade: ")

if tarefa in cidades:
    posicao = cidades.index(tarefa)
    print(f"A cidade {tarefa} está na posição {posicao}.")
else:
    print(f"A {tarefa} não foi encontrada")

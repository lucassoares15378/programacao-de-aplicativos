nomes = ["lucas", "gustao", "Maria", "belly"]

antigo = input("Qual nome você quer mudar? ")
novo = input("Qual o novo nome? ")

for i in range(len(nomes)):
    if nomes[antigo] == nome_antigo:
        nomes[novo] = nome_novo

print("Lista atualizada:", nomes)

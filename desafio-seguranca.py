autorizados = ["alice", "bob", "carlos"]
nome = input("Digite o nome do pesquisador: ")

if nome in autorizados:
    indice = autorizados.index(nome)
    print(f"Acesso Permitido! O pesquisador {nome} está na posição {indice}.")

    remover = input("quer remover esse nome da lista? (s/n)")

    if remover == "s":
        autorizados.remove(nome)
        print(f"Lista atualizada {autorizados}")

else:
    print(f"Acesso Negado, pesquisador {nome} não encontrado na lista")
    adicionar = input("Deseeja cadastrar o novo pesquissador? (s/n)")
    if adicionar == "s":
        autorizados.append(nome)
        print(f"Lista atual {autorizados}")
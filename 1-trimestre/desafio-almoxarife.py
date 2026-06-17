banco_dados = []
while True:
    print("-----Menu do sistema-----")
    print("1- Adicionar item")
    print("2- Listar e sair")
    print("3- Sair")
    opção = (input("O que você deseja fazer? "))

    if opção == "1":
        nome = input("Digite um nome: ")
        banco_dados.append(nome)
        print(f"Banco de dados atualizado {banco_dados}")
    
    elif opção == "2":
        print(f"Banco de dados {banco_dados}")
    
    elif opção == "3":
        print("saindo!")
        rodando = False
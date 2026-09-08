lista_clientes = []

def criar():
    id_cliente = int(input("Digite o ID do cliente: "))
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email: ")
    cliente = {"id": id_cliente, "nome": nome, "email": email}
    lista_clientes.append(cliente)
    print("Cliente adicionado!")

def listar():
    if len(lista_clientes) == 0:
        print("Nenhum cliente encontrado.")
    else:
        for cliente in lista_clientes:
            print(f"ID: {cliente['id']} - Nome: {cliente['nome']} - Email: {cliente['email']}")

def atualizar():
    id_busca = int(input("Digite o ID do cliente que quer alterar: "))
    for cliente in lista_clientes:
        if cliente['id'] == id_busca:
            cliente['nome'] = input("Digite o novo nome: ")
            cliente['email'] = input("Digite o novo email: ")
            print("Cliente alterado!")
            return
    print("Cliente nao encontrado.")

def excluir():
    id_busca = int(input("Digite o ID do cliente que quer excluir: "))
    for cliente in lista_clientes:
        if cliente['id'] == id_busca:
            lista_clientes.remove(cliente)
            print("Cliente excluido!")
            return
    print("Cliente nao encontrado.")

def menu_clientes():
    opcao = 0
    while opcao != 5:
        print("\n--- MENU CLIENTES ---")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Excluir")
        print("5. Voltar")
        opcao = int(input("Opcao: "))
        
        if opcao == 1:
            criar()
        elif opcao == 2:
            listar()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            excluir()




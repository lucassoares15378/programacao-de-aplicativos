lista_produtos = []

def criar():
    id_produto = int(input("Digite o ID do produto: "))
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preco: "))
    produto = {"id": id_produto, "nome": nome, "preco": preco}
    lista_produtos.append(produto)
    print("Produto adicionado!")

def listar():
    if len(lista_produtos) == 0:
        print("Nenhum produto encontrado.")
    else:
        for produto in lista_produtos:
            print(f"ID: {produto['id']} - Nome: {produto['nome']} - Preco: R${produto['preco']:.2f}")

def atualizar():
    id_busca = int(input("Digite o ID do produto que quer alterar: "))
    for produto in lista_produtos:
        if produto['id'] == id_busca:
            produto['nome'] = input("Digite o novo nome: ")
            produto['preco'] = float(input("Digite o novo preco: "))
            print("Produto alterado!")
            return
    print("Produto nao encontrado.")

def excluir():
    id_busca = int(input("Digite o ID do produto que quer excluir: "))
    for produto in lista_produtos:
        if produto['id'] == id_busca:
            lista_produtos.remove(produto)
            print("Produto excluido!")
            return
    print("Produto nao encontrado.")

def menu_produtos():
    opcao = 0
    while opcao != 5:
        print("\n--- MENU PRODUTOS ---")
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

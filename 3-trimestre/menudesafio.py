import tabela1
import tabela2

def menu():
    opcao = 0
    while opcao != 3:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Produtos")
        print("2. Clientes")
        print("3. Sair")
        opcao = int(input("Escolha uma opcao: "))
        
        if opcao == 1:
            tabela1.menu_produtos()
        elif opcao == 2:
            tabela2.menu_clientes()
        elif opcao == 3:
            print("Saindo...")

menu()

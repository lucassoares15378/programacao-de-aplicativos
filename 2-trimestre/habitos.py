def criar_arquivo():
    open('habitos.txt', 'w').close()

def criar():
    habitos = input("Quais são seus habitos: ")
    with open('habitos.txt', 'a') as f:
        f.write(habitos + '\n')
    print("Habito cadastrado!")


def ler():
    with open('habitos.txt', 'r') as f:
        habitos = f.readlines()
        
        i = 0
        for habito in habitos:
            print(f"{i} - {habito.strip()}") 
            i += 1  

def atualizar():
    ler() 
    idx = int(input("Digite o ID do habito que você deseja alterar: "))
    novo_habito = input("Novo habito: ")
    
    with open('habitos.txt', 'r') as f:
        linhas = f.readlines()
    
    linhas[idx] = novo_habito + '\n' 
    
    with open('habitos.txt', 'w') as f: 
        f.writelines(linhas)
    print("Local atualizado!")


def deletar():
    ler()
    idx = int(input("Digite o ID do habito que deseja excluir: "))
    
    with open('habitos.txt', 'r') as f:
        linhas = f.readlines()
    
    del linhas[idx] # Remove da lista
    
    with open('habitos.txt', 'w') as f:
        f.writelines(linhas)
    print("habito removido!")


while True:
    print("\n1-Cadastrar | 2-Listar | 3-Editar | 4-Excluir | 5-Sair")
    opcao = input("Escolha: ")
    
    if opcao == '1': criar()
    elif opcao == '2': ler()
    elif opcao == '3': atualizar()
    elif opcao == '4': deletar()
    elif opcao == '5': break # Interrompe o laço de repetição
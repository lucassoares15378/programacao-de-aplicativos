livros_disponiveis = ["Python Pro", "Banco de Dados", "Redes", "IA", "Hardware"]
livros_emprestados = []

print("1-Escolher livro")
print("2-Devolver livro")
opcao = input("escolha uma opção: ")

if opcao == "1":
    escolha = input("Qual livro você deseja? ")
    if escolha in livros_disponiveis:
        livros_disponiveis.remove(escolha) 
        livros_emprestados.append(escolha) 
        print(f"Você pegou o livro: {escolha}")
    else:
        print("Livro não disponível.")

if opcao == "2":
    escolha = input("Qual livro você deseja devolver? ")
    if escolha in livros_emprestados:
        livros_emprestados.remove(escolha)
        livros_disponiveis.append(escolha)
        print(f"O livro {escolha} retornou a biblioteca! ")
    else:
        print(f"O livro {escolha} não está no catálogo")

del livros_disponiveis[0:2]
print("Alguns livros foram descartados, mas logo serão repostos")

print (livros_disponiveis)
print(livros_emprestados)
        
nomes = ["lucas", "josé", "bruno", "joão", "gustavo"]
usuario = input("Qual é o seu nome? ")
if usuario in nomes:
    print(f"{usuario} você está na lista de convidados!")
else:
    print(f"{usuario} você não está na lista de convidados!")
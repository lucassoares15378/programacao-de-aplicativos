nome = input("Qual é o seu nome? ")
senha = int(input("Senha"))

if nome == "adimin" or nome == "root" and senha == 12345:
    print ("acesso permitido")
else:
    print("acesso negado")

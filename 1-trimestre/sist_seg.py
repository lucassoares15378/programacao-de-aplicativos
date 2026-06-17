nome_de_usuario = input("digite o nome de usuario: ")
codigo = int(input("digite o codigo de segurança: "))

if nome_de_usuario == "adimin" and codigo == 999:
    print("acesso ao servidor liberado")
else:
    print("falha na autenticação")
    
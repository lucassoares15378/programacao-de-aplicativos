senha_correta = "12345"
senha_digitada = ""

while senha_digitada != senha_correta:
    senha_digitada = input("Digite a senha: ")

    if senha_digitada != senha_correta:
        print("senha incorreta, tente novamente.")

print("Bem vindo ao sistema!")
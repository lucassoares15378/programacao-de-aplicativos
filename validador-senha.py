def senha_valida(senha):
    return len(senha) >= 6 

while True:
    senha_digitada = input("Crie uma senha: ")

    if senha_valida(senha_digitada):
        print("Senha Cadastrada!")
    break

print("Senha curta, digite 6 ou mais caracteres")
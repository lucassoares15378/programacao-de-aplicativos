senha = input("Qual é a senha? ")
tentativa = int(input("Qual é o número da tentaiva atual? "))
token = input("Você possui o token? (s/n) ")

if (senha == "adimin123") and (tentativa %3 == 0 or token == "s"):
    print(f"Tentativa nº {tentativa}: ACESSO CONCEDIDO.")
else:
    print(f"Tentativa nº {tentativa}: ACESSO BLOQUEADO POR PROTOCOLO.")
    

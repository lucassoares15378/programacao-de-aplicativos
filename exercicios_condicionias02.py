# 1. Evento VIP
idade = int(input("Sua idade: "))
saldo = float(input("Saldo na carteira: R$ "))

if idade >= 18 and saldo >= 50.0:
    print("Acesso autorizado!")
else:
    print("Acesso negado.")

# 2. Aprovação Escolar
media = float(input("Média final: "))
presenca = int(input("Porcentagem de presença (0-100): "))

if media >= 7.0 and presenca >= 75:
    print("Aprovado!")
else:
    print("Reprovado por nota ou falta.")

# 3. Game Unlock
nivel = int(input("Nível do jogador: "))
esferas = int(input("Esferas coletadas: "))

if nivel >= 20 and esferas > 50:
    print("Super Salto liberado!")
else:
    print("Continue jogando para desbloquear.")

# 4. Login Admin
user = input("Usuário: ")
codigo = int(input("Código secreto: "))

if user == "admin" and codigo == 999:
    print("Acesso concedido ao sistema.")
else:
    print("Erro de login.")
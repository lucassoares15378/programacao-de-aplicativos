saldo = 1000.00

print ("banco")
print("1- deposito")
print("2- saque")
print("3-extrato")

opcao = input("escolha uma opção: ")
if opcao == "1":
    valor = float(input("digite o valor de deposito: "))
    valor_deposito = valor + saldo
    print("deposito realizado com sucesso, seu saldo é", valor_deposito)

if opcao == "2":
    valor = float(input("digite o valor do saque: "))
    valor_saque = saldo - valor
    print("saque realizado com sucesso, seu saldo é", valor_saque)

if opcao == "3":
    extrato = saldo
    print("extrato:", extrato)

#1. O Baú do RPG

nome = input("Digite o nome do personagem: ")
nivel = int(input("Digite o nível do personagem: "))
ouro = float(input("Digite quanto ouro o personagem tem: "))
vivo = input("Ele está vivo? ")


print("Nome do Herói:", nome)
print("Nível:", nivel)
print("Moedas de Ouro:", ouro)
print("Está vivo?", vivo)

#2. Calculadora de Idade (Casting de Inteiros)

ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite o ano em que você nasceu: "))

idade = ano_atual - ano_nascimento

print("Sua idade atual é", idade, "anos.")

#3. Conversor de Moedas
DOLAR = 5.00

reais = float(input("Quantos Reais (R$) você tem na carteira? "))

resultado = reais / DOLAR

print("Com R$", reais, ", você pode comprar US$", resultado)


#5. O Recibo de Loja (Desafio Final)
produto = input("Nome do produto: ")
preco_unitario = float(input("Preço unitário: "))
quantidade = int(input("Quantidade comprada: "))

total = preco_unitario * quantidade

print("Você comprou", quantidade, "unidades de", produto)
print("Total a pagar: R$", total)
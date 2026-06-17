cliente = input("Nome do Cliente: ")
valor_original = float(input("Valor da Compra: R$ "))
distancia = int(input("Distância (km): "))
tem_cupom = input("Possui cupom? (S/N): ")

desconto = 0.0

if valor_original >= 1000.0 and tem_cupom == "S":
    desconto = valor_original * 0.20
elif valor_original > 500.0 and tem_cupom == "S":
    desconto = valor_original * 0.10

valor_com_desconto = valor_original - desconto

frete = 40.0
if distancia <= 50 and valor_com_desconto > 200.0:
    frete = 0.0

total_final = valor_com_desconto + frete

print("-" * 30)
print(f"RELATÓRIO DE COMPRA - {cliente}")
print(f"Valor Original: R$ {valor_original:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Frete: R$ {frete:.2f}")
print(f"TOTAL A PAGAR: R$ {total_final:.2f}")

if desconto == (valor_original * 0.20):
    print("SURPRESA: Você ganhou um Mousepad Gamer de brinde!")
print("-" * 30)
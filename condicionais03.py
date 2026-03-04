compra = float(input("digigte o valor total da compra: "))
cupom = input("digite o cupom: ")


desconto = compra * 0.10
valor_desconto =  compra - desconto

if cupom == "DEV10":
    print("cupom válido", valor_desconto)
else:
    print("cupom inválido", compra)
    
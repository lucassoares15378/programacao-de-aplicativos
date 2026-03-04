valor =  float(input("digite o valor da compra: "))
prime = input("você é assinante prime? (s/n) ")

if valor >= 500.00 or prime == "s" and valor <100:
    frete = 0
else:
    frete = 50
    print ("frete de 50.00 adicionado")

    total = valor + frete 
    print("valor total", total)
    
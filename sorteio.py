id = int(input("Qual é o seu ID: "))
compra = int(input("Qual o valor da compra"))

if id %2 == 0 and compra > 500:
    print(f"Parabéns usuário {id}, você ganhou um cupom para a compra de R${compra}. ")
else:
    print(f"Obrigado pela compra, usuário {id}. Continue acompanhando nossas promoções!")
nome = input ("digite seu nome: ")
altura = float(input("digite sua altura: "))
if altura >= 1.50:
    print("acesso liberado! divirta-se em queda livre", nome)
elif altura <1.50:
    print("desculpa, você não tem a altura mínima", nome)
    
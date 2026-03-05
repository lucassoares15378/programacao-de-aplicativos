comprimento = input("Sua peça está no comprimento entre 10cm a 12cm (s/n)? ")
if comprimento == "s":
    print("comprimento válido")
else:
    print("comprimento inválido, descarte a peça")

largura = input("a largura está entre 5cm a 6cm (s/n)? ")
if largura == "s":
    print("largura válida, peça pronta.")
else:
    print("largura inválida, descarte a peça")

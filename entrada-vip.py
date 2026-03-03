idade = int(input(" Qual é a sua idade? "))
tem_ingresso = input("Tem ingresso? (S/N): ")
esta_na_lista = input("Você está na lista? (S/N): ")
if idade > 18 and tem_ingresso == "S" or esta_na_lista == "S":
    print ("acesso permitido")
else:
    print ("acesso negado")
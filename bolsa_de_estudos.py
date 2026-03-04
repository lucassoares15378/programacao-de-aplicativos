media = float(input ("Qual é a sua média escolar? "))
renda = float(input ("Qual é a sua renda? "))
escolaridade = input ("Veio de escola publica? (s/n)")
if media >= 8.0 and renda >= 2.000 or escolaridade == "s":
    print("Você ganhou a bolsa")
elif media < 8.0 and renda < 2.000 or escolaridade == "n":
    print("Você não ganhou a bolsa")
    
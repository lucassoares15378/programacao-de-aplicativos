vagas = ["ocupado", "livre", "ocupado", "livre"]
usuario = int(input(" digite o numero da vaga (0 a 3)"))

if usuario % 2 == 0 and vagas == ("livre"):
    print("Vaga liberada!")
else:
    print("Vaga ocupada!")
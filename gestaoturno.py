id = int(input("Qual é o seu ID? "))
temperatura = int(input("Qual é a temperatura da máquina que você está operando? "))
tempo = int(input("Quantas horas você está operando a máquina? "))
if (id %3 == 0) and (temperatura > 40 or tempo > 8 ):
    print(f"Funcionário {id}, você foi escalado para a manutenção preventiva hoje.")
else:
    print(f"Funcionário {id}, sua máquina opera dentro dos padrões normais.")
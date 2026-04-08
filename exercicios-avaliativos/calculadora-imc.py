peso = float(input("Qual é o peso? "))
altura = float(input("Qual é a altura? "))
imc = peso / (altura ** 2)
print(f"Seu imc é {imc}")

if imc >= 25:
    print("Você está em sobrepeso!")
else:
    print("Você está no peso normal!")

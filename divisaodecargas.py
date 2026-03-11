codigo = int(input("Digite seu codigo: "))
peso = int(input("Qual é o peso da carga? "))
status = "carga normal"

if peso < 5 and codigo %10 == 0:
    status = "carga normal"

if peso > 50:
    status = "Carga Pesada"

print(f"Pacote {codigo}: {status}") 
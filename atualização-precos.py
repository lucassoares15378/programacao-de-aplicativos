precos = [19.90, 45.00, 89.90, 120.00]
print(precos)

precos.remove(45.00)
precos.insert(1, 55.00)

numero = (120/2)

precos.remove(120.00)
precos.insert(3, numero)

print(f"Os novos preços são{precos}")

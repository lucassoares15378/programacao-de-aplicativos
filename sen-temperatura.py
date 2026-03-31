temps = [28.5, 31.0, 29.8, 33.5, 27.0, 35.2, 30.0]


for valor in temps:
    if valor > 30.0:
       print(f"ALERTA: Temperatura Crítica! ({valor}°C)")
    else:
        print(f"Temperatura Normal. ({valor}°C)")
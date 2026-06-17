temperatura = float(input("digite a temperatura: "))

if temperatura >= 80:
    print("alerta! desligando servidor por superaquecimento. ")
elif temperatura >= 50:
    print("alerta! ventilador no máximo. ")
elif temperatura <=50:
    print("temperatura estável, sistema funcionando normalmente. ")
    
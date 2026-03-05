print("--- Monitor de estufa Inteligente ---")
temp = float(input("Qual é a temperatura?"))
if temp <= 30.0:
    print("temperatura estável!")
elif temp > 30.0:
    print("alerta de calor!")
    umidade = float(input("Qual é a umidade"))
    if  umidade < 40.0:
        print("Alerta, lique os irrigadores!!!")
    elif umidade > 40.0:
        print("Lique os ventiladores e ventoinhas!!!")

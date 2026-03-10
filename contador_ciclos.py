garrafas = int(input("Qual é o total de garrafas que passaram pela esteira hoje"))
if garrafas % 500 == 0:
    print("Hora da limpeza!")
if garrafas % 100 == 0:
        print("Teste de qualidade, retire uma garrafa para conferir")

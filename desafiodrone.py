drone = int(input("qual é o codigo do drone"))
torre = input("possui autorização da torre? (s/n)")

if drone == 999 or torre == "s":
    
    bateria = int(input("qual o nível da bateria ( 0 a 100)"))
    clima = input(" clima (ensolarado/chuvoso): ")
    vento = int(input("Qual a velocidade do vento (km/h): "))

    if bateria > 10:
        print("Pouso autorizado")
    
    else:
        if( clima == " ensolarado" and vento < 30) or (clima == "chuvoso" and vento < 10 ):
            print("pouso liberado")
        else:
            print("pouso negado")
ataque = int(input("digite o dano de ataque do heroi: "))
defesa = int(input("digite a defesa do rival: "))
 
dano = defesa - ataque

if ataque <= defesa:
    print("o vilao bloqueoou o ataque", dano)
elif ataque >= defesa:
    print("ataque critico! o dano causado no rival foi", dano)
    
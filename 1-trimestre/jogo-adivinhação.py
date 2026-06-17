lista_secreta = ["azul", "preto", "verde"]
tentativas = 0
acertou = False 

while tentativas < 3 and not acertou:
    palpite = input("Tente adivinhar uma cor: ")
    
    if palpite in lista_secreta:
        print("Parabéns, você acertou!")
        acertou = True
    else:
        print("Errou!")
    
    tentativas += 1
if not acertou:
    print("Suas tentativas acabaram.")
    print("As cores eram:", lista_secreta)
cargo = input("Qual é o seu cargo? ")
codigo = int(input("Qual é o código? "))
botao = input("O botão de emergência está ativado? (s/n) ")
epi = input("Seu EPI está completo? (s/n)")

if (cargo == "engenheiro" or "tecnico") and (codigo == 1234 or botao == "s") and epi == "s":
    print("acesso permitido")
else:
    print("acesso negado, risco de segurança")
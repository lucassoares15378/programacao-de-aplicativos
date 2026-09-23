print("Menu de Bebidas")
print("1-Café")
print("2- Chá")
print("3- Suco")

opcao = int(input("Qual bebida você quer?"))

match opcao:
    case 1:   
        print("Você escolheu Café")
    case 2:
        print("Você escolheu Chá")
    case 3:
        print("Você escolheu Suco")
    case _:
        print("Opção inválida")
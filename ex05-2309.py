numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

operacao = input("Digite a operação (+ ou -): ")

match operacao:
    case "+":
        print("Resultado:", numero1 + numero2)
    case "-":
        print("Resultado:", numero1 - numero2)
    case _:
        print("Operação inválida")

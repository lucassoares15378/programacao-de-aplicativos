nota = input("Qual a nota?")
match nota:
    case "A" | "B":
        print("Excelente")
    case "C" | "D":
        print("Desempenho mediano")
    case "F":
        print("Reprovado")
    case _:
        print("Nota Inválida")
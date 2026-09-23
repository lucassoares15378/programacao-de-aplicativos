dia = input("Digite o dia da semana: ")
match dia:
    case "sexta" | "sábado" | "domingo":
        print("Fim de semana")
    case "segunda" | "terça" | "quarta" | "quinta":
        print("Meio de semana")
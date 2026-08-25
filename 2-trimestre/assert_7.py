def classificar_idade(idade):
    if idade < 12:
        return "Criança"
    elif idade < 18:
        return "Adolescente"
    else:
        return "Adulto"

assert classificar_idade(10) == "Criança"
assert classificar_idade(15) == "Adolescente"
assert classificar_idade(18) == "Adulto"

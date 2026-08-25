def buscar_nome(lista, nome):
    return nome in lista


def tem_senha_valida(senha):
    return len(senha) >= 8

assert buscar_nome(["Ana", "João"], "Ana") is True
assert buscar_nome([], "Ana") is False
assert buscar_nome(["Ana"], "João") is False

assert tem_senha_valida("1234567") is False  # 7 caracteres
assert tem_senha_valida("12345678") is True  # limite: 8 caracteres
assert tem_senha_valida("senha123") is True  # acima do limite

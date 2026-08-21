def calcular_desconto(preco, percentual):
 	return preco - percentual

 # Escreva seus testes aqui.
assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 20) == 160
assert calcular_desconto(50, 10) == 45

def calcular_desconto(preco, percentual):
 	return preco - (preco * percentual / 100)

assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 20) == 160
assert calcular_desconto(50, 10) == 45

#Estava errado porque o preço subtraia diretamente com a porcentagem
#entao fiz a alteração para fazer o valor correto da porcentagem e depois subtrair com o preço inicial
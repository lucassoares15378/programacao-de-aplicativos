def eh_par(numero):
 	return numero % 2 == 0

assert eh_par(3) is False

#O assert estava errado pois estava falando que 3 é par, porque estava usando o True que é par
#tivemos que trocar o True por False, porque False é ímpar


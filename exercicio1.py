#Exercício Número 1
numero = 10
def quadrado_par(numero):
    print('O numero inserido foi', numero)

    for i in range(numero):        
        if (i % 2) == 0:            
	        print(i ** 2)

quadrado_par(numero)



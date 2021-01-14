#Exercício Número 2
pares = 0
impares = 0
lista_de_pares = []
lista_de_impares = []
lista = list() 

quantidade_de_valores = True

while quantidade_de_valores:
    num = int(input('Adicione um Valor: '))
    if (num < 0):
        break
    lista.append(num)
    
for num in lista:
    if (num % 2) == 0:            
        pares = num            
        lista_de_pares.append(pares)        
    else:            
        impares = num
        lista_de_impares.append(impares)        

print('Elementos Pares:', lista_de_pares)
print('Elementos Impares:', lista_de_impares)

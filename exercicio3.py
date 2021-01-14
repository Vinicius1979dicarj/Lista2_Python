quantidade_de_valores = True
conta_par = 0
cont = 0
print("Digite um numero diferente de -1: ")
while quantidade_de_valores:
    num = int(input("Digite um numero: "))
    if(num < 0):
        break
    cont = cont + 1
    if num % 2 == 0:
        conta_par = conta_par + 1

print(conta_par, "numeros pares")




lista1 = list() 
lista2 = list()
def decrescente(lista1, lista2):
    quantidade_de_valores = True

    print("Populando a primeira lista: ")
    print("Digite um numero diferente de -1: ")
    while quantidade_de_valores:
        num = int(input("Digite um numero: "))
        if(num < 0):
            break
        lista1.append(num)

    print("\nPopulando a segunda lista: ")
    print("Digite um numero diferente de -1: ")
    while quantidade_de_valores:
        num2 = int(input("Digite um numero: "))
        if(num2 < 0):
            break
        lista2.append(num2)

    lista3 = []
    for i in lista1:
        lista3.append(i)
    for j in lista2:
        lista3.append(j)

    print("Lista A:", lista1)
    print("Lista B:", lista2)   
    print("\n Lista C:", sorted(lista3, reverse=True))

decrescente(lista1, lista2)


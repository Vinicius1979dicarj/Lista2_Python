lista = list() 
def lista_ao_quadrado(lista):
    quantidade_de_valores = True

    print("Digite um numero diferente de -1: ")
    while quantidade_de_valores:
        num = int(input("Digite um numero: "))
        if(num < 0):
            break
        lista.append(num ** 2)

    print(lista)

lista_ao_quadrado(lista)


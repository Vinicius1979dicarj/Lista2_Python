quantidade_de_valores = True

A = [10, 20, 30]
B = []

def adiciona(A, *B):
    C = []
    newB = list(B)
    C = A + newB
    
    print(C)

adiciona(A, 4, 10, 50, 1)
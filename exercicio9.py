A = [10, 20, 30]
B = []
D = [5, 13, 20]
E = [25, 35, 64, 40]

def intercept2(A, *B):
    C = []
    newB = list(B)
    for i in newB:
        C = A + i
    C.sort()
    print(C)

intercept2(A, D, E)

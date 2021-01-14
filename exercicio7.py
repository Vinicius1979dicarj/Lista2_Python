A = [-2, 0, 1, 2, 3]
B = [-1, 2, 3, 6, 8]

def intercept(A, B):
    l = []
    for i in A:
        if i in B:
            l.append(i)
    l.sort()
    print(l)



intercept(A, B)
A = [-2, 0, 1, 2]
B = [-1, 1, 2, 10]

def union(A, B):
    l = []
 
    for i in A:
        if i not in B:
            l.append(i)
    for j in B:
        if j not in A or j in B:
            l.append(j)
    l.sort()
    print(l)

union(A, B)
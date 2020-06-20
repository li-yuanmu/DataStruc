# heap算法计算全排列数

def heap_perm(A):
    n = len(A)
    Alist = [i for i in A]
    for hp in _heap_perm_(n, Alist):
        yield hp

def _heap_perm_(n, A):
    if n == 1:
        yield A

    else:
        for i in range(1, n+1):
            for hp in _heap_perm_(n-1,A):
                yield hp

            if (n%2) == 1:
                j = 1

            else:
                j = i

            A[j-1], A[n-1] = A[n-1], A[j-1]

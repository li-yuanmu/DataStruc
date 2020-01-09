L = [1,3,2,5,6,8,4]

def insert_sort(L):
    for i in range(1, len(L)):

        key = L[i]

        j = i - 1

        while j > 0 and key < L[j]:
            L[j+1] = L[j]
            j -= 1
        L[j+1] = key

def insert_sort2(L):
    for j in range(1, len(L)):
        for i in range(j, 0, -1):
            if L[i] < L[i - 1]:
                L[i], L[i -1] = L[i - 1], L[i]
            else:
                break











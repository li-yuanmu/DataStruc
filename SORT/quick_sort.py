
#C风格的快排

def quick_sort_C(L):
    return q_sort(L, 0, len(L) - 1)

def q_sort(L, left, right):
    if left < right:
        pivot = partition(L, left, right)

        q_sort(L, left, pivot - 1)
        q_sort(L, pivot + 1, right)
    return L

def partition(L, left, right):
    pivotkey = L[left]

    while left < right:
        while left < right and L[right] >= pivotkey:
            right -= 1
        L[left] = L[right]
        while left < right and L[left] <= pivotkey:
            left += 1
        L[right] = L[left]

    L[left] = pivotkey
    return left


#python风格的快排,效率极低
def quick_sort_P(L):
    if len(L) < 2:
        return L
    else:
        pivot = L[0]
        less_than_pivot = [x for x in L if x <= pivot]
        more_than_pivot = [x for x in L if x > pivot]
        return quick_sort_P(less_than_pivot) + [pivot] + quick_sort_P(more_than_pivot)


L = [5,9,2]

print(quick_sort_C(L))
print(quick_sort_P(L))



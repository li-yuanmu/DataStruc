
def merge(s1, s2):
    s = len(s1+s2) * [0]
    i = 0
    j = 0
    k = 0

    while i < len(s1) and j < len(s2):

        if s1[i] < s2[j]:
            s[k] = s1[i]
            i += 1
            k += 1

            if i == len(s1):
                s[k] = s2[j]

        else:
            s[k] = s2[j]
            j += 1
            k += 1

            if j == len(s2):
                s[k] = s1[i]

        

    return s


print(merge([1,1,3],[1,2,4]))


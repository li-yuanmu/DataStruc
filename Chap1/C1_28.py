v = [1,2,3]
p = 2
def norm(v,p):
    return pow(sum([v[i]**p for i in range(len(v))]),1/p)

print(norm(v,p))
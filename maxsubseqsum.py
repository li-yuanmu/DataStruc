a = [1,2,3,4]

def maxsubseqsum1(a):  #n的三次方的复杂度
    maxsum = 0

    for i in range(len(a)):
        for j in range(i,len(a)):
            thissum = 0
            for k in range(i, j+1):
                thissum += a[k]
            if thissum > maxsum:
                maxsum = thissum
    return maxsum


def maxsubseqsum2(a):  #n的平方的复杂度
    maxsum = 0
    for i in range(len(a)):
        thissum = 0
        for j in range(i, len(a)):
            thissum += a[j]
            if thissum > maxsum:
                maxsum = thissum
    return maxsum


def maxsubseqsum3(a):      #在线处理  复杂度为O(n)  最快的算法
    thissum = maxsum = 0
    for i in range(len(a)):
        thissum += a[i]
        if thissum > maxsum:
            maxsum = thissum
        elif thissum < 0:
            thissum = 0
    return maxsum




print(maxsubseqsum1(a))

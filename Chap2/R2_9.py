class Vector:
    #多维向量

    def __init__(self, d):
        #初始化一个d-维全0向量
        self._coords = [0] * d

    def __len__(self):
        #返回向量维度
        return len(self._coords)

    def __getitem__(self, j):
        #返回第j个坐标
        return self._coords[j]

    def __setitem__(self, j, val):
        #给第j个位置赋值
        self._coords[j] = val

    def __add__(self, other):
        #返回两个向量的和
        if len(self) != len(other):
            raise ValueError('维度必须一样')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __equal__(self, other):

        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other
    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('维度必须一样')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        result = Vector(self.__len__())
        for j in range(self.__len__()):
            result[j] = 0 - self[j]
        return result
    
    def __mul__(self, other):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * other
        return result
    
    def __mult__(self, other):
        result = 0
        for j in range(len(self)):
            result += self._coords[j] * other[j]
        return result




a = Vector(5)
b = Vector(5)
a.__setitem__(1, 4)
print(a.__mult__([1,1,1,1,1]))
#print(a.__mul__(3))
#print(a.__neg__())
#print(a.__sub__(b))
#print(a.__len__())
#print(a.__str__())
            
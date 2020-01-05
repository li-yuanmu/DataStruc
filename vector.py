class Vector:
    """在多维空间中表示向量"""
    def __init__(self, d):
        """创建一个d维的全0的向量"""
        self._coords = [0] * d

    def __len__(self):
        """返回向量的维度"""
        return len(self._coords)

    def __getitem__(self, j):
        """返回第j个坐标"""
        return self._coords[j]

    def __setitem__(self, j, val):
        """给第j个坐标赋值"""
        self._coords[j] = val

    def __sum__(self, other):
        """返回两个向量的和"""
        if len(self) != len(other):
            raise ValueError('维度不一样!')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    def __str__(self):
        """生成向量的字符串表达"""
        return '<' + str(self._coords)[1:-1] + '>'

v = Vector(5)
v[4] = 4
u = v.__sum__(v)
print(u)

print(v[4])
print(v.__len__())

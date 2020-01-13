class ArrayStack:
    """使用列表作为底层存储的后进先出（LIFO）的栈"""
    def __init__(self):
        """初始化一个空栈"""
        self._data = []

    def __len__():
        """栈中元素个数"""
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        return self._data.append(e)
    def top(self):
        #返回栈顶元素
        if self.is_empty():
            raise Empty('空啦')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('空啦')
        return self._data.pop()
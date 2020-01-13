class ArrayQueue:
    #先进先出的队列（FIFO）

    CAPACITY = 10

    def __init__(self):
        #初始化一个空队列
        self._data = [None] * ArrayQueue.CAPACITY
        self._size = 0
        self._front = 0   #队列最前面

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        #返回队列最前面元素
        if self.is_empty():
            raise Empty('空的')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('空啦')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer
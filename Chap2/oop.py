class Progression:
    """通用数列类"""
    def __init__(self, start = 0):
        self._current = start

    def _advance(self):
        """下一个值"""
        self._current += 1

    def __next__(self):
        """返回下个元素"""
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        """打印数列的下一个值"""
        print(''.join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression):
    """等差数列"""
    def __init__(self, increment = 2, start = 0):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment

class GeometricProgression(Progression):
    """等比数列"""
    def __init__(self, base = 2, start = 1):

        super().__init__(start)
        self._base = base

    def _advance(self):
        self._current *= self._base

class FibonacciProgression(Progression):

    def __init__(self, first = 0, second = 1):
        super().__init__(first)
        self._prev = second - first

    def _advance(self):

        self._prev, self._current = self._current, self._prev + self._current

#print(FibonacciProgression(8))
#FibonacciProgression().print_progression(8)

#GeometricProgression().print_progression(8)

GeometricProgression(8)



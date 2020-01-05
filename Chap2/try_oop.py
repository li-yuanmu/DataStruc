class student:

    def __init__(self, weight, high):
        self._weight = weight
        self._high = high

    def fat(self):
        if self._weight > 120:
            print('you are fat')

    def small(self):
        if self._high < 150:
            print('you are small')

class FatStudent(student):
    def __init__(self, weight, high, add):
        super().__init__(weight, high)
        self._add = add

    def fat(self):
        if self._weight > 120 + self._add:
            print('you are fat')


bob = FatStudent(150, 150, 10)
bob.fat()

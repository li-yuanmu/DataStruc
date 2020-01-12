class Flower:
    def __init__(self, name = 'hua', number = 8, price = 5):
        self._name = name
        self._number = number
        self._price = price

f1 = Flower()

print(f1._name)
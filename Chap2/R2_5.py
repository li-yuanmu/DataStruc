class CreditCard:

    #消费者信用卡

    def __init__(self, customer, bank, acnt, limit):
        #制造一个新的信用卡实例
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def make_payment(self, amount):
        '''
        try:
            float(amount)
            self._balance -= amount
            return  self._balance
        except ValueError:
            print('需要一个数字')
        '''
        try:
            if amount < 0:
                raise ValueError('amount must be positive')
            self._balance -= amount
        except TypeError:
            print('要是数字')

a = CreditCard(1,2,3,4)

print(a.make_payment(1))

#print(a.get_customer())



class Fruit():
    
    def __init__(self, name, price):
        self._name = name
        self._price = price
        
    def __str__(self):
        return 'Fruit Class Info -> Name : {} Price : {}'.format(self._name, self._price)
    
    def __add__(self, x):
        return self._price + x._price
    
f1 = Fruit('Apple', 8000)
f2 = Fruit('Banana', 5000)
f3 = Fruit('Melon', 10000)
print(f1 + f2 )
    
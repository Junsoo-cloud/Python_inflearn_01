# Chpater03_01.py
# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence) , 반복(Iterator), 함수(Functions), 클래스(Class)
# 클래스 안에 정의할 수 있는(Built-in) Method


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
    
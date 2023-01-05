# Chapter02_03
# Codecademy -> 언어 문법을 빠르게 배울 수 있는 곳이다 https://www.codecademy.com/learn

# 파이썬 OOP (객체 지향 프로그래밍) -> 코드의 재사용, 코드 중복 방지, 유지보수 쉬움
# 규모가 큰 프로그램 -> 함수 중심 -> 데이터 방대 -> 복잡도 상승
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

class Car():
    """
    Car class
    Author : Kim
    Date : 2023.01.02
    Description : Class, Instance, Static Method
    """
    
    # 클래스 변수(모든 인스턴스가 공유함 !)
    # 인스턴스 변수를 선언할 때는 _를 붙이는 습관 (클래스 변수와 구분하기 위해서)
    price_per_raise = 1.0
    
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self): # print문으로 내용 확인 (사용자 입장)
        return 'str: {} - {}'.format(self._company, self._details)
    
    def __repr__(self): # 객체 (개발자 입장)
        return 'repr: {} - {}'.format(self._company, self._details)
    
    # Instance Method
    # self: 객체의 고유한 속성 값 사용
    def detail_info(self):
        print('Current id: {}'.format(id(self)))
        print('Car Detail Info : {} - {}'.format(self._company,self._details.get('price')))
    def get_price(self):
        return 'Before Car Price -> Company : {} Price {}'.format(self._company, self._details.get('price'))
    def get_price_culc(self):    
        return 'After Car Price -> Company : {} Price {}'.format(self._company, self._details.get('price') * Car.price_per_raise)
    
    # Class Method -> 클래스 변수를 Handling 할 때 사용 ! (Logic도 추가 가능하다는 장점)
    
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter More ')
            return # 안하면 밑까지 출력됨
        cls.price_per_raise = per
        print('Succeed!')
        
    # Static Method -> 유연하게 사용 가능하다는 장점이 있지만, 사용 안해도 문제될 것은 없다 
    # parameter를 받지 않는다는 특징이 있다
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return 'Ok This Car is {}'.format(inst._company)
        return 'Sorry thie Car is not Bmw'
    

car1 = Car('Ferrari', {'color' : 'White', 'horsepower' : 400, 'price' : 8000})
car2 = Car('Bmw', {'color' : 'black', 'horsepower' : 270, 'price' : 5000})


# 가격정보
print(car1._details.get('price'))


print(car1.get_price())
print(car2.get_price())

print(car1.get_price_culc())
print(car2.get_price_culc())


# 가격 인상(클래스 메소드 미사용)
Car.price_per_raise = 1.4

# 가격 인상(클래스 메소드 사용)
Car.raise_price(1)
Car.raise_price(2)
print()
print()


# 인상 후
print(car1.get_price_culc())
print(car2.get_price_culc())

print()
print()


Car.raise_price(1)
Car.raise_price(2)

print()
print()
print()


print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
print(Car.is_bmw(car1))
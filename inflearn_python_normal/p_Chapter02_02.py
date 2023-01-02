# Chapter02_02


class Car():
    """
    Car class
    Author : Kim
    Date : 2023.01.02
    """
    def __init__(self, company, details):
        self._company = company
        self._details = details
        
    def __str__(self): # print문으로 내용 확인 (사용자 입장)
        return 'str: {} - {}'.format(self._company, self._details)
    
    def __repr__(self): # 객체 (개발자 입장)
        return 'repr: {} - {}'.format(self._company, self._details)

    

car1 = Car('Ferrari', {'color' : 'White', 'horsepower' : 400, 'price' : 8000})
car2 = Car('Bmw', {'color' : 'black', 'horsepower' : 270, 'price' : 5000})
car3 = Car('Audi', {'color' : 'Silver','horsepower' : 300, 'price' : 6000})


# ID 값 확인 (self의 이해)
# 즉, 클래스 내에 정의된 self는 클래스 인스턴스임을 알 수 있음

print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)


# dir & __dict__ 확인

print(dir(car1))
print()
print(car1.__dict__) # 네임스페이스

print()
# Doctring
print(Car.__doc__)
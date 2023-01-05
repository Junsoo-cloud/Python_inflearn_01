# Chapter02_02
# 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

class Car():
    """
    Car class
    Author : Kim
    Date : 2023.01.02
    """
    
    # 클래스 변수(모든 인스턴스가 공유함 !)
    # 인스턴스 변수를 선언할 때는 _를 붙이는 습관 (클래스 변수와 구분하기 위해서)
    car_count = 0
    
    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1 # init 메소드가 호출될때 마다 1씩 증가
        
    def __del__(self):
        Car.car_count -= 1 # 인스턴스 메소드로 가져와야
        
    def __str__(self): # print문으로 내용 확인 (사용자 입장)
        return 'str: {} - {}'.format(self._company, self._details)
    
    def __repr__(self): # 객체 (개발자 입장)
        return 'repr: {} - {}'.format(self._company, self._details)
    def detail_info(self):
        print('Current id: {}'.format(id(self)))
        print('Car Detail Info : {} - {}'.format(self._company,self._details.get('price')))
    

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
# Doctring (나의 정보)
print(Car.__doc__)



car1.detail_info()

# 에러
# Car.detail_info() <- 클래스 (인스턴스 X)

print()

# 네임스페이스에는 클래스 변수 내용 X

print(car1.__dict__)
print(car2.__dict__) 

print(car1.car_count)  # 3

print(dir(car1)) # 클래스 변수


del car2

print()
print(Car.car_count) # del 메소드 사용


# 인스턴스 네임스페이스 없으면 상위에서 자동으로 검색
# 동일한 이름으로 변수 생성 가능, 인스턴스 검색 후 -> 상위 (부모클래스) 변수 검색
# 인스턴스 이름으로 접근, 인스턴스 먼저 검색


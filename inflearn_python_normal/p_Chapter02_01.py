# Chapter02_01

# 파이썬 OOP (객체 지향 프로그래밍) -> 코드의 재사용, 코드 중복 방지, 유지보수 쉬움
# 규모가 큰 프로그램 -> 함수 중심 -> 데이터 방대 -> 복잡도 상승
# 클래스 중심 -> 데이터 중심 -> 객체로 관리


# 일반적인 코딩 (절차지향)

car_company_1 = 'Ferrari'
car_details_1 = [
    {'color' : 'White'},
    {'horsepower' : 400},
    {'price' : 8000}
]

car_company_2 = 'Bmw'
car_details_2 = [
    {'color' : 'black'},
    {'horsepower' : 270},
    {'price' : 5000}
]

car_company_3 = 'Audi'
car_details_3 = [
    {'color' : 'Silver'},
    {'horsepower' : 300},
    {'price' : 6000}
]

# 리스트 구조
# 관리하기가 불편
# 인덱스 접근 시 실수 가능성, 삭제 불편(인덱스 번호를 알아야 하기 때문)
car_company_list = ['Ferrari','Bmw','Audi']
car_detail_list = [
    {'color' : 'White', 'horsepower' : 400, 'price' : 8000},
    {'color' : 'black', 'horsepower' : 270, 'price' : 5000},
    {'color' : 'Silver','horsepower' : 300, 'price' : 6000}
    
]


# 딕셔너리 구조
# 코드 반복 지속 , 키 중복 문제

car_dicts = [
    {'car company': 'Ferrari', 'car detail' : {'color' : 'White', 'horsepower' : 400, 'price' : 8000}},
    {'car company': 'Bmw', 'car detail' : {'color' : 'black', 'horsepower' : 270, 'price' : 5000}},
    {'car company': 'Audi', 'car detail' : {'color' : 'Silver','horsepower' : 300, 'price' : 6000}}
]

print(car_dicts)

print()
print()

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

class Car():
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

print(car1.__dict__) # 네임스페이스
print(car2.__dict__)
print(car3.__dict__)

print(dir(car1)) # 쓸 수 있는 메소드


print()
print()
print()

# 리스트 선언

car_list = []

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list) # 리스트 안에서는 repr 메소드 호출됨

print()
for x in car_list:
    print(repr(x))









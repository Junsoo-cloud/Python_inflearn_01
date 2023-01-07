# Chpater03_02
# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence) , 반복(Iterator), 함수(Functions), 클래스(Class)
# 클래스 안에 정의할 수 있는(Built-in) Method


# 객체 -> 파이썬의 데이터를 추상화

# 일반적인 튜플 

# 네임드 튜플 사용
from math import sqrt
from collections import namedtuple

# 네임드 튜플 선언
# 일반적인 튜플을 사용할 때는 인덱스로 접근해야 함 -> 표본이 많아질 때 혼란을 일으키키 쉬움 -> 네임드 튜플로 key값으로 접근 가능

Point = namedtuple('Point', 'x, y')



pt3 = Point(1.0, 5.0) # x,y가 key로 인식됨
pt4 = Point(2.5, 1.5)
print(pt3)

l_leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)

print(l_leng2)

# 네임드 튜플 선언 방법
Point = namedtuple('Point', 'x, y')
Point2 = namedtuple('Point', 'x y')
Point3 = namedtuple('Point', ['x', 'y'])
Point4 = namedtuple('Point', 'x y x class', rename = True) # 중복 key and 예약어 사용 but rename = True 로 설정

# Dict to Unpaking (튜플 언팩킹)
print(Point4)

temp_dict = {'x': 50, 'y': 20}

pt5 = Point2(**temp_dict)
print(pt5)


# 네임드 튜플 메소드

temp = [52, 38]
# _make() : 새로운 객체 생성
p4 = Point2._make(temp)
print(p4)

# _fields()
# key 값만 조회할 때 사용
print(pt5._fields)

# _asdict() : OrderDict 반환

print(p4._asdict()) # key : value 반환 (맵핑해서)

# 실 사용

# 반20명 4개 반


Classes = namedtuple('Classes','Rank, Number')

numbers = [str(n) for n in range(1,21)]
ranks = 'A B C D'.split()

print(numbers, ranks)

# list Comperhension

stduents = [Classes(rank, number) for rank in ranks for number in numbers]

print(len(stduents))
print(stduents)

# 추천

stduents2 = [Classes(rank, number)
            for rank in 'A B C D'.split()
                for number in [str(n)
                    for n in range(1,21)] ]
print(stduents2)

for s in stduents2:
    print(s)
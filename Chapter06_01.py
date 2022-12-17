# Chapter06_01
# 파이썬 Class
# OOP(객체 지향 프로그래밍) , Self, 인스턴스 메소드, 인스턴스 변수
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# Class vs instance 차이 이해
# 인스턴스 변수 : 객체마다 별도 존재
# 클래스 변수 : 직접 접근 가능 , 공유함

# 예제1

class Dog: # object 상속
    # 클래스 속성
    species = 'just dog'
    def __init__(self,name,age):
        self.name = name
        self.age = age

print(Dog)

# 인스턴스화

dog_1 = Dog('bori', 2)
dog_2 = Dog('mikky',1)
dog_3 = Dog('mikky',1)
        
# 비교
print(dog_1 == dog_3 ,id(dog_1),id(dog_3)) # 인스턴스화 시킨 것들은 모두 id값이 다르다 ++ 다른 객체 !

# 네임스페이스

print('dog_1: ', dog_1.__dict__)
print('dog_2: ', dog_2.__dict__)

# 인스턴스 속성 확인

print(f'{dog_1.name} is {dog_1.age} and {dog_2.name} is {dog_2.age}')

if dog_1.species == 'just dog':
    print(f'{dog_1.name} is {dog_1.species}')

print(Dog.species) # 직접 접근 가능






















# Chapter06_01
# 파이썬 Class
# OOP(객체 지향 프로그래밍) , Self, 인스턴스 메소드, 인스턴스 변수
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# Class vs instance 차이 이해
# 인스턴스 변수 : 객체마다 별도 존재
# 클래스 변수 : 직접 접근 가능 , 공유함
# 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

# 예제1

class Dog2: # object 상속
    # 클래스 속성
    species = 'just dog'
    def __init__(self,name,age):
        self.name = name
        self.age = age

print(Dog)

# # 인스턴스화

dog_1 = Dog('bori', 2)
dog_2 = Dog('mikky',1)
dog_3 = Dog('mikky',1) 
        
# 비교
print(dog_1 == dog_3 ,id(dog_1),id(dog_3)) # 인스턴스화 시킨 것들은 모두 id값이 다르다 ++ 다른 객체 !

# # 네임스페이스

print('dog_1: ', dog_1.__dict__)
print('dog_2: ', dog_2.__dict__)

# 인스턴스 속성 확인

print(f'{dog_1.name} is {dog_1.age} and {dog_2.name} is {dog_2.age}')

if dog_1.species == 'just dog':
    print(f'{dog_1.name} is {dog_1.species}')

print(Dog.species) # 직접 접근 가능

# self 의 이해

class selftest:
    def func1(): # class 메소드이다 (self) 가 없기 때문
        print('Func1 Called')
    def func2(self):
        print(id(self))
        print('Func2 Called')
        
        
f = selftest()

print(dir(f))
print(id(f))
# f.func1() 에러
f.func2()

# self는 인스턴스를 요구한다 ! 

selftest.func1() # 바로 호출

# selftest.func2() 에러 발생 (인스턴스화 된 변수를 넣어줘야함)
selftest.func2(f)


# 예제3
# 클래스 변수 , 인스턴스 변수

class warehouse:
    stock_num = 0
    
    def __init__(self,name):
        
        self.name = name
        warehouse.stock_num += 1
        
    def __del__(self):
        warehouse.stock_num -= 1
        
user1 = warehouse('Lee')
user2 = warehouse('Cho')

print(warehouse.stock_num)

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print(warehouse.__dict__)
print('before: ', warehouse.stock_num)

del user1

print('after :', warehouse.stock_num)

# 예제4

class Dog: # object 상속
    species = 'just dog'
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def info(self):
        return '{0} is {1} years old'.format(self.name, self.age)
    
    def sleap(self,time):
        return '{} time sleap'.format(time)
    

dog_01 = Dog('jult',4)
print(dog_01.info())
print(dog_01.sleap('08:00'))


















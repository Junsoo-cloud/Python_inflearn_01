# Chapter05_01

# 파이썬 함수식 및 람다(Lambda)

# 함수 정의 방법

# def function_name(parameter):
#     code

# 예제1

def first_func(w):
    print("Hello: ",w)

result = first_func('Junsoo')



# 예제2

def return_func(w1):
    result = "Hello: " + str(w1)
    return result

x = return_func('goodboy')

print(x)

# 함수형 프로그래밍 이론 공부하기 !

# 일급 객체와 Closure 

# 일급 객체 (OOP에서 사용되는 함수의 특징)

# 변수 혹은 데이터 구조(자료구조) 안에 담을 수 있어야 한다.
# 매개변수로 전달할 수 있어야 한다.
# 리턴값으로 사용될 수 있어야 한다.

# Closure
# · 어떤 함수의 내부 함수일 것
# · 그 내부 함수가 외부 함수의 변수를 참조할 것
# · 외부 함수가 내부 함수를 리턴할 것


# 예제 3 (다중반환)

def func_mul(x):
    y1 = x*10
    y2 = x*20
    y3 = x*30
    return y1, y2, y3

x, y, z = func_mul(10) #일종의 unpaking

print(x,y,z)

# 튜플 리턴

def func_mul(x):
    y1 = x*10
    y2 = x*20
    y3 = x*30
    return (y1, y2, y3)

q = func_mul(10)
print(type(q),q)

# 리스트 리턴

def func_mul(x):
    y1 = x*10
    y2 = x*20
    y3 = x*30
    return [y1, y2, y3]

s = func_mul(10)
print(type(s),s)

# 딕셔너리 리턴

def func_mul(x):
    y1 = x*10
    y2 = x*20
    y3 = x*30
    return {'v1': y1, 'v2' :y2, 'v3': y3}

d = func_mul(10)

print(type(d),d,d.values(),d.keys())

# 중요 !

# *args , **kwargs

# *args(언팩킹)   * 튜플 형태에서 많이 사용됨 !

def args_func(*args):        # Paking(tuple로)
    for i, v in enumerate(args):        # Unpaking
        print(f'Result : {i} {v}')
    print('----')
    
args_func('Lee')
args_func('Lee','Park')

# **kwargs(언팩킹) * 딕셔너리 형태에서 많이 사용됨 !

def kwargs_func(**kwargs):
    for v in kwargs.keys():
        print(f'{v}',kwargs.get(v))
    print('-----')

kwargs_func(name1 ='Lee',name2 ='kim')

# 전체 혼합

def example_func(args_1,args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)
    
example_func(10,20,'Lee','Park','choi', age=21, grade=1)

# 중첩 함수

def nested_func(num):
    def func_in_func(num):  # 선언
        print(num)
    print('IN FUNC')
    func_in_func(num+100)   # 호출
    
nested_func(100)

# Lambda식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 람다는 즉시 실행 함수 (Heap초기화) -> 메모리 초기화
# 남발 시 가독성 감소

def mul_func(*v):
    x,y = v
    return(x*y)

lambda x,y :x*y


def func_final(x,y,func):
    print(x * y * func(100,100))

func_final(10,20, lambda x,y:x*y)





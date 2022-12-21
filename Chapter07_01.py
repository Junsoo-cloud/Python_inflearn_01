# Chapter07_01

# 파이썬 예외처리
# 예외 종류
# 문법적으로는 예외 x but 코드 실행 시 프로세스에서 발생하는 예외 중요

# 1. 예외는 반드시 처리한다
# 2. 로그는 반드시 남긴다 (Django,Flask에서)
# 3. 예외는 던져진다.
# 4. 예외 무시(추천하는 방법은 아님)

# SyntaxError : 문법 오류

print('eed)
print(''
if True


# NameError : 참조 없음
a = 10
b = 15
print(c)

# ZeroDivisionError

print(100/0)

# IndexError

x = [10,20,30]
print(x[3])

print(x.pop())
print(x.pop())
print(x.pop())
print(x.pop())

# KeyError

dic = {'name': 'Lee', 'Age': 41, 'City': 'Busan'}
# print(dic['hobby']) # KeyError발생
print(dic.get('hobby')) # None 출력 

# 예외 없는 것을 가정하고 프로그램 작성 -> 런타임 예외 발생 시 예외 처리 권장(EAFP)

# AttributeError: 모듈,클래스에 있는 잘못된 속성 사용 예외
import time
# print(time.time2()) # time2라는 것은 time 모듈에 존재하지 않음

# ValueError

# x = [10,50,90]
# x.remove(60)

# FileNotFoundError

# f = open('test.txt') # 파일이 없을 때 발생하는 오류

# TypeError : 자료형에 맞지 않는 연산을 할 경우에 발생

x = [1,2]
y = (1,2)
z = 'junsoo'
print(x + list(y))
print(list(y) + list(z))

# 예외 처리 기본
# try : 에러가 발생할 수 있는 가능성이 있는 코드 실행
# except : 에러명1 :여러개 가능 as e
# else : try블록에 에러가 없는 경우 실행
# finally : 항상 실행

name = ['Kim','Lee','Park']

# 예제1

try:
    z = 'Kim'
    x = name.index(z)
    print(f'{z} found it! {x+1} in name')
except ValueError:
    print('Not found it!')
    
else:
    print('Ok else!')

# 예제2
try:
    z = 'Kim'
    x = name.index(z)
    print(f'{z} found it! {x+1} in name')
except Exception: # 모든 에러를 잡음
    print('Not found it!')
    
else:
    print('Ok else!')


# 예제3

try:
    z = 'choi'
    x = name.index(z)
    print(f'{z} found it! {x+1} in name')
except ValueError as e: # 에러 원인 제공 as e
    print(e)
    print('Not found it!')
    
else:
    print('Ok else!')

finally:
    print('Ok finally!')
    
print()

# 예제4
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Pak'
    if a == 'Park':
        print('Ok Pass')
    else:
        raise ValueError
except ValueError:
    print('Occured! Exception')
else:
    print('Ok else!')

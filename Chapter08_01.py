# Chapter08_01

# 파이썬 Bulit-in function

# 절댓값
# abs 함수

print(abs(-3))

# all, any: iterable 요소 검사(참,거짓)
list_01 = [1,2,3,0]
print(all(list_01)) # 0이 있기 때문에 거짓(iterable한 요소들만 검사 가능) + and 역할
print(any(list_01)) # or 역할

# chr : 아스키 -> 문자 , ord : 문자 -> 아스키

print(chr(65))
print(ord('A'))

# enumerate : 인덱스 + Iterable한 객체 생성

for i, name in enumerate(['abc','def','asda']):
    print(i,name)
    
for i, num in enumerate(list_01):
    print(i,num)
    
# filter : Iterable한 객체 요소를 지정한 함수 조건에 맞는 값 추출

def conv_pos(x):
    return abs(x) > 2

print(filter(conv_pos,[1,2,3,4,-3,-1])) # object 값 
print(list(filter(conv_pos,[1,2,3,4,-3,-1])))

# -> lambda 식으로 더욱 편하게 할 수 있음

print(list(filter(lambda x: abs(x) > 2, [1,2,3,4,-3,-1])))

# id : 객체의 주소값(래퍼런스)반환

print(id(int(5)))

# len : Iterable한 요소의 길이 반환

li = [1,2,3,4,-3,-1]
print(len(li))

# max, min : 최댓값,최솟값

print(max([1,2,3,4,-3,-1]))
print(min([1,2,3,4,-3,-1]))
print(max('python study')) # 오름차순 기준

# map : Iterable한 객체 요소를 지정한 함수 실행 후 추출 <-> filter는 걸러 주고 , map은 추출해서 원하는 자료형으로 묶는 형태

def conv_abs(x):
    return abs(x)

print(list(map(conv_abs,[1,-3,2,0,-5,6])))
print(list(map(lambda x: abs(x),[1,-3,2,0,-5,6])))

# pow : 제곱값 반환
print(pow(2,10))

# range : Iterable한 객체 반환
print(list(range(1,-15,-1)))
print(list(range(1,10,2)))

# round : 반올림 

print(round(5.32))
print(round(5.2321, 2))

# sorted : Iterable한 객체 

print(sorted([1,-3,2,0,-5,6]))


# sum : Iterable한 객체 합 반환

print(sum(range(1,101)))
print(sum(range(1,101,2)))


# type : 자료형 확인

print(type([1,-3,2,0,-5,6]))

# zip : Iterable한 객체의 요소를 묶어서 반환

print(list(zip([10,20,30],[20,30,40])))
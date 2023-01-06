# Chapter04_02

# 반복문 / for 문 패턴 / for ~ else

# for in <collection>
#     <Loop body>

for v1 in range(10):# start , stop , step 으로 구성
    print('v1 is: ',v1)
print()    
for v2 in range(1,11):
    print('v2 is : ',v2)
print()
for v3 in range(2,20,2):
    print('v3 is : ',v3)
    
# 합

sum1 = 0

for v in range(1,1001):
    sum1 += v
print(sum1)

# sum 함수

print('1~100 sum :', sum(range(1,101))) # 1~100

print('4의 배수 합: ', sum(range(4,101,4)))

# Iterables 자료형 반복 (반복 가능한 것)
# 문자열, 리스트, 튜플, 딕셔너리 , 집합
# iterable return 함수 : range, reversed, enumerate , filter , map, zip

names = ['kim','park','cho','lee','choi']

for name in names:
    print('You are :',name)
    

lot_num = [11,13,21,24,136]
for n in lot_num:
    print("current num: ",n)
    
word = "Python"

for lat in word:
    print(lat)
    
my_info = dict(
    name = 'Kim',
    Age = 20,
    City = 'Bundang'
)

for key in my_info:
    print('key:' ,key)
    
for v in my_info.values():
    print('values: ',v)
    
name = 'FineAppLE'

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())
        
# break 

numbers = [14,24,142,25,6,5,34,4,7,73,3,41,6]

for num in numbers:
    if num ==34:
        print('Found: ',34)
        break                 # 구지 마지막까지 search 할 필요 x
    else:
        print('Not Found', num)
        

# continue

lt=  ['1',2,5,True,20,complex(4)]

for v in lt:
    if type(v) is bool:
        continue
    print("current type", type(v))

    
# for ~ else 마지막에 필요한 것

numbers = [14,23,142,25,6,5,34,4,7,73,3,41,6]

for num in numbers:
    if num == 24:
        print('Found: ',24)
        break
else:
    print("Not Found : 24") # 마지막에 못찾으면 못찾았다고 한번 넣어주는 용도로 사용됨 + 찾으면 break문으로 else는 실행되지 않음
    
    
# 변환 예제

name2 = 'niceman'

print('Reversed',reversed(name2))
print('list',list(reversed(name2)))
print('tuple',tuple(reversed(name2)))
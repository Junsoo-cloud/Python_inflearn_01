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
        
# break , continue 문

# 2번째 7분
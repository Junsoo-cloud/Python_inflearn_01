# Chapter04_01

# Python 제어문

# If문

# 기본 형식

print(type(False)) # 0 , [] , () ,'' 비어있는 것들

if True:
    print('Good')
    
if '':
    print('bad') # 실행되지 않음
    


# 관계 연산자

# > >= < <= == !=

# 논리 연산자

# and or not

# 산술 > 관계 > 논리 > 우선순위

print(5+10 >0 and not 7+3 == 10)

score1 = 100
score2 = 'A'
if score1 >= 90 and score2 == 'A':
    print('pass')
    
# 다중조건문

num = 90

if num >= 90:
    print('A')
elif num >= 80 :
    print('B')
elif num >= 70:
    print('C')
else:
    print('과락')
    
# 중첩 조건문

grade = 'A'
total = 95

if grade == 'A':
    if total >= 90:
        print('장학금 100%')
    elif total >= 80:
        print('80%')
        
else:
    print('None')
    
# in, not in

q = [10,20,30]
w = {70,80,90,100}
e = dict(
    name = 'Lee',
    city ='Seoul',
    grade = 'A'
)
r = (10,12,14)

print("Seoul" in e.values())
# separator 옵션

print('P','Y','T','H','O','N', sep='')
print('010','7777','1234', sep="-")
print('kfxsmt','naver.com',sep='@')

# 문자열을 sep = 'x' x로 이어줌

print()


# end 옵션  = 줄바꿈 X end의 해당된 문자열로 이어줌

print('Welcome to',end=' ')
print('IT News', end='-')
print('Web site')


# 객체명
# Camel Case : numberOfCollegeGraduates -> Method
# Pascal Case : NumberOfCollegeGraduates -> Class
# Snake Case : number_of_college_graduates

# 이스케이프 문자 사용

print("I'm boy")
print('I\'m boy')
print('I\\m boy')

print('a\tb')

# \000 : 널 문자

escape_str1 = "Do you have any \"Retro games\"?"
print(escape_str1)

escape_str2 = 'What\'s in Tv?'
print(escape_str2)

# Raw string

raw_s1 = r'D:\python\test' # \ 이나 /  특수 기호를 그대로 사용하는 raw string

print(raw_s1)

# 멀티라인 입력

multi_str = \
'''

String
Multi line
Test
'''
print(multi_str)

any_str = \
'whatever ' \
'you ' \
'want ' \

print(any_str)

# 슬라이싱 연습

str_s1 = "Nice Python"

print(str_s1[0:3]) # 0<= x <3
print(str_s1[5:])
print(str_s1[:len(str_s1)])
print(str_s1[1:9:2]) # 1~9까지에서 2번째씩 (등차)
print(str_s1[-5:])
print(str_s1[:-5])
print(str_s1[::2])
print(str_s1[::-1]) # 역으로 출력

# 아스키 코드(유니코드)

a = 'z'

print(ord(a))
print(chr(122))

# 리스트 함수
a = [1,2,3,4,5]
a.append(10)
print(a)
a.sort()
print(a)
a.reverse()
print(a)
print(a.index(3))
a.insert(2,7)
print(a)
del a[6] 
a.remove(10) # 제거할 값을 넣음
print(a)
a.pop()
print(a)
print(a.count(1))

ex = [8,9]
a.extend(ex)
print(a)

# Tuple 자료형 -> 순서O , 중복O ,수정X ,삭제X # 불변

# 대부분 리스트와 동일

# 선언

t1 = 1,2,3 # 괄호 생략가능
t2 = (2,3,4)
t3 = (2,3,('python','inflearn','army'),'python')
 
# 인덱싱

print(t1[0])
print(t2[0]+t1[0])
print(t3[2][1])


# Packing & Unpaking

t = ('foo','bar','baz','qux') # 튜플로 선언하는 것 자체가 Packing 이다! 

(x1,x2,x3,x4) = t
print(x1,x2,x3,x4) # Unpaking  -> Packing 을 그저 푸는 것!


# 딕셔너리 자료형(순서X ,키 중복X , 수정O, 삭제O)

dic_5 = dict(                # 가장 편리하다고 느끼는 방법 !
        Name = 'man',
        Age = 20,
        Grade = 'A'
)
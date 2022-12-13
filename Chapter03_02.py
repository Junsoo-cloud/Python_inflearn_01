# Chapter03_02

# 파이썬 문자형

# 문자열 생성

str1 = "I am python"
str2 = 'python'
str3 = """How are u?"""
str4 = '''Thank you !'''

# 빈 문자열

str1_t1 = ''
str1_t2 = str() 

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

# 문자열 연산

str_01 = 'ap p le'
str_02 = 'Python'

print(str_01+str_02)
print('y' in str_01)

# 문자열 형 변환

print(str(66),type(str(66)))

# 문자열 함수 (upper, isalnum, startswith , count, endwith)

print("Capitalize: ", str_01.capitalize()) # 첫번째 글자 대문자로
print("endswith: ", str_02.endswith("e")) # 마지막 문자가 어떤걸로 끝나는지
print("replace :", str_02.replace("thon", 'good'))
print("sorted: ", sorted(str_01)) # 정렬
print("split :", str_01.split(' ')) # 특정 단어를 분리할 때 기준이 되는 것

# 반복(시퀀스)

im_str = "Good Boy!"

print(dir(im_str)) # __iter__ 라는 것이 있다 ! -> sequence

for i in im_str:
    print(i)
    

# 슬라이싱 연습

str_s1 = "Nice Python"

print(str_s1[0:3])
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


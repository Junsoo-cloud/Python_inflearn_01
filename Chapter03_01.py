# 파이썬 지원 자료형
# 숫자형 연산자
# 형 변환 (실수+정수) ... 

# 형 변환 실습

# 연산 실습

i1 = 39
i2 = 939
big_int1 = 99999999999999999999999999
bit_int2 = 99999999999999999999888888
f1 = 1.2345
f2 = 3.9292

# 형 변환

a = 3.
b = 6
c = .7
d = 12.7

print(float(b))
print(int(c))
print(int(True))
print(int(d))
print(float(False))
print(complex('3'))  # -> 문자형으로 입력받았어도 숫자형으로 바꾼 다음에 실행


# 수치 연산 함수

print(abs(-7))
x,y = divmod(100,8) # 몫과 나머지
print(x,y)
print(pow(5,3))

# 외부 모듈(패키지)
import math

print(math.pi)
print(math.ceil(5.1))
#Chapter02_02
# 파이썬 변수

# 기본 선언
n = 700

# 출력
print(n)
print(type(n))

# 동시 선언

x=y=z=700
print(x,y,z)


# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1 내부적인 것

print(300)
print(int(300))

# 예2

# n -> 777

n = 777

# id(identity) 확인 : 개체의 고유값 확인

# 같은 오브젝트 참조

m = 800
n = 800

print(id(m))
print(id(n))
print(id(n) == id(m))

# 다양한 변수 선언

# Camel Case : numberOfCollegeGraduates -> Method
# Pascal Case : NumberOfCollegeGraduates -> Class
# Snake Case : number_of_college_graduates


# Chpater04_01
# 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
# Sequence 형
# Container : 서로 다른 자료형 ([List, tuple, collections.deque])
# Flat : 단일 자료형 ([str, bytes, bytearray, array.array, memoryview])
# Mutable : (list, bytearray, array.array, memoryviewm deque)
# Immutable : (int, float, bool, tuple, str, bytes)
# Udemy & Coursera <- 강의 사이트 

# python Bulit-in function 복슴
# enumerate , map, zip, filter

# map -> Syntax : map(function, iterable) : 입력받은 자료형의 각 요소를 함수가 수행한 결과를 그 입력받은 자료형으로 묶어서 반환함
sample_data = [1,2,3,4,5,6,7,8,9]
result = list(map(lambda x: x*2,sample_data))
test = map(lambda x: x*2,sample_data) # -> 아직 자료형 변환 x
print(type(test))
print(result)
print()

# Fliter -> Syntax : filter(function, iterable) : True 인 값을 가지는 요소만 Filter 함

result_01 = list(filter(lambda x: x > 3, sample_data))
print(result_01)

# Zip -> Syntax : zip(*iterable) -> 동일한 개수로 이루어진 자료형을 묶어 주는 역할
# zip 응용
number = [1, 2, 3, 4]
name = ['홍길동','김철수','John','Paul']
number_name = list(zip(number,name))
print(number_name)


# 오늘 나온 용어들 정리 

# List Comprehension (지능형 리스트) -> 편리하게 리스트를 만들 수 있는 방법을 제공 https://www.programiz.com/python-programming/list-comprehension
# https://www.w3schools.com/python/python_lists_comprehension.asp
# syntax of List Comprehension -> [expression for item in list]
# if list 부분에 str or tuple이 들어와도 -> list로 인식함
# python 얕은 복사 vs 깊은 복사  https://blockdmask.tistory.com/576

# 지능형 리스트(List Comprehension)
chars = '+_)(#@$!@'

code_list = []

for s in chars:
    code_list.append(ord(s))
    
print(code_list)

# Use List Comprehension

code_list = [ord(s) for s in chars]
# ord(s) -> expression / s = item / chars = list

print(code_list)
print()
code_list3 = [ord(s) for s in chars if ord(s) >= 40]
code_list4 = list(filter(lambda x: x > 40, map(ord, chars)))

print(code_list3)
print(code_list4)
print()

print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])
print()

# Generator 생성 -> iterator 이다 !
import array

# Generator : 한 번에 한 개의 항목을 생성(메모리를 아낄 수 있음)
tuple_g = (ord(s) for s in chars)
array_h = array.array('I', (ord(s) for s in chars))

print(array_h)
type(array_h)
print(array_h.tolist())


print(tuple_g)
print(type(tuple_g))
print(next(tuple_g))
print(next(tuple_g))
print(next(tuple_g))

print()

# 예제

print()

for s in ('%s' % c + str(n) for c in ['A','B','C','D'] for n in range(1,21)):
    print(s)

print()

# 리스트 주의할 점

# 얕은 복사 (python shallow copy) -> 같은 곳을 참조하고 있다 (mutable 객체)
import array
arr1 = [1,2,3]
arr2 = arr1
arr1.append(3)
print(arr1, arr2)
print(id(arr1) , id(arr2))


marks1 = [['~'] * 3 for _ in range(4)]
marks2 = [['~'] * 3] * 4

print(marks1)
print(marks2)

# 수정
marks1[0][1] = 'x'
marks2[0][1] = 'x'

print(marks1)
print(marks2)

print([id(i) for i in marks1])
print([id(i) for i in marks2])

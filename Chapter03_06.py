# Chapter03_06

# 집합 자료형(set())

# 선언

s1 = set()
s2 = set([1,2,('py'),4,5])
s3 = set([5,4,'python',])
s4 = {'foo','bar','baz','zoo'}

print(f'{s1}\n{s2}\n{s3}\n{s4}')

# 튜플 변환

s2 = tuple(s2)
print(type(s2))
s2 = set(s2)
s3 = list(s3)
print(type(s3))
s3 = set(s3)
# 집합 자료형 활용

print(s1 & s2)
print(s1.intersection(s2))
print(s1 | s2)
print(s1.union(s2))

# 중복 원소 확인

s1 = set([1,2,3,4,5])
s2 = set([3,4,5,6,7])

print(s1.isdisjoint(s2)) # 교집합이 있으면 Faulse 없으면 True

print(s1.issubset(s2)) # s1이 s2의 부분집합인가 ? 당연하게도 Faluse


print(s1.issuperset(s2)) # s1이 s2를 포함하고 있는 집합인가? 당연하게도 Faluse

# 데이터 추가 & 제거

s1 = set([1,2,3,4,5])

s1.add(7)
print(s1)
s1.remove(1)
print(s1)
print(8 in s1)
s1.remove(3) # 만약 없으면 오류 남!! -> in method 사용한는걸 추천!
s1.discard(8) # 에러가 발생하지 않음 !!
s1.clear()
print(s1)

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
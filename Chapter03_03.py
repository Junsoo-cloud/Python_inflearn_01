# Chapter03_03
# 파이썬 리스트
# 자료구조에서 중요

# 리스트 자료형(순서 O ,중복 O , 수정 O , 삭제 O)

# 선언

a= []
b = list()
c = [70,75,80,85]
d = [1,2,'123','123121']
e = [1231,['123123']]

# 인덱싱

print(d[1])
print(d[1]+d[1]) # int형으로

# Identity

temp = c
print(temp,c)
print(id(temp))
print(id(c))

# 리스트 수정,삭제

c[0] = 4
c[1:2] = ['a','b','c'] # 원소로 들어감 ! c[1] = 와는 다름

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

while a:
    data = a.pop()
    print(data)




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
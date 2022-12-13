# Chapter03_04

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




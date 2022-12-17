# Chapter04_03

# 파이썬 While 문

# while <expr>:
#    <statment(s)>


# 예제1

n = 5
while n >0:
    n -= 1
    print(n)
    
# 예제2

a = ['foo','baz','bar','qux']
while a:
    print(a.pop())
    
# 예제5 if 중첩

i = 1

while i <= 10:
    print(i)
    if i ==6:
        break
    i += 1
    
# 예제6

# While ~ else 구문 = for문과 동일


a = ['foo','baz','bar','qux']
s = 'qux'
i = 0
while i< len(a):
    if a[i] == s:
        print('Found: ',s)
        break
    i += 1
else:
    print('Not found : {}'.format(s))
    
# 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
    
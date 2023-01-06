# 1712 python : print문을 나중에 사용 (NameError)
# runtimeerror https://jaimemin.tistory.com/1522
cons, chan, price = map(int,input().split())

try:
    ans = cons / (price - chan)
except ZeroDivisionError:
    ans = -1

if ans < 0:
    ans = -1

else:
    ans = int(ans) + 1
    
print(ans)    


print()
print()
print()


# 2839

task = int(input())

while task 





# Chapter02-1
# 파이썬 완전 기초
# Print 사용법
# 참조 : https://www.python-coures.eu/python3_formatted_output.php  



# 기본 출력
print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")

print()

# separator 옵션

print('P','Y','T','H','O','N', sep='')
print('010','7777','1234', sep="-")
print('kfxsmt','naver.com',sep='@')

print()


# end 옵션

print('Welcome to',end=' ')
print('IT News', end=' ')
print('Web site')

#file 옵션

import sys

print('Learn python',file=sys.stdout) #그냥 file 옵션이 있다 정도만 알아두기
print()

# format 사용 (d,s,f)

print('%s %s' %('one','two'))
print('{} {}' .format('one','two'))
print('{1}{0}'.format('one','two'))

# %s

print('%10s' % ('nice'))
print('{:>10}'.format('nice')) #오른쪽 정렬

print('%-10s' % ('nice'))
print('{:10}'.format('nice')) #왼쪽 정렬

print('{:_>10}'.format('nice')) #왼쪽 공백을 _로 채움
print('{:^10}'.format('nice')) #중앙 정렬

print('%.5s' % ('pythonstudy')) # 절삭 .5
print('{:10.5}'.format('pythonstudy'))

# %d

print('%d %d' % (1,2))
print('{0}{1}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42)) # 숫자는 문자열과 다르게 오른쪽 정렬됨 -> < 사용


# %f

print('%f' % (3.1454545545454))
print('%1.8f' % (3.1454545545454))
print('{:f}'.format(3.1454545545454))


print('{:06.2f}'.format(3.1454545545454)) #:x.yf = 정수부는 x자리 / 소수부는 y자리까지 출력하는 방법

# print(f) 로 format 하면 됨 return 제외ㄴ
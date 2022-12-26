# Chapter09_01

# 파이썬 파일 읽기 및 쓰기

# 읽기 모드 r, 쓰기 모드 w, 추가 모드 a, 텍스트 모드 t, 바이너리 모드 b
# 상대경로(../ ./) , 절대 경로('C:\\Django .....)

# 예제1
# 파일 읽기(Read)

f = open('./resource/it_news.txt', 'rt' , encoding = 'UTF-8')

# 속성 확인
print(dir(f))
# 인코딩 확인
print(f.encoding)
# 파일 이름
print(f.name)
# 모드 확인
print(f.mode)
# 반드시 close

f.close()

# 예제2

with open('./resource/it_news.txt', 'rt' , encoding = 'UTF-8') as f: #alias 주기
    c = f.read()
    # print(c)
    #print(iter(c)) # Iterable
    # print(list(c))
    
print()

# 예제3
# read() : 전체, read(10) : 10바이트만큼 읽는다

with open('./resource/it_news.txt', 'rt' , encoding = 'UTF-8') as f:
    c = f.read(20)
    print(c)
    c = f.read(20) # 커서가 존재, 마지막으로 어디까지 읽었는지 기억함 !
    print(c)
    f.seek(0,0) # (from,to)
    print(f.read(20))
    
# 예제4
# readline() : 한줄씩 읽기
with open('./resource/it_news.txt', 'rt' , encoding = 'UTF-8') as f:
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)
    
# 예제5 전처리, 정규표현식
# readlines() : 전체를 읽은 후 라인 단위 리스트로 전환
import time
with open('./resource/it_news.txt', 'rt' , encoding = 'UTF-8') as f:
    cts = f.readlines()
    print(cts)
    for c in cts:
        print(c)
       # time.sleep(2)
    
# 파일 쓰기 (write)
# 예제1
with open('./resource/contents1.txt', 'wt' , encoding = 'UTF-8') as f:
    f.write('I love python\n')
    
with open('./resource/contents1.txt', 'at' , encoding = 'UTF-8') as f:
    f.write('I love python\n')
    
# 예제3
# writelines : 리스트 -> 파일 (readlines의 반대)

with open('./resource/contents2.txt', 'wt' , encoding = 'UTF-8') as f:
    list_01 = ['Orange\n','Apple\n','Banana\n','Melon\n']
    f.writelines(list_01)
    
# 예제4
with open('./resource/contents3.txt', 'wt' , encoding = 'UTF-8') as f:
    print('Test txt Write', file = f) # 파일로 출력
    
    
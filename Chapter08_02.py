# Chapter08_02

# python external_fucntion 

# sys, pickle, shutil, temfile, time, random 

import sys
print(sys.argv)

# 강제 종료

# sys.exit()

# 파이썬 패키지 위치

print(sys.path)

# pickle : 객체 파일 쓰기

import pickle

f = open("test.txt", 'wb')
txt = {1: 'python', 2: 'java',3:'C#'}
pickle.dump(txt,f)
f.close()

# 읽기

f = open("test.txt", 'rb')
data = pickle.load(f)
print(data,type(data))
f.close()

# os : 환경 변수, 디렉토리(파일) 처리 관련, 운영체제 작업 관련
# mkdir , rmdir , rename 

import os
print(os.environ)

# 현재 경로

print(os.getcwd()) 

# time : 시간 관련 처리

import time

print(time.time())

print(time.localtime(time.time()))

print(time.ctime())

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

# 시간 간격 발생 (고의적으로)


# for i in range(5):
#     print(i)
#     time.sleep(1)

# random : 난수 리턴

import random

print(random.random()) # 0~1난수리턴

print(random.randint(1,45))   # 1~45
print(random.randrange(1,45)) # 1~44


# 섞기

d = [1,2,4,65,21,12,52,3]
random.shuffle(d)
print(d)

# 무작위 선택

result = random.choice(d)
print(result)

# webbrowser : 본인 OS의 웹 브라우저 실행

import webbrowser

webbrowser.open("http://google.com")
webbrowser.open_new("http://google.com")








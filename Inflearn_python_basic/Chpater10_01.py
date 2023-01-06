# Chpater10_01.py

import time

name = input("What is your name? ")

print('Hi,' + name, 'Enjoy game !')

print()

time.sleep(1)

print('Start Loading ..')

time.sleep(1.5)

# 정답 단어
word = "secret"

# 추측 단어
guesses = ''

# 기회
turns = 10

# 핵심
# 찬스 카운트가 남아 있을 경우
while turns > 0:
    # 실패 횟수
    failed = 0
    
    # 정답 단어 반복
    for char in word:
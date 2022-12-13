# Chapter03_05

# 범용적으로 가장 많이 사용 !!

# 딕셔너리 자료형(순서X ,키 중복X , 수정O, 삭제O)

# 선언 (여러가지로 할 수 있다 !)

dic_1 = {'name': 'Kim','Age': 20}
dic_2 = {2: 'python'}
dic_3 = {
        'Name': 'man',
        'Grade':'A'
}
dic_4 = dict([                # 복잡하지만 가장 정석적인 방법 -> 튜플안에 리스트 형대로 또 리스트 안에 튜플 형태로 key와 value값을 저장
        ('Name', 'man'),
        ('Age', 20),
        ('Grade' ,'A')
])


dic_5 = dict(                # 가장 편리하다고 느끼는 방법 !
        Name = 'man',
        Age = 20,
        Grade = 'A'
)


# 출력

print(dic_1['name'])
print(dic_1.get('name')) # get method 를 사용할 때는 값이 없으면 NONE을 출력하기 때문에 사용해야함!


# 딕셔너리 추가

dic_1['address'] = 'seoul'
print(dic_1)

# dick_keys , dick_values , dick_items : 반복분(__iter__ ) 에서 사용가능

print(dic_1.keys())
print(dic_1.values())
print(list(dic_1.items()))

print(dic_1.pop('name')) #key와 value 삭제
print(dic_1)
print(dic_1.popitem())
print(dic_1)
dic_6 = dict(
        name = 'junsoo',
        age = 20,
        belonging = 'roakf', 
        team = 3,
        members = 5
)

print(dic_6.popitem())
print(dic_6)
print(dic_6.popitem()) # 파이썬 버전 3.6이상에서는 마지막 item을 삭제하는 것으로 나옴
print(dic_6)


print ('members' in dic_6)


# 수정

dic_6.update(name='junsookim')
print(dic_6)
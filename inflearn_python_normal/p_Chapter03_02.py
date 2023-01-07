# Chpater03_02
# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence) , 반복(Iterator), 함수(Functions), 클래스(Class)
# 클래스 안에 정의할 수 있는(Built-in) Method


# Vector클래스로 반환하는것이 이해 X

# 클래스 예제 2

class Vector(object):
    
    def __init__(self, *args):
        '''
        Create a Vector, example : v = Vector(5, 10)
        '''
        if len(args) == 0:
            self._x , self._y = 0, 0
        else:
            self._x, self._y = args
        
    def __repr__(self):
        ''' Return Vector Informations'''
        return 'Vector(%r, %r)' % (self._x, self._y)
        
    def __add__(self, other):
        """Return Vector's add"""
        return Vector(self._x + other._x , self._y + other._y)
    
    
    def __mul__(self, z):
        """Return Vector's multiple"""
        return Vector(self._x * z, self._y * z)
    
    def __bool__(self):
        return bool(max(self._x, self._y)) # (0,0) 인것을 확인하는

# Vector Instance

v1 = Vector(5,7)
v2 = Vector(10,20)
v3 = Vector(1,2)
v4 = Vector()
v5 = Vector(0,0)

# 메직메소드 출력

print(v1 + v2 + v3)
print()
        
print(Vector.__add__.__doc__)        
print(Vector.__doc__)
print(Vector.__init__.__doc__)


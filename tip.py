# directory get set
import os
os.getcwd()     # get dir
os.chdir("dir") # change the dir

# 특정 기준으로 정렬을 하는 방법
# 1. 2차원 배열의 특정 값으로 배열하는 방법
test = [('a', 1), ('b', 2), ('c', 3)]
sorted(test, key= lambda test: test[1], reverse= True)

# 2. 이름표가 있는 객체에서 배열 지정하는 방법
class Test:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self): # class 실행시, print를 하기 위한 함수
        return repr((self.name, self.grade, self.age))

students_objects = [
    Test('HJH', 'G', '28'),
    Test('BSY', 'A', '32'),
    Test('HMH', 'S', '60')
]

sorted(students_objects, key= lambda tt: tt.age, reverse= True)

# enumerate : '세다'라는 의미

# namedTuple : 튜플 형태로 구조체를 저장하는 방법
# 좌표 평면 등을 나타낼 때 유용할 수 있음
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
P1 = Point(10, 20)

# asterisk : 기본적으로 곱하기를 의미 하지만, 가변 인자의 의미도 가지고 있음
# 함수의 매개 변수에서 * 사용 : tuple packing, ** 사용 : dict packing
# 변수 *를 사용 : tuple unpacking, ** dict unpacking : 함수의 입력 값, 변수, zip 에서 활용
def asterisk_test(a, *args):
    print(a, args)
    print(type(args))

asterisk_test(1,2,3,4,5)

def asterisk_test(a, **kargs):
    print(a, kargs)
    print(type(kargs))
asterisk_test(1, b=2, c=3, d=4, e=5, f=6)


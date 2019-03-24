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

## bfs 할 때, node를 방문할 때, check = True 를 해주어야 함
## 왜 그런지 모르겠으면, 2 -> 4 , 3 -> 4를 생각해보자.
## https://www.acmicpc.net/blog/view/70

# 구조체 만들기
from collections import namedtuple, deque
list_seq = deque()
Point = namedtuple('Point', ['x', 'y'])

# 정렬 복습!
class student:
    def __init__(self, korean, english, maths):
        self.korean  = korean
        self.english = english
        self.maths = maths

    def __repr__(self):
        return repr((self.korean, self.english, self.maths))


students_scores = {
    student(100, 50, 30),
    student(20, 30, 50),
    student(50, 60, 20),
}

sorted(students_scores, key= lambda tt: tt.maths, reverse = False)

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(x=1, y=10)


# sorted 함수 쓸 때. return 받아서 다시 할당 해주어야 함
# 분명 dict type 에서 return 받을 일이 생길꺼라고 생각

from collections import OrderedDict
dict_seq = OrderedDict()

dict_seq[1] = 30
dict_seq[2] = 20
dict_seq[3] = 10

dict_seq = sorted(dict_seq.items(), key = lambda tt : tt[1])

class test:
    def __init__(self, name, age, house):
        self.name = name
        self.age  = age
        self.house = house

    def __repr__(self):
        return repr((self.name, self.age, self.house))

student_test = {
    test('HJH', 28, 'bundang'),
    test('LMH', 27, 'bundang'),
    test('HMH', 60, 'bundang')
}

sorted(student_test, key = lambda tt : tt.age, reverse = False)

# 2개 이상의 정렬 조건을 추가하는 경우,
# ex) 국어 점수로 우선적으로 정렬한 후, 같으면 수학점수로 정렬하고 싶은 경우,
# sorted 함수의 key 값에 함수를 (국어, 점수) parameter로 setting 해 주면 된다
# ex) sorted(test, key = lambda x: (국어, 점수), reverse = False)

# 2019_03_23
# 진법 전환하기 : bin, oct, dec, hex
# 2, 8, 16 -> 10진법으로 전환
print(int('aa', 16))
print(int('56', 8))
print(int('1001', 2))

# 10진법 -> 2, 8, 16
# bin, hex, oct 함수  이용! : 내장 함수
a = 100
bin(100)[2:] # 결과 값 0b + 2진수로 나옴. 따라서 index 2번 부터 사용

# divmod : return 몫, 나머지

# ** 아스키 코드 <-> 숫자 변환
# 아스키코드번호 -> 문자 :  chr
# 문자열 -> 아스키코드번호 : ord
# 아스키 코드 65번 -> A ~  : 꼭 기억하자

# for 문의 활용
a = [(1,2), (2,3), (3,4)]
for (first, second) in a:
    print(first, second)

a      = [1,2,3,4]
result = [i for i in a if i % 2 == 0]
result = [a*b for a in range(1,6) for b in range(1,10) ]

# 입력 값이 몇개가 되는지 모를 때

def sum_many(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

# 초기화 하고 싶다면, 반드시 가장 뒤에 변수 배치
def say_myself(name, old, man = True):
    pass

# 여러개를 구분자로 자르기
import re
test = "50-50+40"
re.split('\W+', test)

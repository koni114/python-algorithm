# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
import sys
f = sys.stdin
testCases = int(f.readline())

for i in range(testCases):
    tmp = [ int(i) for i in f.readline().split() ]
# 골드바흐의 추측
import sys
from math import sqrt
from collections import deque
number = deque()
max_n = 0
f = sys.stdin

while(True):
    n = int(f.readline())
    max_n = max(n, max_n)
    if n == 0: break
    number.append(n)

result = deque()
arr = [i for i in range(max_n+1)]
arr[1] = 0

# 에라토스테네스의 체 만들기
# 1. n 크기의 배열 생성
# 2. 1, sqrt(n) 까지의 배수를 지우기
for i in range(2, int(sqrt(max_n))+1):
    for j in range(i+i, max_n+1, i):
        arr[j] = 0
arr_short = [i[0] for i in enumerate(arr) if i[1]]

for k in number:
    for i in arr_short:
        if arr[k-i]:
            print(str(k) + " = " + str(i) + " + "+ str(k-i))
            break

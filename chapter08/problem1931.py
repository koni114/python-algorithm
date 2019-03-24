# 회의실 배정
import sys
from collections import deque
f = sys.stdin
n = int(f.readline())
reserve = deque()
for i in range(n):
    reserve.append(list(map(int, f.readline().split())))
reserve = sorted(reserve, key = lambda x: (x[1], x[0]))
result = 0
start = 0
for (i, j) in reserve:
    if start <= i:
        result += 1
        start = j

print(result, end = "")
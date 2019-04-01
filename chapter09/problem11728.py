# 배열 합치기
import sys
from collections import deque
f = sys.stdin
N, M = map(int, f.readline().split())
arr1 = deque([int(i) for i in f.readline().split()])
arr2 = deque([int(i) for i in f.readline().split()])
result = deque()

while len(arr1) != 0 and len(arr2) != 0:
    if arr1[0] < arr2[0]:
        result.append(arr1.popleft())
    else:
        result.append(arr2.popleft())

while len(arr1) != 0:
    result.append(arr1.popleft())

while len(arr2) != 0:
    result.append(arr2.popleft())

print(*result, end = "")
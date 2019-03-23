# 버블 소트
from collections import deque
import sys

f = sys.stdin
n = int(f.readline())
arr = deque()
[arr.append((int(f.readline()), i)) for i in range(1, n+1)]
arr = sorted(arr, key = lambda x: x[0])
print(max([i[1][1] - i[0] for i in enumerate(arr)]), end = "")

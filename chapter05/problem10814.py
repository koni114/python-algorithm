# 나이순 정렬
import sys
from collections import deque
f = sys.stdin
n = int(f.readline())
arr = deque()
for i in range(n):
    tmp = [i for i in f.readline().split()]
    arr.append([int(tmp[0]), tmp[1], i])
arr = sorted(arr, key= lambda x: (x[0], x[2]))
[print(str(i[0]) + " " + i[1] ) for i in arr]
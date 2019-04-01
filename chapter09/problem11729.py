# 하노이 탑
import sys
from collections import deque
f = sys.stdin
n = int(f.readline())
result = deque()

def hanoi(start, end, size):
    empty = 6 - (start + end)
    if size == 1:
        result.append((start, end))
        return
    hanoi(start, empty, size-1)
    result.append((start, end))
    hanoi(empty, end,   size-1)

hanoi(1,3,n)
print(len(result))
[print(*i) for i in result]
# 수 묶기
import sys
from collections import deque
f   = sys.stdin
n   = int(f.readline())
arr1 = deque()
arr2 = deque()
zero   = 0
result = 0
for i in range(n):
    tmp = int(f.readline())
    if tmp > 0:1
        if tmp == 1: result += 1
        else: arr1.append(tmp)
    elif tmp < 0:
        arr2.append(tmp)
    else:
        zero += 1

arr1 = deque(sorted(arr1, reverse= True))
arr2 = deque(sorted(arr2))

if len(arr1) % 2 == 1:
    arr1.append(1)
if len(arr2) % 2 == 1:
    if zero:
        arr2.append(0)
    else:
        arr2.append(1)

while len(arr1) != 0 or len(arr2) != 0:
    if len(arr1) > 0:
        result += arr1.popleft() * arr1.popleft()
    if len(arr2) > 0:
        result += arr2.popleft() * arr2.popleft()

print(result, end = "")
# 오아시스 재결합
import sys
from collections import deque
f = sys.stdin
N = int(f.readline().strip())
arr = deque()
for i in range(N):
    arr.append(int(f.readline().strip()))

s = deque()
result = 0
s.append([arr[0], 1])

for i in range(1,N):
    tmp = [arr[i], 1]
    while len(s) != 0:
        if s[len(s)-1][0] <= tmp[0]:
            result += s[len(s)-1][1]
            if s[len(s)-1][0] == tmp[0]: tmp[1] += s[len(s)-1][1]
            s.pop()
        else:
            break

    if len(s) != 0: result += 1
    s.append(tmp)

print(result, end = "")
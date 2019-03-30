import sys
from collections import deque
f = sys.stdin
N,M = map(int, f.readline().split())
result = 0
before = deque()
after = deque()
for i in range(N): before.append(list(map(int, list(f.readline().strip()))))
for i in range(N): after.append(list(map(int, list(f.readline().strip()))))

if N < 3 or M < 3:
    if before == after:
        result = 0
    else:
        result = -1

else:
    for i in range(N-2):
        if before == after: break
        for j in range(M-2):
            if before == after: break
            if before[i][j] == after[i][j]:
                continue
            else:
                for k in range(3):
                    for l in range(3):
                        if before[i+k][j+l] == 1:
                            before[i+k][j+l] = 0
                        else:
                            before[i+k][j+l] = 1
                result += 1

if before != after:
    result = -1
print(result, end = "")
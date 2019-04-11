# 문자열 폭발
import sys
from collections import deque
f = sys.stdin
N = f.readline().strip()
A = list(f.readline().strip())
d1 = deque(N)
d2 = deque()
while len(d1) != 0:
    check = True
    d2.append(d1.popleft())
    if len(d2) >= len(A):
        for i in range(len(A)):
            if d2[-(len(A) - i)] != A[i]:
                check = False
                break
        if check: [d2.pop() for _ in range(len(A))]
if len(d2) != 0:
    print("".join(d2), end = "")
else:
    print("FRULA", end = "")
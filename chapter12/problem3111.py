# 검열
import sys
from collections import deque
f = sys.stdin
A = f.readline().strip()
T = f.readline().strip()

check = False
d1 = deque(T)
d2 = deque()
d3 = deque()


while len(d1) != 0:
    while len(d1) != 0:
        d2.append(d1.popleft())
        if len(d2) >= len(A):
            if all([A[i] == d2[-(len(A) - i)] for i in range(len(A))]):
                [d2.pop() for _ in range(len(A))]
                break

    if len(d1) == 0: check = True

    while len(d1) != 0:
        d3.appendleft(d1.pop())
        if len(d3) >= len(A):
            if all([A[i] == d3[i] for i in range(len(A))]):
                [d3.popleft() for _ in range(len(A))]
                break

if check:
    while len(d2) != 0:
        d3.appendleft(d2.pop())
        if len(d3) >= len(A):
            if all([A[i] == d3[i] for i in range(len(A))]):
                [d3.popleft() for _ in range(len(A))]
else:
    while len(d3) != 0:
        d2.append(d3.popleft())
        if len(d2) >= len(A):
            if all([A[i] == d2[-(len(A) - i)] for i in range(len(A))]):
                [d2.pop() for _ in range(len(A))]

print("".join(d2 + d3), end = "")
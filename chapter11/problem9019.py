# DSLR
import sys
from collections import deque
from copy import deepcopy
f = sys.stdin
n = int(f.readline().strip())
def bfs(A, B):
    if A == B: return ""
    check[A] = True
    check2[A] = ""
    q = deque()
    q.append(A)
    while len(q) != 0:
        a = q.popleft()
        b = check2[a]
        if a == B: return b
        c1 = (a*2) % 10000
        c2 = a-1
        if c2 == -1: c2 = 9999
        c3 = (a % 1000) * 10 + (a // 1000)
        c4 = (a // 10) + ((a % 10)*1000)
        if not check[c1]:
            check[c1] = True
            check2[c1] = b+"D"
            q.append(c1)
        if not check[c2]:
            check[c2] = True
            check2[c2] = b+"S"
            q.append(c2)
        if not check[c3]:
            check[c3] = True
            check2[c3] = b+"L"
            q.append(c3)
        if not check[c4]:
            check[c4] = True
            check2[c4] = b+"R"
            q.append(c4)


for i in range(n):
    check = [False for _ in range(10000)]
    check2 = [0 for _ in range(10000)]
    A, B = map(int, f.readline().split())
    print(bfs(A, B))
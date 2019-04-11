# 소수 경로
import sys
from collections import deque
f = sys.stdin
n = int(f.readline().strip())
check = [False for _ in range(10001)]
for i in range(2, 101):
    if not check[i]:
        j = 2
        while i*j <= 10000:
            check[i*j] = True
            j += 1

def bfs(A, B):
    q = deque()
    bfsCheck = [False for _ in range(10001)]
    if A == B: return 0
    q.append([A, 0])
    bfsCheck[A] = True

    while len(q) != 0:
        a,b = q.popleft()
        if a == B: return b
        for i in range(4):
            if i == 0: arr = list(range(1,10))
            else: arr = list(range(0,10))
            for j in arr:
                next = int(str(a)[:i] + str(j) + str(a)[i+1:])
                # print(next)
                if not bfsCheck[next] and not check[next]:
                    bfsCheck[next] = True
                    q.append([next, b+1])




for i in range(n):
    A,B = map(int, f.readline().split())
    print(bfs(A,B))
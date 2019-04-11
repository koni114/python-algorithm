# 숨바꼭질
import sys
from collections import deque
f = sys.stdin
n,m = map(int, f.readline().split()) # n : 수빈이 위치, m : 동생 위치

def bfs(n, m):
    q = deque()
    if n == m: return 0
    check = [False for _ in range(1000001)]
    q.append([n, 0])
    while len(q) != 0:
        a,b = q.popleft()
        if a == m: return b
        else:
            if a+1 <= 1000000 and not check[a+1]:
                check[a+1] = True
                q.append([a+1, b+1])
            if a-1 >= 0 and not check[a-1]:
                check[a-1] = True
                q.append([a-1, b+1])
            if a*2 <= 1000000 and not check[a*2]:
                check[a*2] = True
                q.append([a*2, b+1])

print(bfs(n, m), end = "")


test = "1234"
test[:0] + str(9) +test[1:]

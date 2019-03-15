# 순열 사이클
# 문제가 너무 길어 생략
import sys
from collections import deque
f = sys.stdin
n = int(f.readline())
for i in range(n):
    node = int(f.readline())
    result = 0
    check = [False] * (node+1)
    stack = deque()
    cycle = [int(i) for i in f.readline().split()]
    cycle.insert(0,0)
    for j in range(1,node+1):
        if not check[j]:
            number = 1
            while(True):
                check[j] = number
                if check[cycle[j]] == 1:
                    result += 1
                    break
                elif check[cycle[j]] == 0:
                    number += 1
                    j = cycle[j]
                else:
                    break

    print(result)



# 가장 가까운 두 점
import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
f = sys.stdin
n = int(f.readline().strip())
arr = deque()
for _ in range(n): arr.append(list(map(int, f.readline().split())))
arr = sorted(arr, key= lambda x : x[0])

def dista(a, b):
    a1, a2 = arr[a]
    b1, b2 = arr[b]
    return ((a1-b1) ** 2)+((a2 - b2) ** 2)

def bruteForce(x1, x2):
    len_min = -1
    for i in range(x1, x2):
        for j in range(i+1, x2+1):
            tt = dista(i, j)
            if len_min == -1 or len_min > tt:
                len_min = tt
    return len_min


def direction(x1, x2):
    if (x2 - x1 + 1) <= 3:
        return bruteForce(x1, x2)

    mid = (x1 + x2) // 2
    L1 = direction(x1, mid)
    L2 = direction(mid+1, x2)
    m = min(L1, L2)

    temp = deque()
    for i in range(x1, x2+1):
        d = arr[i][0] - arr[mid][0]
        if d*d < m:
            temp.append(arr[i])

    temp = sorted(temp, key=lambda tt : tt[1])
    for i in range(len(temp)-1):
        for j in range(i+1, len(temp)):
            min_value = dista(i, j)
            if m > min_value:
                m = min_value
            else: break

    return m

print(direction(0, n-1), end = "")

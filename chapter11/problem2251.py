import sys
from collections import deque, defaultdict
f = sys.stdin
A, B, C = map(int ,f.readline().split())
startWater = (A,B,C)
nextArr = [[i, j] for i in range(1,4) for j in range(1,4) if i != j]
result  = dict()
check   = defaultdict(lambda : 0)


def changeWater(arr, start, end):
    arr = list(arr)

    a = arr[start-1]
    b = arr[end-1]
    if a > startWater[end-1] - b:
        arr[start-1] = a - (startWater[end-1]-b)
        arr[end-1]   = startWater[end-1]
    else:
        arr[start-1] = 0
        arr[end-1]   = a+b

    return tuple(arr)

def bfs(arr):
    d = deque()
    d.append(arr)
    check[arr] = True

    while len(d) != 0:
        tmp = d.popleft()
        if tmp[0] == 0:
            result[tmp[2]] = 1

        for (start, end) in nextArr:
            if tmp[start-1] != 0:
                next = changeWater(tmp, start, end)
                if not check[next]:
                    check[next] = True
                    d.append(next)

bfs((0,0,C))
print(*sorted(result), end = "")

# 토마토
import sys
from collections import deque
f = sys.stdin
w, h = [int(i) for i in f.readline().split()]
graph = []
check = []
result = 0
xDir = [1, -1, 0, 0]
yDir = [0, 0, 1, -1]

def bfs(queue):
    global result
    while(len(queue) != 0):
        y, x, n = queue.pop()
        for i in range(4):
            yTmp = y + yDir[i]
            xTmp = x + xDir[i]
            if yTmp >= 0 and yTmp < h and xTmp >= 0 and xTmp < w:
                if graph[yTmp][xTmp] == 0:
                    queue.appendleft((yTmp,xTmp,n+1))
                    check[yTmp][xTmp] = n+1
                    graph[yTmp][xTmp] = 1
                    if result < n+1:
                        result = n+1

    for i in range(h):
        if 0 in graph[i]: result = -1
    print(result)


for i in range(h):
    graph.append([int(i) for i in f.readline().split()])
    check.append([0] * w)

queue = deque()

for i in range(h):
    for j in range(w):
        if graph[i][j] == 1:
            queue.appendleft((i,j,0))

bfs(queue)


# 마지막으로 0이 있는지 반드시 check 해서 있으면 -1 return

import sys
from collections import deque
f = sys.stdin
n = int(f.readline())
graph = {}
check = [False] * (n+1)
result = [0] * (n+1)


for i in range(1,n+1): graph[i] = []
for i in range(n-1):
    a, b = [int(i) for i in f.readline().split()]
    graph[a].append(b)
    graph[b].append(a)

def bfs(startNode):
    queue = deque()
    check[startNode] = True
    queue.appendleft(startNode)

    while(len(queue) != 0):
        number = queue.pop()
        for i in graph[number]:
            if not check[i]:
                check[i] = True
                result[i] = number
                queue.appendleft(i)

bfs(1)
[print(i) for i in result[2:]]

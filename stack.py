import sys
from collections import deque
f = sys.stdin
n,m, startNode  = map(int, f.readline().split()) # n 정점, m 간선, startNode : 시작 노드
arr = deque([[] for i in range(n+1)])
for i in range(m):
    a,b = map(int, f.readline().split())
    arr[a].append(b)
    arr[b].append(a)

stack = deque()
check = [False for _ in range(n+1)]

def dfs(currNode):
    stack.append(currNode)
    check[currNode] = True
    print(currNode, end = " ")
    for i in arr[currNode]:
        if not check[i]:
            dfs(i)
    if len(stack) != 0: stack.pop()

dfs(startNode)

from collections import defaultdict
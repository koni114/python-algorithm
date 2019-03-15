# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.
# 1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2
#
# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.
# (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

# 6 5
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6

# 답 : 2

# 6 8
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6
# 5 4
# 2 4
# 2 3

# 답 : 1

import sys
from collections import deque
f = sys.stdin

# var init
graph = {}
result = 0

node, edge = [ int(i) for i in f.readline().split()]
check = [False] * (node+1)
queue = deque()
for i in range(1, node+1): graph[i] = []
for i in range(edge):
    start, end = [int(i) for i in  f.readline().split() ]
    graph[start].append(end)
    graph[end].append(start)

def bfs(start):
    check[start] = True
    queue.appendleft(start)

    while(len(queue) != 0):
        n = queue.pop()
        for i in graph[n]:
            if not check[i]:
                queue.appendleft(i)
                check[i] = True

for i in range(1, node+1):
    if not check[i]:
        bfs(i)
        result += 1

print(result, end = "")
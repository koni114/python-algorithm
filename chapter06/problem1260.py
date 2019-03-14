# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
#
# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000),
# 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
#
# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다.
# V부터 방문된 점을 순서대로 출력하면 된다.

# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4


from collections import deque
import sys

f = sys.stdin
node, edge, start = [int(i) for i in f.readline().split()]
graph = {}
check = [False] * (node+1)
result = ""

# making graph
for i in range(1,node+1):
    graph[i] = []

for i in range(edge):
    startNode, endNode = [int(i) for i in f.readline().split()]
    graph[startNode].append(endNode)
    graph[endNode].append(startNode)

for i in range(1,node+1):
    graph[i] = sorted(graph[i])

# print(graph)

# dfs
stack = deque()
def dfs(start):
    # start node 를 stack에 넣는다
    stack.append(start)
    check[start] = True
    global result
    result = result + str(start) + " "
    for i in graph[start]:
        if not check[i]:
            dfs(i)
    stack.pop()
dfs(start)
print(result)

check = [False] * (node+1)
result = ""

queue = deque()
def bfs(start):
    queue.appendleft(start)
    check[start] = True
    global result
    result = str(start) + " "

    while(len(queue) != 0):
        for i in graph[queue.pop()]:
            if not check[i]:
                result += (str(i) + " ")
                queue.appendleft(i)
                check[i] = True
bfs(start)
print(result)


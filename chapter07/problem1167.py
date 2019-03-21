# 트리의 지름
# 트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. 트리의 지름을 구하는 프로그램을 작성하시오.
# 트리가 입력으로 주어진다.
#  먼저 첫 번째 줄에서는 트리의 정점의 개수 V가 주어지고 (2≤V≤100,000)둘째 줄부터 V개의 줄에 걸쳐 간선의 정보가 다음과 같이 주어진다.
#  (정점 번호는 1부터 V까지 매겨져 있다고 생각한다)
#
# 먼저 정점 번호가 주어지고, 이어서 연결된 간선의 정보를 의미하는 정수가 두 개씩 주어지는데,
# 하나는 정점번호, 다른 하나는 그 정점까지의 거리이다.
# 예를 들어 네 번째 줄의 경우 정점 3은 정점 1과 거리가 2인 간선으로 연결되어 있고, 정점 4와는 거리가 3인 간선으로 연결되어 있는 것을 보여준다.
# 각 줄의 마지막에는 -1이 입력으로 주어진다. 주어지는 거리는 모두 10,000 이하의 자연수이다.

# 5
# 1 3 2 -1
# 2 4 4 -1
# 3 1 2 4 3 -1
# 4 2 4 3 3 5 6 -1
# 5 4 6 -1

# 11

#
import sys
from collections import deque
f = sys.stdin
n = int(f.readline())
graph = {}
check = [False] * (n+1)

for i in range(1,n+1): graph[i] = []

for i in range(n):
    tmp = [int(j) for j in f.readline().split() ]
    for k in range(1, len(tmp)-1, 2):
        graph[tmp[0]].append((tmp[k], tmp[k+1]))

# 1부터 시작하여, 가장 긴 값의 노드를 찾는다
def bfs(start):
    queue = deque()
    finalResult = 0
    finalNode = 0
    check[start] = True
    queue.appendleft((start, 0))

    while(len(queue) != 0):
        node, result = queue.pop()
        for i in graph[node]:
            if not check[i[0]]:
                tmpLen = result + i[1]
                check[i[0]] = True
                queue.appendleft((i[0], tmpLen))
                if finalResult < tmpLen:
                    finalResult = tmpLen
                    finalNode   = i[0]
    return (finalNode, finalResult)

startNode = bfs(list(graph.keys())[0])[0]
check = [0] * (n+1)
print(bfs(startNode)[1], end = "")


# 찾은 노드에서 다시 제일 긴 지름을 찾으면 됨


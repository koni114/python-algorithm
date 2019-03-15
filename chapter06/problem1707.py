# 이분 그래프
# 그래프의 정점의 집합을 둘로 분할하여,
# 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때,
# 그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.
# 그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

# 입력은 여러 개의 테스트 케이스로 구성되어 있는데,
# 첫째 줄에 테스트 케이스의 개수 K(2≤K≤5)가 주어진다.
# 각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V(1≤V≤20,000)와
# 간선의 개수 E(1≤E≤200,000)가 빈 칸을 사이에 두고 순서대로 주어진다.
# 각 정점에는 1부터 V까지 차례로 번호가 붙어 있다. 이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데,
# 각 줄에 인접한 두 정점의 번호가 빈 칸을 사이에 두고 주어진다.

# 출력
# K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다

# 2
# 3 2
# 1 3
# 2 3
# 4 4
# 1 2
# 2 3
# 3 4
# 4 2

# YES
# NO

# 흠

import sys
from collections import deque
f = sys.stdin
n = int(f.readline())

for i in range(n):
    node, edge = [ int(i) for i in f.readline().split()]
    graph = {}
    result = "YES"
    check = [False] * (node+1)
    for j in range(1, node+1):
        graph[j] = []

    for j in range(edge):
        startNode, endNode = [int(k) for k in f.readline().split()]
        graph[startNode].append(endNode)
        graph[endNode].append(startNode)


    def bfs(start):
        queue = deque()
        number = 1
        global result
        check[start] = number
        queue.appendleft(start)

        while(len(queue) != 0):
            m = queue.pop()
            number = check[m]
            for l in graph[m]:
                if check[l] == (3-number):
                    continue
                elif check[l] == number:
                    result = "NO"
                else:
                    queue.appendleft(l)
                    check[l] = (3-number)

    for j in range(1, node+1):
        if not check[j]:
            bfs(j)

    print(result)

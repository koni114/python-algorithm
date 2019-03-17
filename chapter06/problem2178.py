# 미로 탐색
# N×M크기의 배열로 표현되는 미로가 있다.
#
# 1	0	1	1	1	1
# 1	0	1	0	1	0
# 1	0	1	0	1	1
# 1	1	1	0	1	1

# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소
# 의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

# 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

# 입력1
# 4 6
# 101111
# 101010
# 101011
# 111011

# 출력!
# 15

# 입력2
# 4 6
# 110110
# 110110
# 111111
# 111101

# 출력 2
# 9
import sys
from collections import deque
f = sys.stdin
graph = []
xDir = [1, -1, 0, 0]
yDir = [0, 0, 1, -1]

def bfs(y, x):
    queue = deque()
    queue.appendleft((y,x,1))
    graph[y][x] = 0

    while(len(queue) != 0):
        y, x, n = queue.pop()
        if y == h-1 and x == w-1:
            return n
        for i in range(4):
            yTmp = y + yDir[i]
            xTmp = x + xDir[i]
            if yTmp >= 0 and yTmp < h and xTmp >= 0 and xTmp < w:
                if graph[yTmp][xTmp]:
                    graph[yTmp][xTmp] = 0
                    queue.appendleft((yTmp, xTmp, n+1))




h, w = [int(i) for i in f.readline().split()]
for i in range(h):
    graph.append([int(i) for i in f.readline().strip() ])
print(bfs(0, 0))

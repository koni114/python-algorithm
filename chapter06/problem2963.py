# 섬의 개수
# 정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.

# 한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다.
# 두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러쌓여 있으며, 지도 밖으로 나갈 수 없다.

# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.
# 둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.
# 입력의 마지막 줄에는 0이 두 개 주어진다.

# 각 테스트 케이스에 대해서, 섬의 개수를 출력한다.
import sys
from collections import deque
f = sys.stdin
xDir = [1,-1,0,0,1,-1,-1,1]
yDir = [0,0,1,-1,1,-1,1,-1]

def bfs(j, i):
    queue = deque()
    graph[j][i] = 0
    queue.appendleft((j,i))

    while(len(queue) != 0):
        y, x = queue.pop()
        for k in range(8):
            yTmp = y + yDir[k]
            xTmp = x + xDir[k]
            if xTmp >= 0 and xTmp < w and yTmp >= 0 and yTmp < h:
                if graph[yTmp][xTmp]:
                    queue.appendleft((yTmp,xTmp))
                    graph[yTmp][xTmp] = 0


while(True):
    input_str = f.readline().strip()
    if input_str == "0 0": break

    w, h = [ int(i) for i in input_str.split() ]
    graph = []
    island = 0
    for i in range(h): graph.append([int(i) for i in f.readline().split()])
    for i in range(w):
        for j in range(h):
            if graph[j][i]:
                bfs(j,i)
                island += 1
    print(island)
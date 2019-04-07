# 단지 번호 붙이기
# <그림 1>과 같이 정사각형 모양의 지도가 있다.
# 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
# 철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고,
# 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우,
# 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다.

# <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다.
# 지도를 입력하여 단지수를 출력하고,
# 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

# 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

# 첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

import sys
from collections import deque, namedtuple

f = sys.stdin
n = int(f.readline())
graph = {}
house_seq = []
check = []
xDir = [0, 0, 1, -1]
yDir = [1, -1, 0, 0]

for i in range(n):
    graph[i] = [int(j) for j in f.readline().strip()]
    check.append([False] * n)

Point = namedtuple('Point', ['x', 'y'])

def bfs(p):
    q = deque()
    house = 1
    q.appendleft(p)
    check[p.x][p.y] = True

    while(len(q) != 0):
        pTmp = q.pop()
        for k in range(4):
            xTmp, yTmp = pTmp.x + xDir[k], pTmp.y + yDir[k]
            if xTmp >= 0 and xTmp <= n-1 and yTmp >= 0 and yTmp <= n-1:
                if not check[xTmp][yTmp] and graph[xTmp][yTmp]:
                    house += 1
                    check[xTmp][yTmp] = True
                    q.appendleft(Point(xTmp, yTmp))
    return house

for i in range(n):
    for j in range(n):
        if not check[i][j] and graph[i][j]:
            house_seq.append(bfs(Point(i, j)))

print(len(house_seq))
[print(i) for i in sorted(house_seq)]




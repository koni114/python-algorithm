# 쿼드트리
import sys
sys.setrecursionlimit(10 ** 6)
from collections import deque
f = sys.stdin
n = int(f.readline())
quadTree = []
result = deque()
for _ in range(n):
    quadTree.append(list(map(int, list(f.readline().strip()))))

def check(x,y,size):
    tmp = quadTree[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if tmp != quadTree[i][j]:
                return False
    return True


def TreeCheck(x, y, size):
    if size == 1:
        result.append(str(quadTree[x][y]))
        return
    if check(x,y,size):
        result.append(str(quadTree[x][y]))
    else:
        result.append("(")
        half_size = size // 2
        TreeCheck(x, y,half_size)
        TreeCheck(x, y+half_size, half_size)
        TreeCheck(x+half_size, y, half_size)
        TreeCheck(x+half_size, y+half_size, half_size)
        result.append(")")

TreeCheck(0,0,n)
print("".join(result), end = "")
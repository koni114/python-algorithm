# 별 찍기 - 10
import sys
sys.setrecursionlimit(10 ** 6)
f = sys.stdin
n = int(f.readline().strip())
star = []
for i in range(n):
    star.append([" "] * n)

def starPoint(x, y, size):
    if size == 1:
        star[x][y] = "*"
        return

    # 9등분으로 자르기
    tmp = size // 3
    starPoint(x,y,tmp)
    starPoint(x,y+tmp,tmp)
    starPoint(x,y+(2*tmp), tmp)
    starPoint(x+tmp,y, tmp)
    starPoint(x+tmp,y+(2*tmp), tmp)
    starPoint(x+(2*tmp),y, tmp)
    starPoint(x+(2*tmp), y+tmp, tmp)
    starPoint(x+(2*tmp), y+(2*tmp), tmp)

starPoint(0,0,n)
[print("".join(i)) for i in star]


import math
math.log2()
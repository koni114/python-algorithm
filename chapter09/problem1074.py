# Z
import sys
sys.setrecursionlimit(10**6)
f = sys.stdin
N,r,c = map(int, f.readline().split())
xArray = [0,0,1,1]
yArray = [0,1,0,1]

def Zfind(x,y, size, startValue):
    global result
    if size == 1:
        for i in range(4):
            if (x+xArray[i]) == r and (y+yArray[i]) == c:
                print(startValue, end = "")
        return
    tmp = size // 2
    tmp2 = size * size // 4

    if r < x+tmp and c < y+tmp:    Zfind(x,     y,     tmp,  startValue)
    elif r < x+tmp and c >= y+tmp: Zfind(x,     y+tmp, tmp, startValue+(tmp2))
    elif r >= x+tmp and c < y+tmp: Zfind(x+tmp, y,     tmp, startValue+(tmp2*2))
    else:                          Zfind(x+tmp, y+tmp, tmp, startValue+(tmp2*3))

Zfind(0,0, 2 ** N, 0)
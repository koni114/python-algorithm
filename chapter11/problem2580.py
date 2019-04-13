# 스도쿠 ** 중요
import sys
sys.setrecursionlimit(10 ** 6)
c    = [[False for _ in range(10)] for _ in range(10)]
c2   = [[False for _ in range(10)] for _ in range(10)]
c3   = [[False for _ in range(10)] for _ in range(10)]
a    = []

f= sys.stdin
for i in range(9):
    tmp = list(map(int, f.readline().split()))
    a.extend(tmp)
    for j in range(9):
        c[i][tmp[j]] = True
        c2[j][tmp[j]] = True
        c3[((i//3)*3)+(j//3)][tmp[j]] = True

def check(i):

    if i == 81:
        [print(*a[i:i + 9]) for i in range(0, 72, 9)]
        print(*a[72:81], end = "")
        sys.exit(0)
    if a[i] != 0:
        check(i+1)
        return
    else:
        x = i // 9
        y = i % 9
        for j in range(1,10):
            if not c[x][j] and not c2[y][j] and not c3[(x//3)*3 + y//3][j]:
                a[i] = j
                c[x][j] = c2[y][j] = c3[((x//3)*3) + (y//3)][j] = True
                check(i+1)
                a[i] = 0
                c[x][j] = c2[y][j] = c3[((x//3)*3) + (y//3)][j] = False
check(0)



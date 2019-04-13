# N-Queen
import sys
sys.setrecursionlimit(10 ** 6)
f = sys.stdin
N = int(f.readline())
checkCol = [False for _ in range(N)]
checkRight = [False for _ in range(2*N)]
checkLeft  = [False for _ in range(2*N)]
a = [[False for _ in range(N)] for _ in range(N)]
result = 0
check = 0
def queen(num):
    global result
    global N
    global check
    check += 1
    if num >= N:
        result += 1

    for j in range(N):
        if not checkCol[j] and not checkRight[(N-1)+(j-num)] and not checkLeft[num+j] and not a[num][j]:
            a[num][j] = True
            checkCol[j] = True
            checkRight[(N - 1) + (j - num)] = True
            checkLeft[num + j] = True
            tmp = num+1
            queen(tmp)
            a[num][j] = False
            checkCol[j] = False
            checkRight[(N - 1) + (j - num)] = False
            checkLeft[num + j] = False

queen(0)
print(result, end = "")

checkDict = 
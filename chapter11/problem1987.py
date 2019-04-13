# 알파벳 : 재귀적 알고리즘, 답은 나오는데, 시간초과
# why ? 기본적으로 재귀적 함수는 성능 저하 문제가 심각하게 나타난다. 따라서 왠만하면 deque를 이용한 문제를 사용
import sys
import timeit

from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
f = sys.stdin
R, C = map(int, f.readline().split())
check = []
arr = []
xArray = [1,-1,0,0]
yArray = [0,0,1,-1]
checkDict = [0 for _ in range(30)]
result = 0
for i in range(R): check.append([False for _ in range(C)])
arr = [list(map(lambda x: ord(x)-65,input())) for i in range(R)]

checkNum = 0
check[0][0] = True
checkDict[arr[0][0]] = 1

def dfs(x, y, count):
    global result
    global checkNum
    checkNum += 1
    for i in range(4):
        xTmp = x + xArray[i]
        yTmp = y + yArray[i]
        if xTmp >= 0 and xTmp <= R-1 and yTmp >= 0 and yTmp <= C-1:
            if not check[xTmp][yTmp] and not checkDict[arr[xTmp][yTmp]]:
                check[xTmp][yTmp] = True
                checkDict[arr[xTmp][yTmp]] = 1
                dfs(xTmp, yTmp, count+1)
                check[xTmp][yTmp] = False
                checkDict[arr[xTmp][yTmp]] = 0

    result = max(result, count)
    return

dfs(0, 0, 1)
print(result, end = "")
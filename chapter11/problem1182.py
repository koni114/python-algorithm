# 부분수열의 합
import sys
sys.setrecursionlimit(10 ** 6)
f    = sys.stdin
N, S = map(int, f.readline().split())
arr  = sorted(list(map(int, f.readline().split())))
result = 0

def check(currValue, currIdx, t):
    global N, S, result
    if currIdx == N:
        if currValue == S and t >= 1:
            result += 1
        return

    check(currValue+arr[currIdx], currIdx + 1, t+1)
    check(currValue             , currIdx + 1, t)
    return

check(0, 0, 0)
print(result, end = "")
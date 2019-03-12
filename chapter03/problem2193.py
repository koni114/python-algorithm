import sys
f = sys.stdin
n = int(f.readline())
dp = []
dp.append(0)

for i in range(1,n+1):
    if i == 1: dp.append([0,1])
    elif i == 2: dp.append([1,0])
    else:
        dp.append([sum(dp[i-1]),dp[i-1][0]])

print(sum(dp[n]), end = "")


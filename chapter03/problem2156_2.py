# 포도주 시식
# dp[i][j] = i번째 잔 일때 i-1까지 연속 j잔을 먹을 경우,
# [max(dp[i-2]) + wine[i], dp[i-1][0] + wine[i], dp[i-1][1]]

import sys
f = sys.stdin
n = int(f.readline())
wine = [0]
dp = [0]
for i in range(n): wine.append(int(f.readline()))
for i in range(1, n+1):
    if i == 1:
        dp.append([wine[1], 0, 0])
    elif i == 2:
        dp.append([wine[2], sum(wine[1:3]), 0])
    else:
        dp.append([max(dp[i-2]) + wine[i], dp[i-1][0] + wine[i], dp[i-1][1]])

print(max(dp[n]), end = "")
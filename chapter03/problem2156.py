# 이렇게 풀면 안되는 것이였음.
# 포도주 시식의 핵심은, 안먹는 시점을 기준으로 dp[i] 를 적용하면 되는 것이였음

# D[i] = i번째까지 포도주를 마셨을 때 마실 수 있는 최대 양
# max(D[i-1], D[i-2] + A[i], D[i-3] + A[i-1] + A[i])

import sys
f = sys.stdin
n = int(f.readline())
wine = [0]
for i in range(n):
    wine.append(int(f.readline()))

dp = []
dp.append(0)

for i in range(1, n+1):
    if i == 1: dp.append([0, wine[1]])
    elif i == 2: dp.append([wine[1], wine[1] + wine[2]])
    elif i == 3: dp.append([dp[2][1], max(wine[1],wine[2]) + wine[3]])
    else:
        dp.append([max(dp[i-1][1], dp[i-2][1]), max(wine[i-1]+max(dp[i-3]), dp[i-2][1]) + wine[i]])

print(max(dp[n]), end = "")


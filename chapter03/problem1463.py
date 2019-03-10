# 1로 만들기
import sys
f = sys.stdin
n = int(f.readline())
dp = []
dp.append(0) # 1인 경우,

for i in range(1,n+1):
    if i == 1: dp.append(0)
    elif i == 2: dp.append(1)
    elif i == 3: dp.append(1)
    else:
        min_value = 1000000
        if i % 3 == 0: min_value = dp[i//3] + 1
        if i % 2 == 0: min_value = min(min_value, (dp[i//2] + 1))
        min_value = min(min_value, dp[i-1]+1)
        dp.append(min_value)

print(dp[n], end = "")


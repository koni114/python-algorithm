import sys
f = sys.stdin
n = int(f.readline())
dp = []
dp.append(0)
for i in range(1,n+1):
    if i == 1: dp.append(1)
    elif i == 2: dp.append(2)
    else: dp.append(((dp[i-1] % 10007)+ (dp[i-2] % 10007)) % 10007)
print(dp[n], end = "")
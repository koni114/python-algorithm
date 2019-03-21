# 가장 긴 증가하는 수열
# dp[i] = i를 포함할때 제일 긴 수열
import sys
f = sys.stdin
n = int(f.readline())
number = [ int(i) for i in f.readline().split()]
dp = []

for i in range(n):
    if i == 0: dp.append(1)
    else:
        max_n = 0
        for j in range(i):
            if number[i] > number[j]:
                max_n = max(max_n, dp[j])
        dp.append(max_n + 1)

print(max(dp), end = "")

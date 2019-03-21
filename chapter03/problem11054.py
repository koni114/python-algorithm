# 가장 긴 바이토닉 수열
# dp[i]  = i를 포함할때 제일 긴 증가 수열
# dp2[i] = i를 포함할떄 제일 긴 감소 수열
import sys
from collections import deque

f = sys.stdin
n = int(f.readline())
number = [ int(i) for i in f.readline().split()]
dp = []
dp2 = deque()
result = 0
for i in range(n):
    if i == 0: dp.append(1)
    else:
        max_n = 0
        for j in range(i):
            if number[i] > number[j]:
                max_n = max(max_n, dp[j])
        dp.append(max_n + 1)


for i in range(n-1, -1, -1):
    if i == n-1: dp2.appendleft(1)
    else:
        max_n = 0
        for j in range(n-1, i, -1):
            if number[i] > number[j]:
                max_n = max(max_n, dp2[-((n-1)-j+1)])
        dp2.appendleft(max_n + 1)

for i in range(n):
    result = max(result, (dp[i] + dp2[i] -1))
print(result)

# 계단 오르기
import sys
from collections import deque
f = sys.stdin
n = int(f.readline())
dp = deque()
number = deque()
for i in range(n):
    number.append(int(f.readline()))

for i in range(n):
    if i == 0:
        dp.append([number[i],0,0])
    elif i == 1:
        dp.append([number[i], number[i]+number[i-1],0])
    else:
        dp.append([max(dp[i-2][0:2])+number[i], dp[i-1][0]+number[i], dp[i-1][1]])

print(max(dp[n-1][0:2]), end = "")

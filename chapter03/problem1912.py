# 연속합
import sys
from collections import deque
f = sys.stdin
n = int(f.readline())
number = [int(i) for i in f.readline().split() ]
dp = deque()

for i in range(n):
    if i == 0: dp.append(number[i])
    else:
        dp.append(max(dp[i-1]+number[i], number[i]))
print(max(dp), end = "")

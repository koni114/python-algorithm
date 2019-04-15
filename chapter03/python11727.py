# 2×n 타일링 2
# 2×n 직사각형을 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
# 아래 그림은 2×17 직사각형을 채운 한가지 예이다.

# 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)
# 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

# dp[i] = 2*i 일 때, 타일로 채울 수 있는 경우의 수
# dp[i] = dp[i] + dp[i-2]*2

import sys
f = sys.stdin
n = int(f.readline())
dp = []
dp.append(0)
for i in range(1, n+1):
    if i == 1: dp.append(1)
    elif i == 2: dp.append(3)
    else:
        dp.append((dp[i-1] % 10007 + (dp[i-2]*2) % 10007) % 10007)

print(dp[n])
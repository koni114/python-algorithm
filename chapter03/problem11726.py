# 2×n 타일링
# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
# 아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.

# 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)
# 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

# dp[i] = 2*i일 때, 직사각형 채우는 방법
# dp[i] = dp[i-1] + dp[i-2]

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
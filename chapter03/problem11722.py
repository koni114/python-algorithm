# 가장 긴 감소하는 부분 수열
# 수열 A가 주어졌을 때, 가장 긴 감소하는 부분 수열을 구하는 프로그램을 작성하시오.
#
# 예를 들어, 수열 A = {10, 30, 10, 20, 20, 10} 인 경우에 가장 긴 감소하는 부분 수열은 A = {10, 30, 10, 20, 20, 10}  이고, 길이는 3이다.

# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

# 첫째 줄에 수열 A의 가장 긴 감소하는 부분 수열의 길이를 출력한다.

# dp[i] = i를 포함할때 제일 긴 수열
# dp[i] = dp[j]+1 (0<= j <=i-1)

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
            if number[i] < number[j]:
                max_n = max(max_n, dp[j])
        dp.append(max_n + 1)

print(max(dp), end = "")

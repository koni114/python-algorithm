# 쉬운 계단 수
# 45656이라는 수를 보자,
# 이 수는 인접한 모든 자리수의 차이가 1이 난다. 이런 수를 계단 수라고 한다.
# 세준이는 수의 길이가 N인 계단 수가 몇 개 있는지 궁금해졌다.
# N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구하는 프로그램을 작성하시오. (0으로 시작하는 수는 없다.)

# 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.
# 첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.

# 1 -> 9
# 2 -> 17

import sys
f = sys.stdin
n = int(f.readline())
dp = []
dp.append(0)
dp.append([1]*9)

for i in range(2, n+1):
    dp_sub = []
    for j in range(10):
        if j == 9: dp_sub.append(dp[i-1][j-1])
        elif j == 0: dp_sub.append(dp[i-1][j+1])
        else:
            dp_sub.append(dp[i-1][j-1] + dp[i-1][j+1])
    dp.append(dp_sub)

if n == 1: print(9, end = "")
else:
    print(sum(dp[n][1:]) % 1000000000 , end = "")


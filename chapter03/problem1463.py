# 1로 만들기
# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

# 첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.
# 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

# 풀이 방법 : dp문제
# dp[i] = 숫자 i일 때, 시작 값에서 최소의 연산을 이용한 횟 수
# dp[i] = min(dp[i//3] + 1, dp[i//2]+1, dp[i-1]+1)


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


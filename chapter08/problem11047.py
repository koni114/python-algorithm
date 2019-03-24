# 동전 0
# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

# 첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.
# 10 4200
# 1
# 5
# 10
# 50
# 100
# 500
# 1000
# 5000
# 10000
# 50000

# dp[i] = i원일 때 동전 최소 개수
# dp[i] = min(dp[i-A] + 1)
import sys
from collections import deque, defaultdict
f = sys.stdin
n, value = map(int, f.readline().split())
result = 0
coin = deque()
for i in range(n):
    coin.append(int(f.readline()))

for i in range(n-1, -1, -1):
    if  value // coin[i] != 0:
        result += value // coin[i]
        value = value % coin[i]
    if value == 0:
        break

print(result, end = "")


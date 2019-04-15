# 소수 찾기
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
# 주어진 수들 중 소수의 개수를 출력한다.
#
# 풀이 방법 : Math
# 에라토스테네스의 체 만들고, check

import sys
from math import sqrt
f = sys.stdin
n = int(f.readline())
arr = list(map(int, f.readline().split()))
result = 0
def isPrime(n):
    if n < 2: return 0
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0: return 0
    return 1

for i in range(n):
    result += isPrime(arr[i])
print(result, end = "")
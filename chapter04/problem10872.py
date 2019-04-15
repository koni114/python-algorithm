# 팩토리얼
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
# 첫째 줄에 정수 N(0 ≤ N ≤ 12)가 주어진다.
# 첫째 줄에 N!을 출력한다.

import sys
f = sys.stdin
n = int(f.readline())
def factorial(n):
    if n == 1 or n == 0: return 1
    return n * factorial(n-1)
print(factorial(n), end = "")

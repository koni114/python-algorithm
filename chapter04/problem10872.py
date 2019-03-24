# 팩토리얼
import sys
f = sys.stdin
n = int(f.readline())
def factorial(n):
    if n == 1 or n == 0: return 1
    return n * factorial(n-1)
print(factorial(n), end = "")

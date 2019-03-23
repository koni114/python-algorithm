# 소수 찾기
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
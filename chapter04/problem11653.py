# 소인수분해
# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.
# 첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.
# N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다.

# 풀이 방법 : Math
# 소인수 분해 할 줄 알지 ? ㅇ ㅋ

import sys
from math import sqrt
f = sys.stdin
n = int(f.readline())

def primeFactorization(number):
    k = int(sqrt(number))
    for i in range(2, k+3):
        while(True):
            if number % i == 0:
                print(i)
                number = number // i
            else:
                break

    if number > 1: print(number)

primeFactorization(n)
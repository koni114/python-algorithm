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
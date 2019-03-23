# 소수 구하기
import sys
from math import sqrt

f   = sys.stdin
A, B = map(int, f.readline().split())
arr = [i for i in range(B+1)]
arr[1] = 0
for i in range(2, int(sqrt(B))+1):
    if not arr[i]: continue
    for j in range(i+i, B+1, i):
        arr[j] = 0

for i in range(A, B+1):
    if arr[i] != 0:
        print(arr[i])

# 소수 구하기
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000)
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

# 풀이 방법 : Math
# 에라토스테네스의 체를 이용,

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

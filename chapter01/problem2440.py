# 별찍기

# 첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

import sys
f = sys.stdin
n = int(f.readline())

while(n != 0):
    print('*' * n)
    n = n - 1
# 별 찍기 - 17
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
#    *
#   * *
#  *   *
# *******

import sys
f = sys.stdin
n = int(f.readline())

total = (2*n-1)
for i in range(1,n+1):
    if i == 1: print(" "*((total-1)//2)+"*")
    elif i == n: print("*" * total)
    else: print(" "*((total-(2*i-1))//2)+"*" + " "*((2*i)-3)+"*")

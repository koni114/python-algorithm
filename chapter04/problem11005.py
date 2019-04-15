# 진법 변환 2
# 10진법 수 N이 주어진다. 이 수를 B진법으로 바꿔 출력하는 프로그램을 작성하시오.
# 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.
# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35
# 첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36) N은 10억보다 작거나 같은 자연수이다.
# 첫째 줄에 10진법 수 N을 B진법으로 출력한다.

import sys
f = sys.stdin
N, B = map(int, f.readline().split())
if N < B:
    if N < 10: result =  N
    else: result = chr(55 + N)

else: result = ""
while(N >= B):
    i, j = divmod(N, B)
    if j < 10:
        result = str(j) + result
    else:
        result = chr(55 + j) + result
    if i < B:
        if i < 10:
            result = str(i) + result
        else:
            result = chr(55 + i) + result
    N = i

print(result , end = "")

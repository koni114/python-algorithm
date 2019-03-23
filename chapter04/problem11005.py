# 진법 변환 2
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

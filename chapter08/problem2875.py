# 대회 or 인턴
import sys
f = sys.stdin
N,M,K = map(int,f.readline().split())

while(K > 0):
    if N <= 0 or M <= 0:
        result = 0
        break
    if N > 2*M:
        N = N-1
        K = K-1
    elif N < 2*M:
        K = K-1
        M = M-1
    else:
        K = K-3
        N = N-2
        M = M-1

if N >= 2*M: result = M
elif N < 2*M: result = N // 2
print(result, end = "")

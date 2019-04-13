# 부분 수열의 합
import sys
f    = sys.stdin
N, S = map(int, f.readline().split())
arr  = list(map(int, f.readline().split()))
result = 0
for i in range(1, 2**N):
    tmp = 0
    for j in range(N):
        if i & (1 << j): tmp += arr[j]
    if tmp == S:
        result += 1

print(result, end = "")
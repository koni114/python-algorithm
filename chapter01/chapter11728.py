# 배열 합치기
import sys
f = sys.stdin
n = len(f.readline().split())
result = []
for i in range(n):
    tmp = list(map(int, f.readline().strip().split()))
    result.extend(tmp)
result = sorted(result)
print(str(result).replace("[", "").replace(",", "").replace("]", ""))


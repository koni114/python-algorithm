# 30
import sys
f   = sys.stdin
result = 0
arr = list(map(int, list(f.readline().strip())))
if 0 not in arr or not sum(arr) % 3 == 0:
    print(-1)
else:
    print("".join([str(i) for i in sorted(arr, reverse= True)]))

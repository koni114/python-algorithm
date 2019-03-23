import sys
from collections import defaultdict
f = sys.stdin
n = int(f.readline())
arr = defaultdict(lambda : 0)

for i in range(n):
    arr[int(f.readline())] += 1

print(sorted(list(arr.items()), key = lambda x : (x[1], -x[0]), reverse= True)[0][0])

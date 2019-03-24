# ATM
import sys
f = sys.stdin
n = int(f.readline())
arr = map(int, f.readline().split())
arr = sorted(arr, reverse= True)
print(sum([(i+1)*j for i, j in enumerate(arr)]), end = "")
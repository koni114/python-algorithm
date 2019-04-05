# 랜선 자르기
import sys
sys.setrecursionlimit(10 ** 6)
from collections import deque
f = sys.stdin
k, n = map(int, f.readline().split())
arr = deque()
result = 0
max_length = 0
for i in range(k):
    tmp = int(f.readline().strip())
    max_length = max(max_length, tmp)
    arr.append(tmp)

def TreeCheck(n):
    if n == 0: return 0
    return sum([(i // n) for i in arr ])


def binarySearch(start, end, n):
    if start > end: return
    global result
    mid = (start + end) // 2
    line = TreeCheck(mid)
    # print("line :", line, "mid :", mid)
    if line >= n:
        result = max(result, mid)
        binarySearch(mid+1, end, n)
    else:
        binarySearch(start, mid-1, n)

binarySearch(1, max_length, n)
print(result, end = "")
# 나무 자르기
import sys
f = sys.stdin
n, m = map(int, f.readline().split())
arr = list(map(int, f.readline().split()))
max_len = max(arr)
result = 0
def cutTree(n):
    return sum([(i-n) for i in arr if i-n > 0])
def binarySearch(start, end, m):
    global result
    if start > end: return
    mid = (start + end) // 2
    Tree_len = cutTree(mid)
    # print("mid :", mid, "Tree_len :", Tree_len)
    if Tree_len >= m:
        result = max(result, mid)
        binarySearch(mid+1, end, m)
    else:
        binarySearch(start, mid-1,m)

binarySearch(1, max_len, m)
print(result, end = "")


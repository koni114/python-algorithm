# 공유기 설치
import sys
from collections import deque
f = sys.stdin
n, c = map(int, f.readline().split())
arr = deque()
for i in range(n):
    arr.append(int(f.readline().strip()))
arr = sorted(arr)
max_length = arr[-1] - arr[0]
result = 0
# print(arr)
def check(mid, c):
    c -= 1
    # print("mid:", mid)
    global n
    i = 0
    while(i < n-1):
        # print("i:", i, "c :", c, "n :", n)
        if c == 0: return True
        tmp = 0
        for j in range(i, n-1):
            i = j+1
            # print("j :", j)
            tmp += (arr[j+1] - arr[j])
            # print("tmp :", tmp)
            if tmp >= mid:
                c -= 1
                # print("correct :", j)
                break
    if c <= 0:
        return True
    else:
        return False

def binarySearch(start, end, c):
    if start > end: return
    global result
    mid = (start + end) // 2
    # print("mid :", mid, "check :", check(mid, c))
    if check(mid, c):
        result = max(result, mid)
        binarySearch(mid+1, end, c)
    else:
        binarySearch(start, mid-1, c)


binarySearch(1, max_length, c)
print(result, end = "")


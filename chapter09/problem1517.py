# 버블소트
import sys
from collections import deque
f = sys.stdin
n = int(f.readline())
arr = list(map(int,f.readline().split()))
# print("before arr :", arr)
result = 0
def mergeSort(start, end):
    global result
    if start >= end: return
    mid = (start + end) // 2

    mergeSort(start, mid)
    mergeSort(mid+1, end)
    i,j = start, mid+1
    tmp = deque()
    while(i <= mid and j <= end):
        if arr[i] > arr[j]:
            tmp.append(arr[j])
            j += 1
            result += (mid - i + 1)
        else:
            tmp.append(arr[i])
            i += 1
    while(i <= mid):
        tmp.append(arr[i])
        i += 1
    while(j <= end):
        tmp.append(arr[j])
        j += 1
    # print("tmp :", tmp )
    arr[start:end+1] = list(tmp)

mergeSort(0,n-1)
# print("after arr :", arr)
print(result, end = "")
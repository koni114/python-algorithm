# merge sort 구현
import random as ran
from collections import deque
arr = [ran.randint(1,10) for _ in range(10)]
print("before :", arr)

def mergeSort(left, right):
    if left >= right: return 0
    mid = (left + right) // 2

    mergeSort(left, mid-1)
    mergeSort(mid, right)

    tmp = deque()
    i,j = left, mid+1
    while(i <= mid and j <= right):
        if arr[i] < arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1
    while(i <=  mid):
        tmp.append(arr[i])
        i += 1
    while(j <= right):
        tmp.append(arr[j])0
        j += 1
    arr[left:right+1] = tmp


arr = [1,2,3,4,5]
tmp = deque([3,3,3,3,3])
arr[1:3] = tmp[1:3]

# merge sort 구현
import random as ran
from collections import deque
arr = [ran.randint(1,10) for _ in range(10)]
print("before :", arr)

from collections import deque
arr = [5, 4, 1, 2, 3]
def merge_sort(left, right):
    if left >= right:
        return

    mid = (left + right) // 2
    merge_sort(left, mid)
    merge_sort(mid+1, right)
    merge(left, right)

def merge(left, right):
    mid = (left + right) // 2
    i, j = left, mid+1

    tmp = deque()
    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1

    while i <= mid:
        tmp.append(arr[i])
        i += 1

    while j <= right:
        tmp.append(arr[j])
        j += 1

    arr[left:right+1] = tmp

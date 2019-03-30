import sys
import random as ran
arr = [ran.randint(1, 10) for _ in range(10)]
arr = sorted(arr)
print("arr :",arr)
n = ran.randint(1,10)
print("n: ", n)
cnt = 0

def binarySearch(left, right):
    global cnt
    cnt += 1
    print("phase :", cnt)
    print("left :", left, "right :", right)
    if left > right: return 0
    mid = (left + right) // 2

    if arr[mid] == n:
        print(mid)
    elif arr[mid] > n:
        right = mid-1
        binarySearch(left, right)
    else:
        left = mid+1
        binarySearch(left, right)

binarySearch(0, 9)

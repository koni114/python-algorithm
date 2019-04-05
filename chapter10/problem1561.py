# 놀이공원
import sys
f = sys.stdin
n,m = map(int, f.readline().split())
arr = list(map(int, f.readline().split()))
result = 0
max_length = n * max(arr)

def check(mid):
    b = sum([(mid // i)+1 for i in arr])
    tmp = 0
    for i in arr:
        if mid % i == 0:
            tmp += 1
    a = b - tmp + 1
    return (a,b)


def binarySearch(min, max, n):
    global result
    if min > max: return
    mid = (min + max) // 2
    # print("mid :", mid)
    a, b = check(mid)
    # print("a :", a, "b:", b)
    if a <= n and n <= b:
        arr2 = [i for i in enumerate(arr) if mid % i[1] == 0]
        if len(arr2) == 0:
            binarySearch(min, mid - 1, n)
        else:
            for i in range(len(arr2)):
                if (a+i) == n:
                    result = arr2[i][0]+1
    elif n < a:
        binarySearch(min, mid-1, n)
    else:
        binarySearch(mid+1, max, n)


binarySearch(0, max_length, n)
print(result, end = "")


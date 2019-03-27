# 숫자 카드2
import sys
from collections import defaultdict, deque
f = sys.stdin
number = int(f.readline()) - 1
right = number
left  = 0
arr   = sorted(list(map(int, f.readline().split())))
find_n = int(f.readline())
find_arr = list(map(int, f.readline().split()))
result = deque()

def binarySearch(left, right, n):
    global number
    if left > right:
        dict_arr[n] = 0
        return 0
    mid = (left + right) // 2
    if arr[mid] == n:
        tmp = 1
        a, b = (mid+1, mid-1)
        while a <= number and arr[a] == n:
            a = a+1
            tmp += 1
        while b >= 0 and arr[b] == n:
            b = b-1
            tmp += 1
        dict_arr[n] = tmp
        return tmp
    elif arr[mid] > n:
        right = mid-1
        return binarySearch(left, right, n)
    else:
        left = mid+1
        return binarySearch(left, right, n)


# 요행
dict_arr = defaultdict(lambda : -1)

for i in find_arr:
    if dict_arr[i] == -1:
        right = number
        left = 0
        result.append(binarySearch(left, right, i))
    else:
        result.append(dict_arr[i])

print(*list(result))

# 숫자 카드
import sys
from collections import defaultdict, deque
f = sys.stdin
n = int(f.readline()) - 1
right = n
left  = 0
arr   = sorted(list(map(int, f.readline().split())))
find_n = int(f.readline())
find_arr = list(map(int, f.readline().split()))
result = deque()

def binarySearch(left, right, n):
    if left > right:
        dict_arr[n] = 0
        return 0
    mid = (left + right) // 2
    if arr[mid] == n:
        dict_arr[n] = 1
        return 1
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
        right = n
        left = 0
        result.append(binarySearch(left, right, i))
    else:
        result.append(dict_arr[i])

print(*list(result))

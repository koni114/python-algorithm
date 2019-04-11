# 이전 순열(permutation)
import sys
f = sys.stdin
n = int(f.readline().strip())
arr = list(map(int, f.readline().split()))
def permutation(arr, n):
    i = n-1
    while i > 0 and arr[i-1] <= arr[i]:
        i -= 1
    if i == 0:
        print(-1, end = "")
        return
    j = n-1
    while j >= i and arr[i-1] <= arr[j]:
        j -= 1
    arr[i-1], arr[j] = arr[j], arr[i-1]

    j = n-1
    while i <= j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    print(*arr, end = "")

permutation(arr, n)
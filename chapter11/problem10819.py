# 차이를 최대로
import sys
sys.setrecursionlimit(10 ** 6)
f = sys.stdin
n = int(f.readline().strip())
arr = sorted(list(map(int, f.readline().split())))
def check(arr):
    tmp = 0
    for i in range(len(arr)-1):
        tmp += abs(arr[i]-arr[i+1])
    return tmp

result = check(arr)
def permutation(arr, n):
    global result
    i = n
    while i > 0 and arr[i] <= arr[i-1]:
        i -= 1
    if i == 0: return
    j = n
    while i <= j and arr[i-1] >= arr[j]:
        j -= 1

    arr[i-1], arr[j] = arr[j], arr[i-1]
    j = n
    while i <= j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    result = max(check(arr), result)
    permutation(arr, n)


permutation(arr, len(arr)-1)
print(result, end = "")
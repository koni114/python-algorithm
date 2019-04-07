# 모든 순열
# 다음 순열(next permutation)
import sys
f = sys.stdin
n = int(f.readline().strip())
arr = list(range(1,n+1))
print(*arr)
toggle = True
def permutation(arr, n):
    global toggle
    i = n-1
    while i > 0 and arr[i-1] >= arr[i]:
        i -= 1
    if i == 0:
        toggle = False
        return
    j = n-1
    while j >= i and arr[i-1] >= arr[j]:
        j -= 1
    arr[i-1], arr[j] = arr[j], arr[i-1]

    j = n-1
    while i <= j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    print(*arr)

while toggle:
    permutation(arr, n)
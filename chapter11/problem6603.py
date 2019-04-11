# 로또
import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
f = sys.stdin

# arr : 순열, n : len(arr)-1
def check(array):
    global arr
    tmp = deque()
    for i in range(len(array)):
        if array[i] == 1:
            tmp.append(arr[i])
    print(*tmp)

def permutation(arr, n):
    check(arr)

    i = n
    while i > 0 and arr[i] >= arr[i-1]:
        i -= 1

    if i == 0: return

    j = n
    while j >= i and arr[i-1] <= arr[j]:
        j -= 1

    arr[i-1], arr[j] = arr[j], arr[i-1]

    j = n
    while j >= i:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    permutation(arr, n)



while(True):
    arr = list(map(int, f.readline().split()))
    if arr[0] == 0:
        break
    else:
        n    = arr[0]
        arr  = arr[1:]
        init = [1 for i in range(6)]
        [ init.append(0) for _ in range(n-6)]
        # print("init :", init)
        permutation(init, n-1)
        print("")

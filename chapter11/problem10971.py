# 외판원 문제2
import sys
sys.setrecursionlimit(10 ** 6)
f = sys.stdin
n = int(f.readline().strip())
arr = [[] for i in range(n+1)]
for i in range(1, n+1):
    t = list(map(int, f.readline().split()))
    t.insert(0,0)
    arr[i] = t
result = 999999999
init = list(range(2, n+1))

# print("arr :", arr)


def calculate(vec):
    tmp = 0
    # print("vec :", vec)
    # print("vec[0] :", vec[0], "vec[-1]:", vec[-1])
    if arr[1][vec[0]] == 0 or arr[vec[-1]][1] == 0:
        return 0
    else:
        tmp += (arr[1][vec[0]] + arr[vec[-1]][1])

    for i in range(len(vec)-1):
        if arr[vec[i]][vec[i+1]] == 0: return 0
        tmp += arr[vec[i]][vec[i+1]]
    return tmp

# arr : 오름차순 배열, n : len(arr)-1
def permutation(arr, n):
    global result
    num = calculate(arr)
    if num:
        result = min(num, result)

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
    permutation(arr, n)

# if n == 2:
#     print(arr[1][2] + arr[2][1], end = "")
# else:
permutation(init, n-2)
print(result, end = "")
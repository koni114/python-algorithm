# 순열의 순서
import sys
sys.setrecursionlimit(10 ** 6)
from collections import deque
sys.setrecursionlimit(10 ** 6)
f = sys.stdin
n = int(f.readline().strip())
arr = list(map(int, f.readline().split()))
if arr[0] == 1:
    code, number = arr[0], arr[1]
    finalScore = deque()
    init = list(range(1, n+1))
else:
    code = arr[0]
    finalScore = arr[1:]
    init = list(range(1, n+1))

def factorial(n):
    if n <= 1: return 1
    return n*factorial(n-1)

def code1(result, arr):
    global number
    n = len(arr)
    if n <= 1:
        finalScore.append(arr[0])
        print(*finalScore, end = "")
        return
    n -= 1
    for i in range(n, -1, -1):
        k = factorial(n) * i
        if number >= (result+k):
            finalScore.append(arr[i])
            arr.remove(arr[i])
            code1(result+k, arr)
            break

def code2(result, arr):
    if len(arr) == 1:
        print(result, end = "")
        return
    n = len(arr) - 1
    for i in range(n+1):
        if finalScore[-(n+1)] == arr[i]:
            result = (result + (factorial(n)*i))
            arr.remove(arr[i])
            code2(result, arr)
            break

if code == 1:
    code1(1, init)
else:
    code2(1, init)
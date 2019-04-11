# 암호 만들기
import sys
from collections import deque
f = sys.stdin
L, C = map(int, f.readline().split())
arr  = sorted(f.readline().split())
check = ['a', 'e', 'i', 'o', 'u']
result = deque()

def makePassWord(s, a, b, currIdx):
    global L, C
    if len(s) == L:
        # print(s)
        if a>=2 and b>=1: result.append(s)
        return
    if currIdx >= C: return

    Toggle = False
    if arr[currIdx] in check:
        Toggle = True

    tmp = s+arr[currIdx]

    if Toggle:
        makePassWord(tmp, a, b+1, currIdx+1)
    else:
        makePassWord(tmp, a+1, b, currIdx+1)

    makePassWord(s, a, b, currIdx+1)


makePassWord("", 0, 0, 0)
[print(i) for i in result]
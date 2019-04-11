# 퍼즐
import sys
from collections import deque, defaultdict

f = sys.stdin
start = []
check = defaultdict(lambda : 0)
for i in range(3):
    start.extend(f.readline().split())

for i in range(9):
    if start[i] == '0':
        start[i] = '9'
        break

start.insert(0,'0')
nextArr = [0]
nextArr.append([2,4])
nextArr.append([1,3,5])
nextArr.append([2,6])
nextArr.append([1,5,7])
nextArr.append([2,4,6,8])
nextArr.append([3,5,9])
nextArr.append([4,8])
nextArr.append([5,7,9])
nextArr.append([6,8])

def change(s):
    for i in range(1,10):
        if s[i] == '9':
            idx = i
            break
    arr = []
    for i in nextArr[idx]:
        a = s[i]
        b = s[idx]
        tmp = s[:i] + b + s[i+1:]
        arr.append(tmp[:idx]+a+tmp[idx+1:])
    return arr

def bfs(start):
    d = deque()
    check[start] = True
    d.append([start,0])

    while len(d) != 0:
        currStr,n = d.popleft()
        if currStr == "0123456789": return n
        for tmp in change(currStr):
            if not check[tmp]:
                check[tmp] = True
                d.append([tmp, n+1])

    return -1

print(bfs("".join(start)), end = "")



# test
# 중량 제한
import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
f = sys.stdin
n,m = map(int, f.readline().split()) # n : 노드의 개수, m : 간선의 개수
max_weight = 0
result = 0
arr = deque()
[arr.append([]) for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int, f.readline().split())
    max_weight = max(max_weight, c)
    arr[a].append((b,c))
    arr[b].append((a,c))

startNode, endNode = map(int, f.readline().split())

def BFS(mid, sn = startNode, en = endNode):
    global n
    # print("mid :", mid)
    tmp = deque()
    tmp.append(sn)
    check = [False for i in range(n+1)]
    while(len(tmp) != 0):
        # print(tmp)
        currentNode = tmp.popleft()
        for nextNode, weight in arr[currentNode]:
            # print("nextNode :", nextNode, "weight: ", weight)
            if mid <= weight and not check[nextNode]:
                if nextNode == en: return True
                tmp.append(nextNode)
                check[nextNode] = True
    return False

def binarySearch(start, end):
    global result
    if start > end: return
    mid = (start + end) // 2
    if BFS(mid):
        result = max(result, mid)
        binarySearch(mid+1, end)
    else:
        binarySearch(start, mid-1)

binarySearch(1, max_weight+1)
print(result, end = "")




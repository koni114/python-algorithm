# 트리의 순회
import sys
from collections import deque
sys.setrecursionlimit(10**6)
f = sys.stdin
n = int(f.readline().strip())
inOrder   = list(map(int, f.readline().strip().split()))
postOrder = list(map(int, f.readline().strip().split()))
position = dict()
for i,j in enumerate(inOrder):
    position[j] = i
result = deque()

def solve(Is, Ie, Ps, Pe):
    if Is > Ie or Ps > Pe:
        return
    root = postOrder[Pe] #
    result.append(root)
    Ir = position[root]
    l = Ir - Is
    solve(Is, Ir-1, Ps, Ps+l-1)
    solve(Ir+1, Ie, Ps+l, Pe-1)
solve(0, n-1, 0, n-1)

print(*result, end = "")

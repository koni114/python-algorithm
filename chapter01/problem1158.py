from collections import deque
import sys
f = sys.stdin
N, M = [int(i) for i in f.readline().split()]
N_list = deque(range(1, N+1))
i = 0
print("<", end = "")
while(len(N_list) != 0):
    N_list.rotate(-(M - 1))
    if i != len(N_list)-1:
        print(N_list.popleft(), end = ", ")
    else:
        print(N_list.popleft(), end="")
print(">", end = "")


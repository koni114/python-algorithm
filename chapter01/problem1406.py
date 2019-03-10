from collections import deque
import sys

f = sys.stdin
left_stack  = deque(list(f.readline().strip()))
right_stack = deque()
n = int(f.readline())

for i in range(n):
    tmp = f.readline().strip()
    # print("tmp :", tmp)
    if tmp[0] == 'L':
        if len(left_stack) != 0:
            right_stack.appendleft(left_stack.pop())

    elif tmp[0] == 'D':
        if len(right_stack) != 0:
            left_stack.append(right_stack.popleft())

    elif tmp[0] == 'B':
        if len(left_stack) != 0:
            left_stack.pop()

    elif tmp[0] == 'P':
        left_stack.append(tmp[2])

print("".join(left_stack) + "".join(right_stack), end = "")



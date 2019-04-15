# 쇠막대기
# 백준 문제 참조,

# 풀이 방법 : stack을 이용해서 풀이


import sys
f = sys.stdin
pipe = f.readline().strip()
stack = 0
count = 0
for i in range(len(pipe)):
    if pipe[i] == '(':
        stack = stack + 1
    else:
        stack = stack - 1
        if pipe[i-1] == "(":
            count = count + stack
        else:
            count = count + 1
print(count)


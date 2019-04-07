# 집합
import sys
f = sys.stdin
n = int(f.readline().strip())
result = 0

def check(code, num=0):
    global result
    num = int(num)
    if code == "add":
        result = result | (1 << num)
    elif code == "remove":
        result = result & ~(1 << num)
    elif code == "check":
        if result & (1 << num) > 0:
            print(1)
        else:
            print(0)
    elif code == "toggle":
        result = result ^ (1 << num)
    elif code == "all":
        result = (1 << 21) -2
    else:
        result = 0

for i in range(n):
    tmp = f.readline().split()
    num = 0
    if len(tmp) > 1:
        code, num = tmp
    else:
        code = tmp[0]
    check(code, num)

# 날짜 계산
import sys
f = sys.stdin
e,s,m = map(int, f.readline().split())
result = 1
i = 1
j = 1
k = 1
while(True):
    if e == i and s == j and m == k:
        print(result, end = "")
        break
    if (i+1) % 16 == 0: i = 1
    else: i = i+1
    if (j+1) % 29 == 0: j = 1
    else: j = j+1
    if (k+1) % 20 == 0: k = 1
    else: k = k+1
    result += 1

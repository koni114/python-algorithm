# 병든 나이트
import sys
f = sys.stdin
N, M = map(int,f.readline().split())
if N <= 1 or M <= 1:
    print(1)
elif N == 2:
    if M >= 7:
        print(4)
    elif M >= 5:
        print(3)
    elif M >= 3:
        print(2)
    else:
        print(1)
else:
    if M >= 7:
        result = 4
        result += (M - 6)
        print(result)
    else:
        result = 1
        if M-1 <= 2:
            result += M-1
        else:
            result += 3
        print(result)
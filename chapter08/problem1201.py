import sys
from collections import deque
f= sys.stdin
n, up, down = map(int, f.readline().split())
num = 1
result = deque()
# 수열 생성 조건 확인
if n < up + down - 1 or n > (up * down):
    print(-1)
else:
    # 만족하는 감소 수열 만들기
    if up == 1:
        print(*sorted(list(range(1, n+1)), reverse = True))
    else:
        arr = deque()
        arr.append(down)
        a,b = divmod(n-down, up-1)
        for _ in range(up-1):
            if b != 0:
                arr.append(a+1)
                b -= 1
            else:
                arr.append(a)
        for i in arr:
            result.append(sorted(list(range(num, num+i)), reverse = True))
            num = num + i
        # print(result)
        print(*[j for i in result for j in i ])

# 팩토리얼 0의 개수
import sys
f = sys.stdin
n = int(f.readline())
k = 0
for i in range(1, 5):
    if n < pow(5, i):
        k = i-1
        break
result = 0

for i in range(1, k+1):
    for j in range(1, n+1):
        if j % pow(5, i) == 0:
            result += 1
print(result, end = "")

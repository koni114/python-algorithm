# 리모컨(1107)
import sys
f = sys.stdin
n = int(f.readline().strip())
unClick = int(f.readline().strip())
result = 10000000
if unClick == 0:
    arr = []
else:
    arr = list(map(int, f.readline().split()))

def click(n):
   for i in str(n):
       if int(i) in arr: return 0
   return len(str(n))

for i in range(0, 1000000):
    if click(i):
        tmp = click(i) + abs(n-i)
        result = min(result, tmp)

result = min(result, abs(100 - n))
print(result, end = "")


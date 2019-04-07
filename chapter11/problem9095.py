# 1, 2, 3 더하기
import sys
f = sys.stdin
n = int(f.readline().strip())
def bruteForce(n):
    global k
    global result
    if n > k: return
    if n == k: result += 1
    else:
        bruteForce(n+1)
        bruteForce(n+2)
        bruteForce(n+3)

for i in range(n):
    k = int(f.readline().strip())
    result = 0
    bruteForce(0)
    print(result)

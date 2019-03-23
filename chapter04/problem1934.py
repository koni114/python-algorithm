# 최소공배수
import sys
f = sys.stdin
n = int(f.readline())
def gcd(A, B):
    if B == 0: return A
    return gcd(B, A % B)

for i in range(n):
    A, B = map(int, f.readline().split())
    n_gcd = gcd(A, B)
    print((A*B) // n_gcd)
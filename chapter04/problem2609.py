import sys
f = sys.stdin
A, B = map(int, f.readline().split())

def gcd(A, B):
    if B == 0: return A
    return gcd(B, A % B)

n_gcd = gcd(A, B)
n_lcm = A * B // n_gcd

print(n_gcd)
print(n_lcm)


import sys
f = sys.stdin
n = int(f.readline())
def gcd(A, B):
    if B == 0: return A
    return gcd(B, A % B)

for i in range(n):
    arr = list(map(int, f.readline().split()))
    result = 0
    k, arr = arr[0], arr[1:]
    for i in range(k):
        for j in range(k):
            if not i == j:
                result += gcd(arr[i], arr[j])
    print(result // 2)

# Base Conversion
import sys
f = sys.stdin
A, B = map(int, f.readline().split())
n_decimal = 0
n    = int(f.readline())
arr = list(map(int, f.readline().split()))
# print("arr :", arr)

def changeToB(n, B):
    result = ""
    if n < B: return n
    while(n >= B):
        i , j = divmod(n, B)
        result = str(j) + " " + result
        n = i
        if i < B:
            result = str(i) + " " + result
    return result

for i in range(1, n+1):
    n_decimal += (pow(A, i-1) * arr[-i])

# print(n_decimal)
print(changeToB(n_decimal, B) , end = "")


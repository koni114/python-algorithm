import sys
f = sys.stdin
n = int(f.readline())

total = (2*n-1)
for i in range(1,n+1):
    if i == 1: print(" "*((total-1)//2)+"*")
    elif i == n: print("*" * total)
    else: print(" "*((total-(2*i-1))//2)+"*" + " "*((2*i)-3)+"*")

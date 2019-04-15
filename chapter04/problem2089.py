# -2진수
import sys
f = sys.stdin
n = int(f.readline())
if abs(n) >= 2: result = ""
elif n == -1: result = "11"
elif n == 0: result = "0"
else: result = 1

while(abs(n) >= 2):
    if n % 2 == 0:
        i, j = divmod(n, -2)
        result = str(abs(j)) + result
        n = i
    else:
        i, j = divmod(n, -2)
        result = str(abs(j)) + result
        n = i+1
    # print(result)
    if n == 1: result = "1" + result
    elif n == -1: result = "11" + result

print(result)

arr = [['a', 1], ['c', 3], ['c', 1]]
sorted(arr, key= lambda x : (x[0], x[1]), reverse = False)



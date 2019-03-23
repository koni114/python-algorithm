import sys
f = sys.stdin
n = int(f.readline())
arr = []
for i in range(n):
    arr.append([int(i) for i in f.readline().split()])
arr = sorted(arr, key = lambda x : (x[1], x[0]))
[print(str(i[0]) + " " + str(i[1])) for i in arr ]


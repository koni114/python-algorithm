import sys
f = sys.stdin
test = f.readline()
a = len(test)
for i in range(0, a, 10):
    print(test[i:i+10])
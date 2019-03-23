import sys
f = sys.stdin
A, B, C = map(int, f.readline().split())
[print((A+B) % C) for _ in range(2)]
[print((A*B) % C) for _ in range(2)]

# k번째 수
import sys
f = sys.stdin
A, K = [int(i) for i in f.readline().split() ]
# list_seq = sorted(list(map(int, f.readline().split())))
list_seq = sorted([int(i) for i in f.readline().split()])
print(list_seq[K-1], end = "")
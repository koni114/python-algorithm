import sys
inf = sys.stdin

T = inf.readline();
list_int = T.split()
answer = 0

for i in list_int:
    answer += int(i)

print(answer)


[int(i) for i in test.split()]
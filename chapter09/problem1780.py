# 종이 자르기
import sys
f = sys.stdin
N = int(f.readline())
paper = []
result = [0] * 3

for i in range(N):
    paper.append(list(map(int, f.readline().split())))

def check(a, b, size):
    for i in range(a, a+size):
        for j in range(b, b+size):
            if paper[a][b] != paper[i][j]: return False
    return True

def paperCheck(a, b, size):
    if size == 1:
        result[paper[a][b]+1] += 1
        return
    if check(a,b,size):
        result[paper[a][b]+1] += 1
        return
    else:
        tmp = size // 3
        paperCheck(a,b, tmp)
        paperCheck(a,b+tmp, tmp)
        paperCheck(a,b+(2*tmp),tmp)
        paperCheck(a+tmp, b, tmp)
        paperCheck(a+tmp, b+tmp, tmp)
        paperCheck(a+tmp, b+(2*tmp), tmp)
        paperCheck(a+(2*tmp), b, tmp)
        paperCheck(a+(2*tmp), b+tmp, tmp)
        paperCheck(a+(2*tmp), b+(2*tmp), tmp)

paperCheck(0,0,N)

[print(i) for i in result]
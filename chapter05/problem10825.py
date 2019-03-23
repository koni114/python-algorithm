# 국영수
# 국어 점수가 감소하는 순서로
# 국어 점수가 같으면 영어 점수가 증가하는 순서로
# 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
# 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)
import sys
f = sys.stdin
n = int(f.readline())
arr = []
for i in range(n):
    tmp = [i for i in f.readline().split()]
    arr.append([tmp[0], int(tmp[1]), int(tmp[2]), int(tmp[3])])
arr = sorted(arr, key = lambda x : (-x[1], x[2], -x[3], x[0]))
[print(i[0]) for i in arr ]
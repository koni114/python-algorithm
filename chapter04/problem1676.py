# 팩토리얼 0의 개수
# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
# 첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)
# 첫째 줄에 구한 0의 개수를 출력한다.

# 풀이 방법 : Math
# 0 이 나오는 개수는, 2,5 가 몇개인지 세보면 되지 않을까용 ?

import sys
f = sys.stdin
n = int(f.readline())
k = 0
for i in range(1, 5):
    if n < pow(5, i):
        k = i-1
        break
result = 0

for i in range(1, k+1):
    for j in range(1, n+1):
        if j % pow(5, i) == 0:
            result += 1
print(result, end = "")

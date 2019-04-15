# 배열 합치기
# 문제 : 정렬되어있는 두 배열 A와 B가 주어진다. 두 배열을 합친 다음 정렬해서 출력하는 프로그램
# 첫째 줄에 배열 A의 크기 N, 배열 B의 크기 M이 주어진다. (1 ≤ N, M ≤ 1,000,000)
# 둘째 줄에는 배열 A의 내용이, 셋째 줄에는 배열 B의 내용이 주어진다. 배열에 들어있는 수는 절댓값이 109보다 작거나 같은 정수이다.

# 첫째 줄에 두 배열을 합친 후 정렬한 결과를 출력한다.

# 풀이 방법 : 분할 정복의 알고리즘을 사용하는 merge sort의 정복 부분을 응용하자

import sys
f = sys.stdin
n = len(f.readline().split())
result = []
for i in range(n):
    tmp = list(map(int, f.readline().strip().split()))
    result.extend(tmp)
result = sorted(result)
print(str(result).replace("[", "").replace(",", "").replace("]", ""))

# 풀이 2
import sys
from collections import deque
f = sys.stdin
a, b = f.readline().split()
arr1 = deque(list(map(int, f.readline().split())))
arr2 = deque(list(map(int, f.readline().split())))
arr3 = deque()

while len(arr1) != 0 and len(arr2) != 0:
    if arr1[0] < arr2[0]:
        arr3.append(arr1.popleft())
    else:
        arr3.append(arr2.popleft())

while len(arr1) != 0:
    arr3.append(arr1.popleft())

while len(arr2) != 0:
    arr3.append(arr2.popleft())

print(*arr3)
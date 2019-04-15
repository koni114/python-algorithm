# 골드바흐의 추측
# 1742년, 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다.
# 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
# 예를 들어 8은 3 + 5로 나타낼 수 있고, 3과 5는 모두 홀수인 소수이다. 또, 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23 이다.
# 이 추측은 아직도 해결되지 않은 문제이다.
# 백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.

# 입력은 하나 또는 그 이상의 테스트 케이스로 이루어져 있다. 테스트 케이스의 개수는 100,000개를 넘지 않는다.
# 각 테스트 케이스는 짝수 정수 n 하나로 이루어져 있다. (6 ≤ n ≤ 1000000)
# 입력의 마지막 줄에는 0이 하나 주어진다.

# 각 테스트 케이스에 대해서, n = a + b 형태로 출력한다. 이때, a와 b는 홀수 소수이다. 숫자와 연산자는 공백 하나로 구분되어져 있다. 만약, n을 만들 수 있는 방법이 여러 가지라면,
# b-a가 가장 큰 것을 출력한다. 또, 두 홀수 소수의 합으로 n을 나타낼 수 없는 경우에는 "Goldbach's conjecture is wrong."을 출력한다.

# 풀이 방법 : Math
# 최대 값을 알아내어, 에라토스테네스의 체를 만듬. 이를 이용해 조합을 만들어냄
# Tip : 두 소수의 조합을 나타 낼 때 2중 for문 쓸 필요가 없음
#       case 마다 에라토스테네스의 체를 만들 필요가 없음

import sys
from math import sqrt
from collections import deque
number = deque()
max_n = 0
f = sys.stdin

while(True):
    n = int(f.readline())
    max_n = max(n, max_n)
    if n == 0: break
    number.append(n)

result = deque()
arr = [i for i in range(max_n+1)]
arr[1] = 0

# 에라토스테네스의 체 만들기
# 1. n 크기의 배열 생성
# 2. 1, sqrt(n) 까지의 배수를 지우기
for i in range(2, int(sqrt(max_n))+1):
    for j in range(i+i, max_n+1, i):
        arr[j] = 0
arr_short = [i[0] for i in enumerate(arr) if i[1]]

for k in number:
    for i in arr_short:
        if arr[k-i]:
            print(str(k) + " = " + str(i) + " + "+ str(k-i))
            break

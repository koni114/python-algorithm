# 최대공약수와 최소공배수
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를,둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

import sys
f = sys.stdin
A, B = map(int, f.readline().split())

def gcd(A, B):
    if B == 0: return A
    return gcd(B, A % B)

n_gcd = gcd(A, B)
n_lcm = A * B // n_gcd

print(n_gcd)
print(n_lcm)


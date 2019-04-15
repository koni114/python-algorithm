# 조합0의 개수
#


import sys
f = sys.stdin
two_value =  five_value = 0
n,m = map(int,f.readline().split())
max = n

def check(n, pow_n):
    max_n = 0
    result = 0
    for i in range(100):
        if pow(pow_n, i) > max:
            max_n = i
            break

    for i in range(1, max_n+1):
        result += n // pow(pow_n, i)

    return result

two_value = check(n, 2) - check(n-m, 2) - check(m, 2)
five_value += check(n, 5) - check(n-m, 5) - check(m, 5)
print(min(two_value ,five_value))







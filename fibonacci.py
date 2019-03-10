'''
fibonacci 수열.
'''

# 1. Top-Down
memo = [0] * 200
def fibonacci(n):
    if n <= 1:
        return n
    elif memo[n] > 0:
        return memo[n]
    memo[n] = (fibonacci(n-1) + fibonacci(n-2))
    return memo[n]

# 2. bottom-up

def fibonacci(n):
    memo2 = [0]*200
    for i in range(1,n+1):
        if i <= 1:
            memo2[i] = 1
        else:
            memo2[i] = memo2[i-1] + memo2[i-2]
    return memo2[n]


fibonacci(10)



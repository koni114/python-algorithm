# 입력 값이 n 일 때 피보나치 수열(n) 의 값을 구하는 함수 제작

def fibonacci(n):
    if n <= 0: return 0
    if n == 1: return 1
    return fibonacci(n-1) + fibonacci(n-2)


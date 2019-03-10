input_int = int(input("더하려고 하는 숫자를 입력하세요"))
def sum(n):
    if n == 0: return 0
    return n + sum(n-1)
sum(input_int)


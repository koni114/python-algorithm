# 1부터 n까지 연속한 숫자의 제곱의 합을 구하는 프로그램을 for 반복문으로 만들어 보세요
from math import *

def square2(n):
    sum = 0
    for i in range(1,n+1):
        sum += pow(i, 2)
    return(int(sum))


# 낙서장. TEST를 하기 위한 script

# factorial
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    print(result)

def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)


# 유클리드 알고리즘을 이용해서 gcd 만들기
def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

## 하노이 탑
#  크기가 다른 원반 n개를 출발점 기둥에서 도착점 기둥으로 전부 옮겨야 함
#  원반을 옮길 때는 한 기둥의 맨 위 원반을 뽑아,다른 기둥의 맨 위로만 옮길 수 있음
#  큰 원반을 작은 원반 위로 옮길 수 없음


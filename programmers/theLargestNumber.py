# 풀이의 핵심 : 최대 값이 1000 이라고 했으므로, 어떤 숫자이던지 간에, 중복하여 숫자를 만들고
#             이를 배열 함수(sorted) 를 이용하여 계산

def solution(numbers):
    # numbers = numbers[1:-2].split(", ")
    numbers = [str(i) for i in numbers]
    answer = ""
    final = list(enumerate([int((i*4)[0:4]) for i in numbers]))
    test = sorted(final, key=lambda final: final[1], reverse=True)
    for t in test: answer = answer + numbers[t[0]]
    return str(int(answer))

# testCase 11 : [0,0,0,0] -> int 로 변경후, str로 하지 않으면, "0000" 출력 됨
# testCase ** : [21, 212] ->
# -> 어떻게 예외 들을 다 처리해 나갈 것인가..?

# 기본적으로 저런 예외는 생각하기 힘듬.





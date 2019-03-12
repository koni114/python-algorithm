def solution(numbers):
    # numbers = numbers[1:-2].split(", ")
    numbers = [str(i) for i in numbers]
    answer = ""
    final = list(enumerate([int((i*4)[0:4]) for i in numbers]))
    test = sorted(final, key=lambda final: final[1], reverse=True)
    for t in test: answer = answer + numbers[t[0]]
    return str(int(answer))

# testCase 11 : [0,0,0,0]

import os
os.getcwd()
os.set
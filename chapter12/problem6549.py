# 히스토그램에서 가장 큰 직사각형
# 푸는 방법 : Stack 이용!
# stack에 막대를 넣기 전에, stack에 가장 위에 있는 막대 Top 과 현재 x의 높이 비교.
# top의 높이가 x의 높이가 크면, top을 높이로 하는 직사각형은 x를 지나갈 수 없다
# 스택에 값이 없는 경우, -> 해당 인덱스 stack에 추가

import sys
from collections import deque
f = sys.stdin
while(True):
    arr = list(map(int, f.readline().split()))
    if arr[0] == 0: break
    else:
        N   = arr[0]
        arr = arr[1:]
        s   = deque()
        result = 0


        for i in range(N+1):
            if i == N:
                # print(s)
                while len(s) != 0:
                    top = s.pop()
                    if len(s) != 0:
                        left = top - s[len(s) - 1]
                    else:
                        left = top+1
                    right = i - top
                    value = arr[top] * (left + right - 1)
                    # print("left :", left, "right :", right, "value :", value)
                    result = max(result, arr[top] * (left + right - 1))
            else:
                # print(s)
                if len(s) == 0: s.append(i)
                else:
                    while len(s) != 0:
                        if arr[s[len(s)-1]] <= arr[i]: # 스택의 top의 값이 현재 인덱스의 값보다 작거나 같은 경우, push
                            s.append(i)
                            break
                        else:                          # 스택의 top의 값이 현재 인덱스의 값보다 큰경우, check
                            top = s.pop()
                            if len(s) != 0:
                                left = top - s[len(s) - 1]
                            else:
                                left = top+1
                            right = i-top
                            value = arr[top] * (left + right - 1)
                            # print("i : ", i, "left :", left, "right :", right, "value :", value)
                            result = max(result, value)
                    s.append(i)

        print(result)




# 스택에 값이 있는 경우
# 스택의 top의 값이 현재 인덱스의 값보다 작거나 같은 경우, push
# 스택의 top의 값이 현재 인덱스의 값보다 큰경우, check
# (left + right -1) * top index의 높이
# left  : 현재 top index -  next top index
# right : curr index - 현재 top index

# currIdx == n, (끝 도착)
# stack 에 값을 한개씩 pop 하면서,
# (left + right -1) * top index의 높이
# left  : 현재 top index -  next top index
# right : curr index - 현재 top index







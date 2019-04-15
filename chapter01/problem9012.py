# 괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다.
# 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다.
# 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다.
# 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” ,
# 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다.
#
# 여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다.

# 풀이방법 : stack을 이용해, ( 괄호인 경우에는 stack에 추가하고, ) 인 경우에는 pop 을 사용해서 검사하면 됨

import sys
f = sys.stdin
testCase = int(f.readline())

for i in range(testCase):
    tmp = f.readline()
    # print("tmp :", tmp)
    count = 0
    for j in range(len(tmp)):
        if tmp[j] == "(":
            count = count + 1
            # print("count : ", count)
        else:
            if(count == 0):
                print("NO")
                break
            else:
                count = count - 1
                # print("count : ", count)
        if j == (len(tmp)-1):
            if count != 0:
                print("NO")
            else: print("YES")







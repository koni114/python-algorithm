# 알파벳 개수
# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각 알파벳이 단어에 몇 개가 포함되어 있는지 구하는 프로그램을 작성하시오.
# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.
# 단어에 포함되어 있는 a의 개수, b의 개수, …, z의 개수를 공백으로 구분해서 출력한다.

from collections import Counter
import sys
f = sys.stdin
tt = f.readline().strip()
final_list = [0]*26
for i, j in Counter(tt).items():
    final_list[(ord(i) - 97)] = j

for i in range(26):
    if i != 25:
        print(final_list[i], end = " ")
    else:
        print(final_list[i], end = "")

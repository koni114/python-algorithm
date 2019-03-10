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

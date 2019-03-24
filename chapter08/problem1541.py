# 잃어버린 괄호
import sys, re
f = sys.stdin
text = f.readline().strip()
value = list(map(int, re.split('\W+', text)))
plus_minus = re.split("[0-9]+", text)[1:-1]
if "-" in plus_minus:
    idx = plus_minus.index("-")+1
    print(sum(value[:idx]) - sum(value[idx:]), end = "")
else:
    print(sum(value), end = "")
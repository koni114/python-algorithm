import sys
inf = sys.stdin
T = inf.readline().strip()
for i in range(1, int(T)+1):
    list_int = [ int(i) for i in inf.readline().split() ]
    print("Case #" + str(i) + ":", sum(list_int))

import datetime
print((datetime.datetime.utcnow() + datetime.timedelta(hours=9)).strftime('%Y-%m-%d'))

print(96)
print("jaebig")

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






